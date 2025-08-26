import pandas as pd

df = pd.read_csv('output/nyc_jobs_cleaned.csv', parse_dates=['posting_date'])
print("Cleaned data loaded:", df.shape)


print("\n Top 10 job titles:")
print(df['business_title'].value_counts().head(10))

print("\n Top 10 hiring agencies:")
print(df['agency'].value_counts().head(10))

# Create midpoint salary column
df['salary_midpoint'] = (df['salary_range_from'] + df['salary_range_to']) / 2

print("\n Salary summary:")
print(df['salary_midpoint'].describe())

print("\n Average salary by agency (Top 10):")
agency_salary = df.groupby('agency')['salary_midpoint'].mean().sort_values(ascending=False).head(10)
print(agency_salary)

# Convert to posting month
df['posting_month'] = df['posting_date'].dt.to_period('M')

# Group by month and calculate mean salary
monthly_salary = df.groupby('posting_month')['salary_midpoint'].mean()

print("\n🔹 Average salary by posting month:")
print(monthly_salary.tail(10))  # Show most recent months


