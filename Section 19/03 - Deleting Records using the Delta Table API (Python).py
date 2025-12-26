# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Delta Lake documentation - Deletes](https://docs.delta.io/latest/delta-update.html#delete-from-a-table)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Deleting Records using the Delta Table API

# COMMAND ----------

# Previewing the country_regions table

spark.read.table("population_metrics.default.country_regions").display()

# COMMAND ----------

# Creating a Delta Table instance 

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "population_metrics.default.country_regions")

# COMMAND ----------

# Deleting Records from the Delta Table where name = 'America'
dt.delete("name = 'America'")

# COMMAND ----------

# Confirming the record has been deleted

df = spark.read.table("population_metrics.default.country_regions")
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### The equivalent operation is not possible using the DataFrameWriter API
# MAGIC
# MAGIC To delete even a single record you need to overwrite the entire dataset.
# MAGIC
# MAGIC This full table rewrite can get expensive if you have a table with billions of rows.

# COMMAND ----------

df = spark.read.table("population_metrics.default.country_regions")

df = df.filter("name != 'Europe'")

# Use mode as overwrite to update the data, this is inefficient as it results in a full table rewrite
df.write.mode("overwrite").saveAsTable("population_metrics.default.country_regions")