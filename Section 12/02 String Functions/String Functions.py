# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [String Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#string-functions)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Examples

# COMMAND ----------

from pyspark.sql.functions import length, char_length, initcap, upper, lower, concat, concat_ws, lit

# COMMAND ----------

#length()

df.select(
    "name",
    length("name").alias("count_of_chars")
).display()

# COMMAND ----------

# char_length()

df.select(
    "name",
    char_length("name").alias("count_of_chars")
).display()

# COMMAND ----------

# upper() and lower()

df.select(
    "name",
    upper("name").alias("name_upper"),
    lower("name").alias("name_lower")
).display()

# COMMAND ----------

#lit()

df.select(
    "name",
    lit("hello")
).display()

# COMMAND ----------

# concat() and concat_ws()

df.select(
    "name",
    "capital"
    concat("capital", lit(", "), "name").alias("city_and_country"),
    concat_ws(", ", "name", "capital").alias("city_and_country_ws")
    ).display()