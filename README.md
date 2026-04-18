📌 Project Overview
This project is an end-to-end data engineering pipeline built on Microsoft Azure to analyze how students use AI tools and how it impacts their academic performance.
The pipeline ingests raw data, processes it through a medallion architecture, and generates analytical insights using PySpark in Databricks.

🎯 Problem Statement
Students are increasingly using AI tools in education. This project aims to analyze:
* How students use AI tools
* Which tools are most popular
* How AI usage impacts academic performance
* Usage patterns across majors and purposes

🧱 Architecture 
The pipeline follows a Medallion Architecture:

Bronze Layer → Raw data ingestion via Azure Data Factory
Silver Layer → Data cleaning & transformation using Azure Databricks
Gold Layer → Aggregated analytical tables stored as Delta table

ADF → ADLS (Bronze) → Databricks (Silver/Gold)

⚙️ Tech Stack
Azure Data Factory (ETL orchestration)
Azure Data Lake Storage Gen2 (data storage)
Azure Databricks (data processing)
PySpark (data transformation)

🔄 Data Pipeline Steps
1. Data Ingestion
Raw dataset loaded into ADLS using Azure Data Factory
2. Data Cleaning (Silver Layer)
Removed null values and duplicates
Add new columns Usage_Category and Impact_due_to_AI with the available data 
4. Data Transformation
Aggregations for analytics
5. Gold Layer (Analytics Tables)
Created 5 analytical visualisation based on:
AI usage vs Impact on grade
Usage of popular AI tools
Purpose of AI usage
Usage based on Major subjects of students
Ethics of AI usage

Created Final delta table with the usage and impact on grade data

📊 Key Insights
* High AI usage shows correlation with improved academic performance
* Usage patterns shows AI tool is equally used by all major subject students
* All major AI tool are equaly used my students
* AI is used slightly more for Exam preparation purpose than other
* Usage ethics is majorly low

📁 Project Structure
* pipelines/   → ADF pipeline JSON
* notebooks/   → Databricks PySpark code
* jobs/        → Databricks job config
* images/      → Architecture + charts

🚀 How to Run
-> Upload dataset to Azure Data Lake Storage
-> Trigger Azure Data Factory pipeline
-> Run Databricks job to run Databricks notebooks in sequence:
       Cleaning → Transformation → Gold Layer

📌 Future Improvements
. Add real-time streaming pipeline
. Build dashboard using Power BI or Streamlit
. Automate CI/CD deployment

👨‍💻 Author
Gomathi Katipally
