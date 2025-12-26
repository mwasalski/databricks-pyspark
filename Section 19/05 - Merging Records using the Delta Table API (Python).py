# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Upsert into a table using merge](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Merging Records using the Delta Table API

# COMMAND ----------

# Target Delta Table instance

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "population_metrics.default.country_regions")

# COMMAND ----------

# You can convert a DeltaTable instance to a DataFrame with toDF()
# This enables you to display the contents
# This is an alternative to the DataFrameReader API (spark.read.format("delta").load(...))

dt.toDF().display()

# COMMAND ----------

# Deleting the record with id = 100 before proceeding

dt.delete("id = 100")

# COMMAND ----------

# The source DataFrame

df = spark.read.\
        format("csv").\
        option("header", True).\
        schema("id int, name string").\
        load("/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/country_regions/")

df.display()

# COMMAND ----------

# Begin a merge operation on the target Delta table (aliased as "target")
dt.alias("target").\
    merge(
        df.alias("source"), # Merge with the source DataFrame (aliased as "source") based on matching 'id'
        "target.id = source.id"
    ).\
    whenMatchedUpdate(
        set = {
            "target.name": "source.name" # If a match is found on 'id', update the 'name' column in the target with the source value
        }
    ).\
    whenNotMatchedInsert( # If no match is found, insert a new row into the target with values from the source
        values = {
            "target.id": "source.id", 
            "target.name": "source.name"
        }
    ).execute()  # Execute the merge operation

# COMMAND ----------

# After the merge you should be able to see the 'upserted' records
dt.toDF().display()

# COMMAND ----------

# Alternative syntax, more concise
# When a match is found, update all columns in the target with values from the source
# When no match is found, insert all columns from the source into the target
dt.alias("target").\ # Merge with the source DataFrame (aliased as "source") on the 'id' column
    merge(
        df.alias("source"),
        "target.id = source.id"
    ).\
    whenMatchedUpdateAll().\ 
    whenNotMatchedInsertAll().\
    execute()