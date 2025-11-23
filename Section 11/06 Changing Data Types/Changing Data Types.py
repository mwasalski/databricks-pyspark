# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [cast()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Column.cast.html)
# MAGIC - [Spark Data Types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_population")

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using cast()

# COMMAND ----------

from pyspark.sql.functions import col

from pyspark.sql.types import StringType

# COMMAND ----------

# df_1: uses the actual Spark StringType() class (an object instance) to cast columns explicitly

df_1 = df.select(
            col("country_id").cast(StringType()),
            col("name"),
            col("nationality"),
            col("country_code"),
            col("iso_alpha2"),
            col("capital"),
            col("population").cast(StringType()),
            col("area_km2").cast(StringType()),
            col("region_id").cast(StringType()),
            col("sub_region_id").cast(StringType())
        )

df_1.dtypes

# COMMAND ----------

# df_2: uses the shorthand literal "string", which Spark internally maps to the same StringType() object

df_2 = df.select(
            col("country_id").cast("string"),
            col("name"),
            col("nationality"),
            col("country_code"),
            col("iso_alpha2"),
            col("capital"),
            col("population").cast("string"),
            col("area_km2").cast("string"),
            col("region_id").cast("string"),
            col("sub_region_id").cast("string")
        )

df_2.dtypes

# COMMAND ----------

# df_3: cast multiple columns to StringType in-place using withColumns and a mapping of column names to cast expressions

df_3 = df.withColumns(
                        {
                            "country_id": col("country_id").cast(StringType()), 
                            "population": col("population").cast(StringType()),
                            "area_km2": col("area_km2").cast(StringType()),
                            "region_id": col("region_id").cast(StringType()),
                            "sub_region_id": col("sub_region_id").cast(StringType())
                        }
                     )
                     
df_3.dtypes