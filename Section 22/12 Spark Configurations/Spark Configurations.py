# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Spark Configurations](https://spark.apache.org/docs/latest/configuration.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 How to set Spark Configurations
# MAGIC
# MAGIC You can set your configurations in:
# MAGIC - Notebooks
# MAGIC - Clusters (Clusters -> Advanced -> Spark Configs)
# MAGIC - Jobs (to be discussed later)

# COMMAND ----------

# Notebook configs
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 104857600)
spark.conf.set("spark.databricks.io.cache.enabled", "false")

# COMMAND ----------

# Get all configs as a list of key-value pairs
spark.conf.getAll

# COMMAND ----------

# Get specified config value
spark.conf.get("spark.sql.ansi.enabled")