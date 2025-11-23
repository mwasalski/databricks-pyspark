# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [to_date()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_date.html)
# MAGIC - [to_timestamp()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html)
# MAGIC - [date_format()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.date_format.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Standard Date Format Patterns

# COMMAND ----------

# MAGIC %md
# MAGIC Date: `yyyy-MM-dd`
# MAGIC
# MAGIC Timestamp: `'yyyy-MM-dd[T]HH:mm:ss[.SSSSSS]`
# MAGIC

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

df.printSchema

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

from pyspark.sql.functions import to_date, to_timestamp, date_format

# COMMAND ----------

# to_date()

df = df.withColumn("hire_date_converted", to_date("hire_date", "dd-MM-yyyy"))

df.display()

# COMMAND ----------

# to_timestamp()

df = df.withColumn("hire_timestamp_converted", to_timestamp("hire_date", "dd-MM-yyyy"))

df.display()

# COMMAND ----------

# date_format()

df.withColumn("year", date_format("hire_date_converted", "yyyy-MM")).display()

df.withColumn("month_year", date_format("hire_date_converted", "MMMM, yyyy")).display()