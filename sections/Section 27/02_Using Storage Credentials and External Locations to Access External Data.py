# Databricks notebook source
# Provide your specific URI [abfss] path here

path = "abfss://[your container name]@[your storage account name].dfs.core.windows.net/population_data/countries_population.parquet"

# COMMAND ----------

# MAGIC %md
# MAGIC The below code cell will not work unless you have created a **Storage Credential** and **External Location** in Unity Catalog for the Azure Data Lake Storage Gen2 Container specified in the path above.
# MAGIC
# MAGIC The Access Connector used to create the Storage Credential should also be granted **Storage Blob Data Contributor** Access to the Storage Account Container

# COMMAND ----------

spark.read.format("parquet").load(path)