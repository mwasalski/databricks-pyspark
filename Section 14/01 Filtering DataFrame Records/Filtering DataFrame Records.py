# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [filter()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.filter.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

# Using column instances to filter the DataFrame
df.filter(df.region == "Asia").display()


# COMMAND ----------

# This uses SQL expression-based filtering.
df.filter("region = 'Asia'").display()

# COMMAND ----------


# filtering on multiple conditions using the | operator
df.filter((df.region == "Asia") | (df.region == "Europe")).display()

# COMMAND ----------

# filtering on multiple conditions using the 'or' operator
df.filter("region = 'Asia' or region = 'Europe'").display

# COMMAND ----------

# filtering on multiple conditions using the & operator
df.filter((df.region == "Asia") & (df.country_name == "India")).display()

# COMMAND ----------

# filtering on multiple conditions using the and operator
df.filter("region = 'Asia' and country_name = 'India'").display()


# COMMAND ----------

# Using an expression to filter records (column instances)
df.where((df.population/df.area_km2) > 1000).display()

# COMMAND ----------

# Using an expression to filter records (SQL string)
df.where("(population/area_km2) > 1000").display()