# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [union](https://spark.apache.org/docs/3.5.3/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.union.html)
# MAGIC - [unionByName](https://spark.apache.org/docs/3.5.3/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unionByName.html)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating DataFrames

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# COMMAND ----------

# Define schema for df_1 (stores)
schema_stores_1 = StructType([
    StructField("id", IntegerType(), True),
    StructField("store_name", StringType(), True),
    StructField("city", StringType(), True),
    StructField("country", StringType(), True)
])

# Data for df_1: stores
data_stores_1 = [
    (101, "Store A", "New York", "USA"),
    (102, "Store B", "Los Angeles", "USA"),
    (103, "Store C", "Chicago", "USA"),
    (104, "Store D", "Houston", "USA"),
    (105, "Store E", "Phoenix", "USA")
]

# Create df_2 with the stores data
df_1 = spark.createDataFrame(data_stores_1, schema_stores_1)
df_1.show()

# Define schema for df_2 (stores)
schema_stores_2 = StructType([
    StructField("id", IntegerType(), True),
    StructField("store_name", StringType(), True),
    StructField("city", StringType(), True)
    ])

# Data for df_2: stores
data_stores_2 = [
    (101, "Store A", "New York"),
    (102, "Store B", "Los Angeles"),
    (103, "Store C", "Chicago"),
    (104, "Store D", "Houston"),
    (105, "Store E", "Phoenix")
]

# Create df_2 with the stores data
df_2 = spark.createDataFrame(data_stores_2, schema_stores_2)
df_2.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 union()

# COMMAND ----------

df_1.union(df_1).display()

# COMMAND ----------

# Union is positional, both DataFrames need the same number of columns

df_1.union(df_2).display()

# COMMAND ----------

df_1.union(df_2.select("id", "city", "store_name", "store_name")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 unionByName()

# COMMAND ----------

# Unless you specify allowMissingColumns=True you will get an error if both DataFrames do not have the same columns

df_1.unionByName(df_2).display()

# COMMAND ----------

df_1.unionByName(df_2, True).display()