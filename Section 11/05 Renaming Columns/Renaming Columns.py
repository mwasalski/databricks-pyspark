# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [alias()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Column.alias.html)
# MAGIC - [withColumnRenamed()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumnRenamed.html)
# MAGIC - [withColumnsRenamed()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumnsRenamed.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Renaming columns with alias()

# COMMAND ----------

df.select(df.country_id.alias("id"), df.name.alias("country_name"), "population", "area_km2").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Renaming columns with withColumnRenamed()

# COMMAND ----------

df.withColumnRenamed("country_id", "id").withColumnRenamed("name", "country_name").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Renaming columns with withColumnsRenamed()

# COMMAND ----------

df.withColumnsRenamed({"country_id": "id","name": "country_name"}).display()