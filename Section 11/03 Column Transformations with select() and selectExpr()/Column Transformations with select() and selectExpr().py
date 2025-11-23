# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [select()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.select.html)
# MAGIC - [selectExpr()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.selectExpr.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 select()

# COMMAND ----------

df.select("country_id", "name", "population").display()

# COMMAND ----------

from pyspark.sql.functions import col, upper

# You can perform various methods and functions on the columns
df.select(
    col("country_id"), 
    upper("name").alias("country_name"), 
    col("population"),
    col("area_km2"),
    (col("population")/col("area_km2")).alias("population_density") 
    ).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 selectExpr()

# COMMAND ----------

# selectExpr allows you to use SQL expressions

df.selectExpr(
    "country_id", 
    "upper(name) as country_name",
    "population",
    "area_km2",
    "(population/area_km2) as population_density"    
).display()