# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC #### Reading Data:
# MAGIC - [json()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html)
# MAGIC - [load()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.load.html)
# MAGIC
# MAGIC #### Writing Data:
# MAGIC - [json()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html)
# MAGIC - [save()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.save.html)

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
# MAGIC ### 📌 Save the contents of a DataFrame in JSON Format

# COMMAND ----------

# Using the json method to write the DataFrame to json format
df.write.mode("overwrite").json("/Volumes/population_metrics/landing/datasets/output_dataset/json/countries_population")

# COMMAND ----------

# Using the save method to write the DataFrame to json format
df.write.format("json").mode("overwrite").save("/Volumes/population_metrics/landing/datasets/output_dataset/json/countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading JSON into a DataFrame

# COMMAND ----------

# Using the load method to read the DataFrame from json format, no schema provided
spark.read.format("json").load("/Volumes/population_metrics/landing/datasets/output_dataset/json/countries_population").display()

# COMMAND ----------

# Using the json method to read the DataFrame from json format, no schema provided
spark.read.json("/Volumes/population_metrics/landing/datasets/output_dataset/json/countries_population").display()

# COMMAND ----------

# The JSON reader tries to infer the data types from the content of the files. This can lead to different data types for the same column in different files. To avoid this, you can provide a schema

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

path = "/Volumes/population_metrics/landing/datasets/output_dataset/json/countries_population/"

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

df = spark.read.format("json").schema(schema).load(path)