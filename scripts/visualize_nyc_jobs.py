import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('output/nyc_jobs_cleaned.csv', parse_dates=['posting_date'])

# Create salary_midpoint if not already done
df['salary_midpoint'] = (df['salary_range_from'] + df['salary_range_to']) / 2

# -----------------------------------
# 1. Salary Trend Over Time
# -----------------------------------
df['posting_month'] = df['posting_date'].dt.to_period('M')
monthly_salary = df.groupby('posting_month')['salary_midpoint'].mean()
monthly_salary.index = monthly_salary.index.to_timestamp()

plt.figure(figsize=(10, 6))
plt.plot(monthly_salary.index, monthly_salary.values, marker='o', linestyle='-', color='blue')
plt.title('Average Tech Job Salary in NYC Over Time')
plt.xlabel('Posting Month')
plt.ylabel('Average Salary ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('output/salary_trend.png')
plt.show()

# -----------------------------------
# 2. Top Paying Agencies
# -----------------------------------
agency_salary = df.groupby('agency')['salary_midpoint'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
agency_salary.plot(kind='barh', color='green')
plt.title('Top Paying Agencies (Avg Salary)')
plt.xlabel('Average Salary ($)')
plt.ylabel('Agency')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('output/top_agencies.png')
plt.show()

# -----------------------------------
# 3. Top Job Titles
# -----------------------------------
top_titles = df['business_title'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_titles.plot(kind='bar', color='orange')
plt.title('Top 10 Most In-Demand Tech Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Number of Postings')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('output/top_job_titles.png')
plt.show()

# -----------------------------------
# 4. Salary Distribution
# -----------------------------------
plt.figure(figsize=(10, 6))
df['salary_midpoint'].plot(kind='hist', bins=20, color='purple', edgecolor='black')
plt.title('Salary Distribution of Tech Jobs')
plt.xlabel('Salary ($)')
plt.ylabel('Number of Jobs')
plt.tight_layout()
plt.savefig('output/salary_distribution.png')
plt.show()
