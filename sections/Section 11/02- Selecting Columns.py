# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [select()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.select.html)
# MAGIC - [col()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.col.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using select() with String Column Names

# COMMAND ----------

df.select("country_id", "name", "population").display()

# COMMAND ----------

df.select("*").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using select() with Bracket Notation

# COMMAND ----------

df.select(df['country_id'], df['name'], df['population']).display()

# COMMAND ----------

# You can chain additional methods and transformations on to column objects

df.select(df['country_id'].alias("id"), df['name'].alias("country_name"), df['population']).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using select() with DataFrame Attribute Access

# COMMAND ----------

df.select(df.country_id, df.name, df.population).display()

# COMMAND ----------

# You can chain additional methods and transformations on to column objects

df.select(df.country_id.alias("id"), df.name.alias("country_name"), df.population).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using select() with col()

# COMMAND ----------

# col must be imported
from pyspark.sql.functions import col

# COMMAND ----------

df.select(col('country_id'), col('name'), col('population')).display()

# COMMAND ----------

# You can chain additional methods and transformations on to column objects

df.select(col('country_id').alias("id"), col('name').alias("country_name"), col('population')).display()