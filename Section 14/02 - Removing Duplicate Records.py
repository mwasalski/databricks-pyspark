# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [dropDuplicates()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.dropDuplicates.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Spark DataFrame

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define Schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True)
])

# Sample Data (with Duplicates)
data = [
    (1, "Alice", "HR"),
    (2, "Bob", "IT"),
    (3, "Charlie", "Finance"),
    (1, "Alice", "HR"),  # Duplicate row
    (2, "Bob", "IT"),    # Duplicate row
    (4, "David", "HR"),
    (3, "Charlie", "Finance"),  # Duplicate row
    (5, "Alice", "Finance"),  # Same name, different department
    (6, "Bob", "HR")  # Same name, different department
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

# Removes duplicate rows from the DataFrame, keeping only the first occurrence of each unique row.

df.dropDuplicates().show()

# COMMAND ----------

# Removes duplicate rows based on the "name" column, keeping only the first occurrence of each unique name.

df.dropDuplicates(["name"]).show()

# COMMAND ----------

# Removes duplicate rows based on the "name" and "department" columns, keeping only the first occurrence of each unique name and department.

df.dropDuplicates(["name", "department"]).show()