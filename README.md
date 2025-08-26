# NYC Tech Jobs Data Pipeline

This project analyzes NYC government job postings with a focus on technology-related roles such as engineering and information technology. The dataset was sourced from NYC Open Data and includes thousands of postings across various departments and agencies.

The project was built to simulate a real-world data pipeline: starting from raw data ingestion, followed by data cleaning and transformation, exploratory analysis, and visualization of insights. The code is structured in a modular and reproducible way, using separate scripts for each stage.

## Project Objectives

- Clean and standardize the raw job postings dataset
- Filter the data to focus on tech-related job categories
- Analyze salary ranges, job demand, and agency-level hiring patterns
- Visualize trends in salaries, job titles, and hiring activity

## Project Structure

nyc-tech-jobs-pipeline/
├── data/ # Raw or sample dataset (optional)

├── output/ # Cleaned CSV file and generated charts

├── scripts/

│ ├── clean_nyc_jobs.py # Data cleaning and filtering

│ ├── analyze_nyc_jobs.py # Exploratory data analysis

│ └── visualize_nyc_jobs.py # Visualizations

├── requirements.txt # Python package dependencies

└── README.md # Project summary and instructions


## Pipeline Overview

The pipeline is divided into three modular scripts:

1. **Data Cleaning (`clean_nyc_jobs.py`)**
   - Standardizes column names and formats
   - Removes irrelevant or incomplete records
   - Filters for tech-related job categories

2. **Data Analysis (`analyze_nyc_jobs.py`)**
   - Identifies top job titles and hiring agencies
   - Calculates salary statistics and trends

3. **Data Visualization (`visualize_nyc_jobs.py`)**
   - Generates charts for salary trends, job demand, and agency comparisons



Why I Built This

This project was built as part of my learning in data engineering and to gain hands-on experience with real-world public datasets. The focus was on writing modular, reproducible code that reflects how data pipelines are designed in production environments. It helped me strengthen my understanding of data cleaning, filtering, analysis, and visualization — all critical skills for working with operational data.
