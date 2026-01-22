# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 📌 Creating the **countries_population** table in Unity Catalog

# COMMAND ----------

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

df.write.mode("overwrite").saveAsTable("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating the **country_regions** table in Unity Catalog

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/country_regions/country_regions.csv"

schema = StructType(
                [
                    StructField("id", IntegerType(), False),
                    StructField("name", StringType(), True)          
                ]
            )

df = spark.read.format("csv").schema(schema).options(header=True).load(path)

df.write.mode("overwrite").saveAsTable("population_metrics.default.country_regions")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating the **country_sub_regions** table in Unity Catalog

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/country_sub_regions/country_sub_regions.csv"

schema = StructType(
                [
                    StructField("id", IntegerType(), False),
                    StructField("name", StringType(), True)          
                ]
            )

df = spark.read.format("csv").schema(schema).options(header=True).load(path)

df.write.mode("overwrite").saveAsTable("population_metrics.default.country_sub_regions")
