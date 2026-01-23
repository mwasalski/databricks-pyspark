# Databricks notebook source
# MAGIC %md
# MAGIC ### 📌 Lazy Evaluation

# COMMAND ----------

# MAGIC %md
# MAGIC All transformations in Spark are lazy, in that they do not compute their results right away. Instead, they just remember the transformations applied to some base dataset (e.g. a file). The transformations are only computed when an action requires a result to be returned to the driver program. 
# MAGIC
# MAGIC - `Transformations` are methods on a DataFrame which returns another DataFrame or Data Object.
# MAGIC
# MAGIC - `Actions` are methods on a DataFrame which returns a value or writes it to External Storage.
# MAGIC
# MAGIC Lazy Evaluation means that when you call a transformation on a DataFrame Spark doesn’t immediately read data or run that operation. Instead it just records the transformation in a plan. Only when you invoke an action does Spark actually go out and load data, apply every transformation in one go, and produce results.
# MAGIC
# MAGIC

# COMMAND ----------

# Since we're only performing transformations this code cell will not trigger an execution

df = spark.read.table("population_metrics.default.countries_consolidated").\
     groupBy("region").\
     sum("population")

# COMMAND ----------

# display() is an action and will trigger the execution.

df.display()