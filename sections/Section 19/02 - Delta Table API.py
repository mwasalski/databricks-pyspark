# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Delta Lake documentation](https://docs.delta.io/latest/index.html)
# MAGIC - [forPath](https://docs.delta.io/0.4.0/api/python/index.html#delta.tables.DeltaTable.forPath)
# MAGIC - [forName](https://docs.delta.io/0.7.0/api/python/index.html#delta.tables.DeltaTable.forName)
# MAGIC

# COMMAND ----------

# Importing the DeltaTable API

from delta.tables import DeltaTable

# COMMAND ----------

# Creating a DeltaTable instance using forName to reference a Unity Catalog Delta Table

dt1 = DeltaTable.forName(spark, "population_metrics.default.country_regions")

type(dt1)

# COMMAND ----------

# Creating a DeltaTable instance using forName to reference a Unity Catalog Delta File Path

dt2 = DeltaTable.forPath(spark, "/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/countries_population/")

type(dt2)