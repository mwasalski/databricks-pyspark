# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Broadcast Join](https://www.databricks.com/discover/pages/optimize-data-workloads-guide#broadcast-hash)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Turning off disk cache

# COMMAND ----------

spark.conf.set("spark.databricks.io.cache.enabled", "false")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data from the sample 'tpch' schema

# COMMAND ----------

spark.read.table("samples.tpch.customer").count()

# COMMAND ----------

spark.read.table("samples.tpch.customer").display()

# COMMAND ----------

spark.read.table("samples.tpch.nation").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Broadcast Join

# COMMAND ----------

df1 = spark.read.table("samples.tpch.customer")

# make the DataFrame relatively large
df1 = df1.union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1)

df2 = spark.read.table("samples.tpch.nation")

df3 = df1.join(df2, df1.c_nationkey == df2.n_nationkey, "inner")

# The explain plan should automatically include a broadcast join due to AQE
df3.explain("extended")

# COMMAND ----------

# This will leverage the broadcast join and should be relatively quicker vs the Data Shuffle
df3.write.mode("overwrite").saveAsTable("population_metrics.default.customer_nation_bc")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Disable Auto Broadcast Join
# MAGIC

# COMMAND ----------

spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1")

# COMMAND ----------

df1 = spark.read.table("samples.tpch.customer")

df1 = df1.union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1).union(df1)

df2 = spark.read.table("samples.tpch.nation")

df3 = df1.join(df2, df1.c_nationkey == df2.n_nationkey, "inner")

# The explain plan should include a Data Shuffle due to disabled broadcast join
df3.explain("extended")

# COMMAND ----------

# This will take longer due to the Data Shuffle
df3.write.mode("overwrite").saveAsTable("population_metrics.default.customer_nation_nbc")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Changing the Auto Broadcast threshold

# COMMAND ----------

# 100MB = 100 × 1024 × 1024 = 104,857,600 bytes
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "104857600")