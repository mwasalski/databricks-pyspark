# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Delta Lake Transaction Log](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Inspecting the Delta Log After executing each code cell one by one

# COMMAND ----------

# A JSON file will be created to capture this transaction

data = [
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 90},
    {"id": 3, "name": "Charlie", "score": 78},
    {"id": 4, "name": "Diana", "score": 92},
    {"id": 5, "name": "Ethan", "score": 88},
    {"id": 6, "name": "Fiona", "score": 81},
    {"id": 7, "name": "George", "score": 74},
    {"id": 8, "name": "Hannah", "score": 95},
    {"id": 9, "name": "Ian", "score": 69},
    {"id": 10, "name": "Jasmine", "score": 87}
]

spark.createDataFrame(data).\
    write.mode("append").\
    format("delta").\
    save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/")

# COMMAND ----------

# Another JSON file will be created to capture this transaction

data2 = [
    {"id": 11, "name": "Kevin", "score": 83},
    {"id": 12, "name": "Lena", "score": 91},
    {"id": 13, "name": "Marcus", "score": 77},
    {"id": 14, "name": "Nina", "score": 89},
    {"id": 15, "name": "Oscar", "score": 72},
    {"id": 16, "name": "Priya", "score": 94},
    {"id": 17, "name": "Quinn", "score": 79},
    {"id": 18, "name": "Ravi", "score": 88},
    {"id": 19, "name": "Sophie", "score": 86},
    {"id": 20, "name": "Tom", "score": 80}
]

spark.createDataFrame(data2).\
    write.mode("append").\
    format("delta").\
    save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/")

# COMMAND ----------

# Another JSON file will be created to capture this transaction, this time with remove entries
# In the Delta Lake transaction log, a "remove" entry marks a data file as no longer part of the active table snapshot
# You may also get an auto commit for an OPTIMIZE command

from delta.tables import DeltaTable

dt = DeltaTable.forPath(spark, "/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/")

dt.delete("score < 80")

# COMMAND ----------

# Multiple commits will result in compacting JSON files and checkpointing

for i in range(50):
    spark.createDataFrame(data2).write.mode("append").format("delta").save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/student_data/")