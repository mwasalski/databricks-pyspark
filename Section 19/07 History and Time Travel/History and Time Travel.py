# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Work with Delta Lake table history](https://learn.microsoft.com/en-us/azure/databricks/delta/history)
# MAGIC - [Restore a Delta table to an earlier state](https://learn.microsoft.com/en-us/azure/databricks/delta/history#restore)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Delta Table History

# COMMAND ----------

spark.sql("""
          DESCRIBE HISTORY delta.`/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/`
          """).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Viewing Previous versions of the Delta Table

# COMMAND ----------

# Using versionAsOf option

spark.read.\
    format("delta").\
    option("versionAsOf", "enter version here...").\ 
    load("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/").\
    display()

# COMMAND ----------

# Using timestampAsOf option

spark.read.\
    format("delta").\
    option("timeStampAsOf", "enter timestamp here...").\
    load("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/").\
    display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Restore a Delta table to an earlier state

# COMMAND ----------

spark.sql("""
          RESTORE delta.`/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/` TO VERSION AS OF 0
          """)