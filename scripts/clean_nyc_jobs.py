import pandas as pd

df = pd.read_csv('data/nyc_jobs_raw.csv.csv')
print("Loaded data:", df.shape)

print("\n Column names:")
print(df.columns.tolist())

print("\n Missing values per column:")
print(df.isnull().sum())

print("\n🔹 First 5 rows:")
print(df.head())

#Cleaning
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(' ', '_')
              .str.replace(r'[^a-z0-9_]', '', regex=True)
)
print(" Columns cleaned:", df.columns.tolist())

df = df.drop(columns=['recruitment_contact'])
print(" Dropped unnecessary columns")


df = df.dropna(subset=['salary_range_from', 'job_category', 'posting_date'])
print("✅ Dropped rows with missing critical values")

df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')
df['process_date'] = pd.to_datetime(df['process_date'], errors='coerce')
print("✅ Converted date fields to datetime")

# Trim spaces in all string fields
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
print("✅ Stripped whitespace from all string fields")

# Filter for Engineering and IT jobs only
relevant_categories = [
    'Engineering, Architecture & Planning',
    'Information Technology & Telecommunications'
]

print("🔍 Unique job categories BEFORE filtering:")
print(df['job_category'].value_counts())


# Filter rows that CONTAIN Engineering or IT in job_category
df = df[
    df['job_category'].str.contains('engineering', case=False, na=False) |
    df['job_category'].str.contains('information technology', case=False, na=False)
]

print(f"✅ Filtered rows: {df.shape[0]} remaining")


df.to_csv('C:/Users/laxmi/nyc_jobs_etl/output/nyc_jobs_cleaned.csv', index=False)
print("✅ Cleaned data saved to output/nyc_jobs_cleaned.csv")

'''

    print("🧪 Actual job_category values:")
    print(df['Job Category'].value_counts())
    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

    #    df = df[df['job_category'].isin(['Information Technology', 'Engineeing'])]

    #   df.to_csv('C:/Users/laxmi/nyc_jobs_etl/output/nyc_jobs_cleaned.csv', index=False)
'''