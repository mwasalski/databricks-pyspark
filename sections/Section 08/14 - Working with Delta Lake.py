# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC #### Reading Data:
# MAGIC - [load()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.load.html)
# MAGIC
# MAGIC #### Writing Data:
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
# MAGIC ### 📌 Save the contents of a DataFrame in Delta Lake Format

# COMMAND ----------

# Using the save method to write the DataFrame to Delta Lake format
df.write.format("delta").mode("overwrite").save("/Volumes/population_metrics/landing/datasets/output_dataset/delta/countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading Parquet into a DataFrame

# COMMAND ----------

# Using the load method to read the DataFrame from Delta Lake format
spark.read.format("delta").load("/Volumes/population_metrics/landing/datasets/output_dataset/delta/countries_population").display()