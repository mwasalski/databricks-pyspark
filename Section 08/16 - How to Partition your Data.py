# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [partitionBy()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.partitionBy.html)

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

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Partitioning by a single column

# COMMAND ----------

# The partitionBy() method is used to partition your data
df.write.format("csv").partitionBy("region_id").save("/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population_partitioned")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Partitioning by multiple columns

# COMMAND ----------

# The order you specify the columns in the partitionBy() method will be the order of partitioning
df.write.format("csv").mode("overwrite").partitionBy("region_id", "sub_region_id").save("/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population_partitioned")