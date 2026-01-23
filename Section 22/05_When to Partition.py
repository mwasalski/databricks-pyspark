# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Partitioning](https://www.databricks.com/discover/pages/optimize-data-workloads-guide#partitioning)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 When to Partition
# MAGIC - Partitioning can speed up your queries if you provide the partition column(s) as filters or join on partition column(s) or aggregate on partition column(s) or merge on partition column(s), as it will help Spark to skip a lot of unnecessary data partition (i.e., subfolders) during scan time.
# MAGIC - Databricks recommends not to partition tables under 1TB in size and let ingestion time clustering automatically take effect. This feature will cluster the data based on the order the data was ingested by default for all tables.
# MAGIC - You can partition by a column if you expect data in each partition to be at least 1GB
# MAGIC - Always choose a low cardinality column — for example, year, date — as a partition column
# MAGIC

# COMMAND ----------

# Partitioning during file write
df.write.mode("overwrite").format("delta").partitionBy("region").save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/countries_consolidated_partitioned")

# COMMAND ----------

# Partitioning during table write
df.write.partitionBy("region").saveAsTable("population_metrics.default.countries_consolidated_partitioned")

# COMMAND ----------

# Reading in the partitioned data
df1 = spark.read.format("delta").load("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/countries_consolidated_partitioned")

# COMMAND ----------

# While this leverages the partitioned column, the overhead associated does not make the overall performance much better
# Partitioning yields true benefits on tables > 1TB
df1.filter("region = 'America'").display()

# COMMAND ----------

# Querying the non partitioned column as a comparison, due to the small file size the performance is only marginally slower
df1.filter("sub_region = 'Northern America'").display()