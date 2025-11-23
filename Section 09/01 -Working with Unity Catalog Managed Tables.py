# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [saveAsTable()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.saveAsTable.html)
# MAGIC - [table()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.table.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

schema = StructType(
                [
                    StructField("country_id", IntegerType(), False),
                    StructField("name", StringType(), True),
                    StructField("nationality", StringType(), True),
                    StructField("country_code", StringType(), True),
                    StructField("iso_alpha2", StringType(), True),
                    StructField("capital", StringType(), True),
                    StructField("population", IntegerType(), True),
                    StructField("area_km2", IntegerType(), True),
                    StructField("region_id", IntegerType(), True),
                    StructField("sub_region_id", IntegerType(), True)                   
                ]
            )

df = spark.read.format("csv").schema(schema).options(header=True).load(path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Saving the contents of a DataFrame as a Managed Table

# COMMAND ----------

# By default when using the saveAsTable method a Managed Delta table is created
df.write.saveAsTable("population_metrics.default.countries_population")

# COMMAND ----------

# You can specify the mode as "append" or "overwrite"
df.write.mode("append").saveAsTable("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading a Managed Table into a DataFrame

# COMMAND ----------

# The table() method on the Spark DataFrameReader object can be used to read a table into a DataFrame
df = spark.read.table("population_metrics.default.countries_population")

df.display()