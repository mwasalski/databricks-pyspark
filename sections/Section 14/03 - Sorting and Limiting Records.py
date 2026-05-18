# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [sort()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.sort.html)
# MAGIC - [limit()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.limit.html)

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

# sort on population (ascending by default)

df.sort("population").display()

# COMMAND ----------

# sort on population descending

df.sort("population", ascending=False).display()

# COMMAND ----------

# sort on population and limit to top 10 records

df.sort("population", ascending=False).limit(10).display()

# COMMAND ----------

# sort on region and population (both descending)

df.sort("region", "population", ascending=False).display()

# COMMAND ----------

# sort on regsion ascending and population descending 

df.sort(df.region.asc(), df.population.desc()).display()

# COMMAND ----------

# orderBy is an alias for sort

df.orderBy(df.region.asc(), df.population.desc()).display()