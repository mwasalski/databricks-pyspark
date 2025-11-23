# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Liquid Clustering](https://learn.microsoft.com/en-us/azure/databricks/delta/clustering)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Liquid Clustering Demo

# COMMAND ----------

# Creating a large DataFrame to test liquid clustering
# Uses the sample orders data from tpch schema

df = spark.read.table("samples.tpch.orders")

df = df.union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df).union(df)

df.count()

# COMMAND ----------

# WITHOUT LIQUID CLUSTERING
df.write.format("delta").save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders")

# COMMAND ----------

# WITH LIQUID CLUSTERING
# Clustering on the o_orderdate column
df.write.format("delta").clusterBy("o_orderdate").save("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders_lq")

# COMMAND ----------

# Reading in both datasets (clustered and non-clustered)

# df1 is not clustered
# df2 is clustered

df1 = spark.read.format("delta").load("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders")

df2 = spark.read.format("delta").load("/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders_lq")

# COMMAND ----------

# If you examine the query stats then this query does not benefit from liquid clustering
# It does not skip any files
df1.filter("o_orderdate > '1998-01-01'").display()

# COMMAND ----------

# This query benefits from liquid clustering and is quicker
# It prunes the majority of files
df2.filter("o_orderdate > '1998-01-01'").display()

# COMMAND ----------

# You can run the optimize command to manually trigger clustering
spark.sql("optimize delta.`/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders_lq`")