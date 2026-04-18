# Databricks notebook source
# MAGIC %md
# MAGIC Read data from Silver -> studaidata_cleansed table

# COMMAND ----------

df = spark.read.table("aidatabricks01.aiadat_schema.studaidata_cleansed")

# COMMAND ----------

# MAGIC %md
# MAGIC Add Coulumns Usage_Category based on Task_Frequency_Daily

# COMMAND ----------

df_enriched = df.withColumn(
    "Usage_category",
    when(col("Task_Frequency_Daily") < 2, "Low")
    .when(col("Task_Frequency_Daily") < 5, "Medium")
    .otherwise("High")
)

# COMMAND ----------

# MAGIC %md
# MAGIC Impact_due_to_AI to capture the impact by finding difference between GPA_Bsaeline and after GPA_post_AI

# COMMAND ----------


df_enriched = df_enriched.withColumn(
    "Impact_on_Grade",
    when((round(col("GPA_Post_AI") - col("GPA_Baseline"), 2)) < 0, "Decline")
    .when((round(col("GPA_Post_AI") - col("GPA_Baseline"), 2)) > 0, "Increase")
    .otherwise("No Change")
)

# COMMAND ----------

df_enriched.write.mode("overwrite").saveAsTable("aiadat_schema.studaidata_enriched")