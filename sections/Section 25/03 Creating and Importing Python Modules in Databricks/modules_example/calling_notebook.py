# Databricks notebook source
from utils.metadata import add_processed_timestamp
from utils.col_transformers import divide_cols

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated")

# COMMAND ----------

add_processed_timestamp(df).display()

# COMMAND ----------

df.withColumn("density_km2", divide_cols(df.population, df.area_km2)).display()