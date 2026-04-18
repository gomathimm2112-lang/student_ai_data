# Databricks notebook source
# MAGIC %md
# MAGIC Read CSV file from Bronze -> Processed 

# COMMAND ----------

df = spark.read.csv("abfss://bronze@aistracc.dfs.core.windows.net/ingest/studaidata_ingest", header=True, inferSchema=True)


# COMMAND ----------

# MAGIC %md
# MAGIC Drop NULL values

# COMMAND ----------

df = df.dropDuplicates().dropna()

# COMMAND ----------

# MAGIC %md
# MAGIC Write to studaidata_cleansed table for next processing

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("aiadat_schema.studaidata_cleansed")