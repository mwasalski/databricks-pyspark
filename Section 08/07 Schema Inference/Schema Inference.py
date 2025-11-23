# Databricks notebook source
# MAGIC %md
# MAGIC ### 📌 Reading in the countries data

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

# COMMAND ----------

df = spark.read.format("csv").options(header= True).load(path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 The following methods and attributes allow you to see the schema

# COMMAND ----------

df.dtypes

# COMMAND ----------

df.describe()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Explicitly inferring the schema via the inferSchema method - wnioskowanie typów danych

# COMMAND ----------

df = spark.read.format("csv").options(header=True, inferSchema=True).load(path)

df.display()

# COMMAND ----------

df.dtypes