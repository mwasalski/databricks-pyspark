# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [pivot()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.GroupedData.pivot.html)
# MAGIC - [unpivot()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unpivot.html#pyspark.sql.DataFrame.unpivot)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 pivot()

# COMMAND ----------

# Aggregate population by sub-region into separate region columns
df_pivot = (
    df
    .groupBy("sub_region")   # group rows by each sub-region
    .pivot("region")         # turn each distinct region value into its own column
    .sum("population")       # compute the sum of population for each (sub_region, region) pair
)

df_pivot.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 unpivot()

# COMMAND ----------

# Take the df_pivot DataFrame and “melt” the specified continent columns
df_pivot.unpivot(
    "sub_region",                                            # column holding the IDs (grouping key)
    ["Africa", "America", "Asia", "Europe", "Oceania"],      # list of columns to unpivot (these become row values)
    "region",                                                # name for the new column that will hold the former column names
    "population"                                             # name for the new column that will hold the corresponding values
).display()                              