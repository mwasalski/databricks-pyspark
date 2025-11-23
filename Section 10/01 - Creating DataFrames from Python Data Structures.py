# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [createDataFrame()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.createDataFrame.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

# Define a list of records, where each inner list represents [name, age, city]
data_1 = [
    ["Alice", 30, "London"],
    ["Bob",   25, "New York"],
    ["Carol", 27, "San Francisco"],
    ["Dave",  35, "Berlin"],
]

# Specify the schema as a SQL DDL string: column names and types
schema = "name string, age integer, city string"

# Create a Spark DataFrame from the in-memory list using the given schema,
# then display it in the notebook
spark.createDataFrame(data_1, schema).display()

# COMMAND ----------

# Create and display a Spark DataFrame from a list of dicts
data_2 = [
    {"name": "Alice", "age": 30, "city": "London"},
    {"name": "Bob",   "age": 25, "city": "New York"},
    {"name": "Carol", "age": 27, "city": "San Francisco"},
    {"name": "Dave",  "age": 35, "city": "Berlin"},
]

spark.createDataFrame(data_2).display()