# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [write](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.write.html)
# MAGIC - [csv()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.csv.html)
# MAGIC - [save()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.save.html)
# MAGIC - [mode](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.mode.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame
# MAGIC This DataFrame will be written as a CSV output

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

df = spark.read.format("csv").options(header=True).load(path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using the csv() method

# COMMAND ----------

output_path = "/Volumes/population_metrics/landing/datasets/output_datasets/csv/countries_population"

# COMMAND ----------

# This is a DataFrameWriter object, you can apply the csv or save methods to it
# pisząc tak dostaniemy po prostu info o obiekcie
df.write

# COMMAND ----------

# Writing the DataFrame to CSV
df.write.csv(output_path)

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ### 📌 Append vs Overwrite
# MAGIC
# MAGIC When the target directory already contains data, specify a write mode:
# MAGIC
# MAGIC - **overwrite**: delete existing files before writing the new output  
# MAGIC - **append**: keep existing files and add the new output alongside them
# MAGIC
# MAGIC Using **append** lets you incrementally add new data to the destination as it arrives.

# COMMAND ----------

# mode as append and header=True
# df.write to tworzeneie obiektu Writer
df.write.mode("append").options(header=True).csv(output_path)

# COMMAND ----------

# mode as overwrite and header=True
df.write.mode("overwrite").options(header=True).csv(output_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using the save() method

# COMMAND ----------

df.write.format("csv").mode("append").options(header=True).save(output_path)

# COMMAND ----------

# Changing the delimiter to the pipe symbol (|)
df.write.format("csv").mode("overwrite").options(header=True, sep="|").save(output_path)