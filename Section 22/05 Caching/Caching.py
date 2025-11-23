# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Optimize performance with caching on Azure Databricks](https://learn.microsoft.com/en-gb/azure/databricks/optimizations/disk-cache)
# MAGIC - [persist()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.persist.html)
# MAGIC - [unpersist()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unpersist.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Disk Cache

# COMMAND ----------

# The first time you read data it will be cached
# If you check the performance metrics for this query then 0% bytes have been read from the cache

df = spark.read.table("population_metrics.default.countries_consolidated")

df.display()

# COMMAND ----------

# If you read data from the cached table again then 100% bytes have been read from the cache
# The query will be faster

df = spark.read.table("population_metrics.default.countries_consolidated")

df.display()

# COMMAND ----------

# On all-purpose or job compute clusters you can disable the cache
spark.conf.set("spark.databricks.io.cache.enabled", "false")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Spark Cache

# COMMAND ----------

# The cache() and persist() methods will add the DataFrame to the Spark cache
df.cache()
df.persist()

# COMMAND ----------

# The unpersist() method will evict the DataFrame from the Spark cache
df.unpersist()