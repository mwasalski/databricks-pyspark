# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [What are user-defined functions](https://learn.microsoft.com/en-us/azure/databricks/udf/)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Python UDF

# COMMAND ----------

# Creating a Python UDF
from pyspark.sql.types import IntegerType

@udf(IntegerType())
def get_length(x):
    return len(x)

# COMMAND ----------

# Calling the UDF
df = spark.read.table("population_metrics.default.countries_consolidated")

df.withColumn("country_length", get_length(df.country)).display()