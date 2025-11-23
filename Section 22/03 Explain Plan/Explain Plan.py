# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [explain()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.explain.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Printing the Explain Plan

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated").\
     groupBy("region").\
     sum("population")

# COMMAND ----------

# By default the mode is simple, only the physical plan is printed
df.explain()

# COMMAND ----------

# The mode can be set to 'formatted', this will print the physical plan in a more readable format
df.explain(mode = "formatted")

# COMMAND ----------

# Setting the mode to 'extended' will print the logical and physical plans
df.explain(mode="extended")