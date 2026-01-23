# Databricks notebook source
region_name = dbutils.widgets.get("region_name")

# COMMAND ----------

print(region_name)

# COMMAND ----------

spark.read.table("population_metrics.default.countries_consolidated").filter(f"region = '{region_name}'").display()