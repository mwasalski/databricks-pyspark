# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [groupBy()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.groupBy.html)
# MAGIC - [Aggregate Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#aggregate-functions)

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

# Applying the groupBy method returns a GroupedData object
type(df.groupBy("region"))

# COMMAND ----------

from pyspark.sql.functions import sum, avg

# COMMAND ----------

# Grouping by region and summing the population
df.groupBy("region").sum("population").display()

# COMMAND ----------

# You can perform multiple aggregations with the .agg() method
# Grouping by region and calculating the total and average population
df.groupBy("region").agg(
                            sum("population"),
                            avg("population")      
                           ).display()

# COMMAND ----------

# Aliasing the aggregated columns
df.groupBy("region").agg(
                            sum("population").alias("total_population"),
                            avg("population").alias("avg_population")      
                           ).display()

# COMMAND ----------

# Grouping by multiple columns
df.groupBy("region", "sub_region").agg(
                            sum("population").alias("total_population"),
                            avg("population").alias("avg_population")      
                           ).display()