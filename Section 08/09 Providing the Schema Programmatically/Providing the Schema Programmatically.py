# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [schema](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.schema.html)
# MAGIC - [Spark Data Types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html)
# MAGIC - [Data Types API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/data_types.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Providing the Schema Programatically

# COMMAND ----------

path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

# COMMAND ----------

# Import the classes needed to define a Spark schema
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define a schema for our country dataset as a StructType (a list of StructField objects)
# każdy element listy jest obiektem sctruct field
# każde pole struct definiuje kolumnę
schema = StructType(
    [
        StructField("country_id", IntegerType(), False),   # country_id: integer column, cannot be null
        StructField("name", StringType(), True),           # name: string column, may contain nulls
        StructField("nationality", StringType(), True),    # nationality: string column, may contain nulls
        StructField("country_code", StringType(), True),   # country_code: string column, may contain nulls
        StructField("iso_alpha2", StringType(), True),     # iso_alpha2: 2-letter ISO code, may contain nulls
        StructField("capital", StringType(), True),        # capital: string column for capital city name
        StructField("population", IntegerType(), True),    # population: integer column, may contain nulls
        StructField("area_km2", IntegerType(), True),      # area_km2: integer column for area in km²
        StructField("region_id", IntegerType(), True),     # region_id: integer referencing region, may be null
        StructField("sub_region_id", IntegerType(), True)  # sub_region_id: integer referencing sub-region, may be null
    ]
)

# COMMAND ----------

df = spark.read.format("csv").schema(schema).options(header=True).load(path)