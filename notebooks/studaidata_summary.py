# Databricks notebook source
from pyspark.sql.functions import when, col, sum, round, count

# COMMAND ----------

df = spark.read.table("aidatabricks01.aiadat_schema.studaidata_enriched")

# COMMAND ----------

# MAGIC %md
# MAGIC Summarise 

# COMMAND ----------

df_impact = df.groupBy("Impact_on_Grade").agg(
    count(col("Impact_on_Grade")).alias("Change_in_student")
)

# COMMAND ----------

# MAGIC %md
# MAGIC Categorise based on Primary AI tool

# COMMAND ----------

df_tool = df.groupBy("Primary_AI_Tool").agg(
    sum("Task_Frequency_Daily").alias("Total_Hours")
)

# COMMAND ----------

# MAGIC %md
# MAGIC Summarise based on Purpose of usage

# COMMAND ----------

df_gold_1 = df.groupBy("Main_Usage_Case") \
              .agg(count("*").alias("Usage_count"))

# COMMAND ----------

# MAGIC %md
# MAGIC Summarise the based on Student's Major subject

# COMMAND ----------

df_gold_2 = df.groupBy("Major") \
              .agg(sum("Task_Frequency_Daily").alias("Total_major_usage"))

display(df_gold_3)

# COMMAND ----------

# MAGIC %md
# MAGIC Summarise based on Ethics of AI usage

# COMMAND ----------

df_gold_3 = df.groupBy("AI_Ethics_Concern") \
              .agg(count("*").alias("Ethics_of_Usage"))

display(df_gold_4)

# COMMAND ----------

# MAGIC %md
# MAGIC Summarise based on usage and Impact_on_Grade

# COMMAND ----------

df_final = df.groupBy("Usage_category", "Impact_on_Grade") \
              .agg(count("*").alias("Total_count"))

# COMMAND ----------

# MAGIC %md
# MAGIC Write the final analysed data to table 

# COMMAND ----------

df_final.write.mode("overwrite").saveAsTable("aiadat_schema.studaidata_final")