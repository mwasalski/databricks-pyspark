# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [withColumn()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumn.html)
# MAGIC - [withColumns()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumns.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 withColumn()

# COMMAND ----------

from pyspark.sql.functions import upper

# withColumn adds single columns or replaces the existing column with the same name
# withColumn -> Returns a new DataFrame by adding a column or replacing the existing column that has the same name.
df.withColumn("country_name", upper("name")).\
  withColumn("population_density", df.population / df.area_km2).\
  select("coutry_name", "population", "area_km2","population_density").\
  display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### It's often more efficient to use a single select() method.
# MAGIC
# MAGIC Chaining withColumn() and select() result in multiple DataFrames

# COMMAND ----------

df.select(
      df.name.alias("country_name"), 
      df.population, 
      df.area_km2,
      (df.population / df.area_km2).alias("population_density").\
  display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 withColumns()

# COMMAND ----------

# withColumns adds multiple columns or replaces the existing columns that have the same names

df.withColumns(
  {
    "country_name": upper("name"), 
    "population_density": df.population / df.area_km2
    }
  ).display()