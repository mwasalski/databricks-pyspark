# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [show()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.show.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

schema = StructType(
                [
                    StructField("country_id", IntegerType(), False),
                    StructField("name", StringType(), True),
                    StructField("nationality", StringType(), True),
                    StructField("country_code", StringType(), True),
                    StructField("iso_alpha2", StringType(), True),
                    StructField("capital", StringType(), True),
                    StructField("population", IntegerType(), True),
                    StructField("area_km2", IntegerType(), True),
                    StructField("region_id", IntegerType(), True),
                    StructField("sub_region_id", IntegerType(), True)                   
                ]
            )

df = spark.read.format("csv").schema(schema).options(header=True).load(path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 show()

# COMMAND ----------

df.show()

# COMMAND ----------

# By default values are truncated to 20 characters unless you specify truncate=False
df.show(truncate=False)

# COMMAND ----------

# By default only the top 20 rows are displayed, unless you specify the number of rows as an argument (n)
df.show(n=200)

# COMMAND ----------

# MAGIC %md
# MAGIC %md 
# MAGIC ### 📌 display()

# COMMAND ----------

# display() renders the DataFrame as an interactive HTML table
display(df)