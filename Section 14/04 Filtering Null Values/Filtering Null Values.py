# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [dropna()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.dropna.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Spark DataFrame

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# sample data: (id, name, age)
data = [
    (1,    "Alice",    23),
    (2,    None,       30),    # name is null
    (None, "Bob",      None),  # id and age are null
    (4,    "Charlie",  25),
    (None, None,       None)   # entire row null
]

# define schema
schema = StructType([
    StructField("id",   IntegerType(), True),
    StructField("name", StringType(),  True),
    StructField("age",  IntegerType(), True)
])

# create DataFrame
df = spark.createDataFrame(data, schema)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 dropna

# COMMAND ----------

df.dropna().display()

# COMMAND ----------

# By default how = 'any' unless specified

df.dropna(how='all').display()

# COMMAND ----------

# Drop rows that have less than thresh non-null values. This overwrites the how parameter.

df.dropna(thresh=2).display()

# COMMAND ----------

# List of columns to consider
 
df.dropna(subset=['name', 'age']).display()