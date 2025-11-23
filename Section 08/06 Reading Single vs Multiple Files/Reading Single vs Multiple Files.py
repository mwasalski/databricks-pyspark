# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [DataFrameReader](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.read.html)
# MAGIC - [csv()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.csv.html)
# MAGIC - [load()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.load.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading a single file

# COMMAND ----------

# You can read a single file by providing the path to that file

df = spark.read.format("csv").option("header", True).load("/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading multiple files

# COMMAND ----------

# If you provide the path to a directory it will read all files of the specified format (in this case 'csv') and append them together

df = spark.read.format("csv").option("header", True).load("/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population_partitioned/")

df.display()

# COMMAND ----------

