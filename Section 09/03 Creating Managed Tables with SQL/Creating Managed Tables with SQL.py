# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Spark SQL Reference](https://spark.apache.org/docs/latest/sql-ref.html)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Creating an empty Managed Table
# MAGIC CREATE TABLE population_metrics.default.countries_population_2
# MAGIC (
# MAGIC   country_id integer, 
# MAGIC   name string, 
# MAGIC   nationality string, 
# MAGIC   country_code string, 
# MAGIC   iso_alpha2 string, 
# MAGIC   capital string, 
# MAGIC   population integer, 
# MAGIC   area_km2 integer, 
# MAGIC   region_id integer, 
# MAGIC   sub_region_id integer
# MAGIC  )

# COMMAND ----------

# Returning the newly created managed table as a DataFrame

df = spark.sql("select * from population_metrics.default.countries_population_2")

df.display()

# COMMAND ----------

# Inserting records into the table from the countries_population table

df = spark.sql("select * from population_metrics.default.countries_population")

df.write.mode("append").saveAsTable("select * from population_metrics.default.countries_population_2")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- CREATE TABLE AS Statement can create a table from a query result
# MAGIC
# MAGIC CREATE TABLE population_metrics.default.countries_population_3
# MAGIC AS SELECT * FROM population_metrics.default.countries_population_2