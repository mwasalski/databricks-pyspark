# Databricks notebook source
# MAGIC %md
# MAGIC ### 📌 SCD Type 2 Demo

# COMMAND ----------

# MAGIC %md
# MAGIC #### Creating an Empty SCD 2 Table

# COMMAND ----------

spark.sql(
    """
    CREATE TABLE population_metrics.default.country_regions_scd_2
    (
        id int,
        name string,
        effective_date timestamp,
        end_date timestamp
    )
    """
)

# COMMAND ----------

spark.read.table("population_metrics.default.country_regions_scd_2").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Loading the initial country_regions data to the SCD 2 table

# COMMAND ----------

df_changes = spark.read.\
                  format("csv").\
                  option("header", True).\
                  schema("id int, name string").\
                  load("/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/country_regions/")

df_changes.display()

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql.functions import lit, current_timestamp
from pyspark.sql.types import TimestampType, IntegerType, StringType

# Load the SCD2 Delta table
dt = DeltaTable.forName(spark, "population_metrics.default.country_regions_scd_2")

# Step 1: Expire current active rows
# - Match on id where end_date IS NULL (only current versions)
# - Update end_date to current timestamp to “close out” the old record
dt.alias("t").\
    merge(
        source    = df_changes.alias("s"),
        condition = "t.id = s.id AND t.end_date IS NULL"
    ).\
    whenMatchedUpdate(
        set = { "t.end_date": current_timestamp() }
    ).\
    execute()

# Step 2: Append new version rows
# - Stamp each row with effective_date = now
# - Set end_date = NULL to mark it as the active version
df_changes = df_changes.\
    withColumn("effective_date", current_timestamp()).\
    withColumn("end_date", lit(None).cast(TimestampType())).\
    select(
        df_changes.id.cast(IntegerType()),
        df_changes.name.cast(StringType()),
        "effective_date",
        "end_date"
    ).\
    write.\
    mode("append").\
    saveAsTable("population_metrics.default.country_regions_scd_2")

# COMMAND ----------

spark.read.table("population_metrics.default.country_regions_scd_2").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Changing attributes
# MAGIC
# MAGIC Run these cells and then re-run the Type 2 upsert operation to see how they get inserted into the SCD 2 Table

# COMMAND ----------

data = [{
    "id": 10,
    "name": "United States"
}]

df_changes = spark.createDataFrame(data)

df_changes.display()

# COMMAND ----------

data = [{
    "id": 10,
    "name": "USA"
}]

df_changes = spark.createDataFrame(data)

df_changes.display()

# COMMAND ----------

data = [{
    "id": 11,
    "name": "New"
}]

df_changes = spark.createDataFrame(data)

df_changes.display()