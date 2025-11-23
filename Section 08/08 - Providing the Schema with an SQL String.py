# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [schema](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.schema.html)
# MAGIC - [Spark Data Types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Providing the Schema via SQL DDL

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

# COMMAND ----------

# SQL schema as a DDL string

schema = "country_id int, name string, nationality string, country_code string, iso_alpha2 string, capital string, population int, area_km2 int, region_id int, sub_region_id int"

# COMMAND ----------

# SQL schema as a multi-line DDL string

schema = """
        country_id int, 
        name string, 
        nationality string, 
        country_code string, 
        iso_alpha2 string, 
        capital string, 
        population int, 
        area_km2 int, 
        region_id int, 
        sub_region_id int
        """

# COMMAND ----------

df = spark.read.format("csv").schema(schema).options(header=True).load(path)