# Databricks notebook source
def function():
  resubable logic

# COMMAND ----------

# Defining a simple function
from pyspark.sql.functions import current_timestamp

def add_processed_timestamp(df):
    return df.withColumn("processed_timestamp", current_timestamp())

# COMMAND ----------

# Calling the function on a DataFrame
df = spark.read.table("population_metrics.default.countries_consolidated")

df = add_processed_timestamp(df)

df.display()

# COMMAND ----------

# Defining another simple function
from pyspark.sql.functions import round

def divide_cols(col1, col2):
    return round(col1 / col2, 2)

# COMMAND ----------

# Calling the function on the same DataFrame at the column level via the withColumn() method
df.withColumn("density_km2", divide_cols(df.population, df.area_km2)).display()

# COMMAND ----------

# Calling the function via the select() method
df.select("country_id", 
          "country", 
          "region", 
          "sub_region", 
          "population", 
          "area_km2", 
          "processed_timestamp",
          divide_cols(df.population, df.area_km2).alias("density_km2")).\
          display()