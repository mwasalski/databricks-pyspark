# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [curdate()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.curdate.html)
# MAGIC - [current_timestamp()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.current_timestamp.html)
# MAGIC - [timestamp_diff()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.timestamp_diff.html)
# MAGIC - [date_add()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.date_add.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Spark DataFrame

# COMMAND ----------

schema = "name string, hire_date string"

# Create a minimal DataFrame with name and hire_date
data = [
    ("Alice", "15-06-2020"),
    ("Bob", "25-09-2018"),
    ("Charlie", "05-12-2022")
    ]

df = spark.createDataFrame(data, schema)

df = df.withColumn("hire_date", to_date("hire_date", "dd-MM-yyyy"))

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

from pyspark.sql.functions import curdate, current_timestamp, timestamp_diff

# COMMAND ----------

# curdate() and current_timestamp()
 
df = df.\
        withColumn("last_updated_date", curdate()).\
        withColumn("last_updated_timestamp", current_timestamp())

df.display()

# COMMAND ----------

# timestamp_diff

df.withColumn("days_since_hired", timestamp_diff("DAY", "hire_date", "last_updated_date")).display()

df.withColumn("days_since_hired", timestamp_diff("MONTH", "hire_date", "last_updated_date")).display()

df.withColumn("days_since_hired", timestamp_diff("MONTH", "hire_date", "last_updated_timestamp")).display()

# The time element for a date column is midnight, e.g."2020-06-15" is "2020-06-15T00:00:00"
df.withColumn("days_since_hired", timestamp_diff("MONTH", "hire_date", "last_updated_timestamp")).display()

# COMMAND ----------

# date_add()

df.withColumn("hire_date_plus_10", date_add("hire_date", 10)).display()
df.withColumn("hire_date_minus_10", date_add("hire_date", -10)).display()