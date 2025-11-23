# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Conditional Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#conditional-functions)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a Spark DataFrame

# COMMAND ----------

# Sample data: (id, name, nickname, age)
data = [
    (1,    "Alice",    None,     23),
    (2,    None,       "Ally",   25),
    (3,    None,       None,     31),
    (4,    "Bob",      "Bobby",  30),
]

schema = ["id", "name", "nickname", "age"]
df = spark.createDataFrame(data, schema)

# Show results
df.display()

# COMMAND ----------

from pyspark.sql.functions import coalesce, lit

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 coalesce

# COMMAND ----------

df.select(
    "id",
    "name",
    "nickname",
    "age",
    coalesce("name","nickname", lit("No name provided")).alias("age_filled")
).display()