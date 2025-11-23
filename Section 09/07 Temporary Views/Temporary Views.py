# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [createOrReplaceTempView()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createOrReplaceTempView.html)
# MAGIC - [createOrReplaceGlobalTempView()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createOrReplaceGlobalTempView.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Local Temporary View
# MAGIC Local temporary views are visible only to the session that created them and are dropped when the session ends.

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

df.createOrReplaceTempView("_sql_df")

# COMMAND ----------

spark.sql("select * from _sql_df").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Global Temporary View
# MAGIC To create a global temporary view you use the createGlobalTempView or createOrReplaceGlobalTempView method on the dataframe and give the view a name.
# MAGIC

# COMMAND ----------

df.createOrReplaceGlobalTempView("_sql_gdf")

# COMMAND ----------

spark.sql("select * from global_temp._sql_gdf")

# COMMAND ----------

# run in other notebook
spark.sql("select * from global_temp._sql_gdf")