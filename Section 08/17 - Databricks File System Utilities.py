# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Databricks File System Utilieis](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-utils#dbutils-fs)

# COMMAND ----------

# Documentation for dbutils

dbutils.help()

# COMMAND ----------

# Documentation for dbutils.fs

dbutils.fs.help()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Copying Files and Directories

# COMMAND ----------

# Documentation for dbutils.fs.cp

help(dbutils.fs.cp)

# COMMAND ----------

# Copying a file

dbutils.fs.cp(
    "/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population/part-00000-tid-849534417012172180-eabe33f8-3a8c-4fd7-9f4d-a964efcf2bd0-140-1-c000.csv",
    "/Volumes/population_metrics/landing/datasets/output_dataset"
)

# COMMAND ----------

# Copying a directory
# Must specify recurse=True

dbutils.fs.cp(
    "/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population/",
    "/Volumes/population_metrics/landing/datasets/output_dataset/countries_population_copy",
    recurse=True
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Deleting Files and Directories

# COMMAND ----------

# Documentation on dbutils.fs.rm

help(dbutils.fs.rm)

# COMMAND ----------

# Remove a file

dbutils.fs.rm("/Volumes/population_metrics/landing/datasets/output_dataset/part-00000-tid-849534417012172180-eabe33f8-3a8c-4fd7-9f4d-a964efcf2bd0-140-1-c000.csv")

# COMMAND ----------

# Remove a directory
# Must specify recurse=True

dbutils.fs.rm("/Volumes/population_metrics/landing/datasets/output_dataset/countries_population_copy/", recurse=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Listing the contents of a Directory

# COMMAND ----------

# Documentation on dbutils.fs.ls

help(dbutils.fs.ls)

# COMMAND ----------

# Displaying the contents of a directory

display(dbutils.fs.ls("dbfs:/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population/"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Displaying the contents of a File

# COMMAND ----------

# Displaying the contents of a file

dbutils.fs.head("dbfs:/Volumes/population_metrics/landing/datasets/output_dataset/csv/countries_population/part-00000-tid-849534417012172180-eabe33f8-3a8c-4fd7-9f4d-a964efcf2bd0-140-1-c000.csv")