# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Managed Tables](https://learn.microsoft.com/en-us/azure/databricks/tables/managed)
# MAGIC - [External Tables](https://learn.microsoft.com/en-us/azure/databricks/tables/external)
# MAGIC - [catalog.createTable()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Catalog.createTable.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Pre-requisites
# MAGIC - Create your own Storage Account + Container
# MAGIC - Register the Container as an External Location (+ Create Storage Credential if required)
# MAGIC - Create a catalog called **test_catalog_1**

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Writing to an External Table

# COMMAND ----------

df = spark.read.table("samples.accuweather.historical_hourly_metric")

# COMMAND ----------

path = "your path here"

df.write.option("path", path).saveAsTable("test_catalog_1.default.historical_hourly_metric_ext")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Dropping an External Table

# COMMAND ----------

spark.sql("DROP TABLE test_catalog_1.default.historical_hourly_metric_ext")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Registering an External Table backed by existing data

# COMMAND ----------

spark.catalog.createTable(
    tableName = "test_catalog_1.default.historical_hourly_metric_ext",
    path = path,
    source = "delta"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 External tables can use the DELTA, CSV, JSON, AVRO, PARQUET, ORC and TEXT file formats

# COMMAND ----------

csv_path = "your path here"
df.write.option("path", csv_path).format("csv").saveAsTable("test_catalog_1.default.historical_hourly_metric_ext_csv")