# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [join](https://spark.apache.org/docs/3.5.3/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.join.html?highlight=join#pyspark.sql.DataFrame.join)
# MAGIC - [crossjoin](https://spark.apache.org/docs/3.5.3/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.crossJoin.html?highlight=join#pyspark.sql.DataFrame.crossJoin)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating DataFrames

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define schema for df_1 (Sales) with transaction_id included
schema_sales = StructType([
    StructField("transaction_id", IntegerType(), True),
    StructField("store_id", IntegerType(), True),
    StructField("sale_date", StringType(), True),
    StructField("sales_amount", IntegerType(), True)
])

# Data for df_1: sales records
# Some store_ids (e.g., 106 and 107) are not present in df_2 to demonstrate join gaps.
data_sales = [
    (1001, 103, "2025-01-15", 5000),
    (1002, 104, "2025-01-16", 7000),
    (1003, 105, "2025-01-17", 6500),
    (1004, 106, "2025-01-18", 4800),
    (1005, 107, "2025-01-19", 5300)
]

# Create df_1 with the sales data
df_1 = spark.createDataFrame(data_sales, schema=schema_sales)
df_1.show()

# Define schema for df_2 (Stores)
schema_stores = StructType([
    StructField("id", IntegerType(), True),
    StructField("store_name", StringType(), True),
    StructField("city", StringType(), True)
])

# Data for df_2: stores
data_stores = [
    (101, "Store A", "New York"),
    (102, "Store B", "Los Angeles"),
    (103, "Store C", "Chicago"),
    (104, "Store D", "Houston"),
    (105, "Store E", "Phoenix")
]

# Create df_2 with the stores data
df_2 = spark.createDataFrame(data_stores, schema=schema_stores)
df_2.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Left Join

# COMMAND ----------

left_join_df = df_1.join(df_2, df_1.store_id == df_2.id, "left")

left_join_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Right Join

# COMMAND ----------

right_join_df = df_1.join(df_2, df_1.store_id == df_2.id, "right")

right_join_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Inner Join

# COMMAND ----------

inner_join_df = df_1.join(df_2, df_1.store_id == df_2.id, "inner")

inner_join_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Full Outer Join

# COMMAND ----------

full_join_df = df_1.join(df_2, df_1.store_id == df_2.id, "fullouter")

full_join_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Left Anti Join

# COMMAND ----------

left_anti_df = df_1.join(df_2, df_1.store_id == df_2.id, "left_anti")

left_anti_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ### 📌 Cross Join

# COMMAND ----------

df_1.crossJoin(df_2).display()