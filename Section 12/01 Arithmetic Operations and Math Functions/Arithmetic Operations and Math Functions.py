# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Mathematical Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#mathematical-functions)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Module Imports

# COMMAND ----------

from pyspark.sql.functions import col, round, greatest, least

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Basic Arithmetic Expressions

# COMMAND ----------

df = df.withColumn("population_forecast_2030", col("population")*1.2)

df.display()

# COMMAND ----------

df = df.withColumn("population_density", col("population")/col("area_km2"))

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

# round()
df = df.withColumn("population_forecast_2030", round(col("population")*1.2,1))

df.display()

# COMMAND ----------

# round()
df = df.withColumn("population_density", round(col("population")/col("area_km2"), 1))

df.display()

# COMMAND ----------

# greatest() and least()
df.select(
    "name",
    "population",
    col("population_forecast_2030"),
    least("population", "population_forecast_2030").alias("lower_of_pop_and_forecast_pop"),
    greatest("population", "population_forecast_2030").alias("greater_of_pop_and_forecast_pop")
).display()