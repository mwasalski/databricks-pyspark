# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Enable Schema Evolution](https://learn.microsoft.com/en-us/azure/databricks/delta/update-schema#enable-schema-evo)
# MAGIC - [withSchemaEvolution() for Delta Lake Merges](https://docs.delta.io/3.2.0/api/java/spark/io/delta/tables/DeltaMergeBuilder.html#withSchemaEvolution--)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 mergeSchema()

# COMMAND ----------

# This is the target table

spark.read.table("population_metrics.default.country_sub_regions").display()

# COMMAND ----------

# This is the source DataFrame

from pyspark.sql.functions import *
from pyspark.sql.types import *

df = spark.createDataFrame([
    {"id": 100, "name": "New Sub Region", "new_col": "Some new value"}
])

df = df.select(col("id").cast(IntegerType()), col("name").cast(StringType()), col("new_col").cast(StringType()))

df.display()


# COMMAND ----------

# Unless you explicitly specify the mergeSchema option as True, the write operation will result in a schema mismatch as the source DataFrame contains additional columns that are not present in the target table

df.write.format("delta").option("mergeSchema", True).mode("append").saveAsTable("population_metrics.default.country_sub_regions")

# COMMAND ----------

# Restoring the country_sub_regions table to prior state

spark.sql("DESCRIBE HISTORY population_metrics.default.country_sub_regions").display()
spark.sql("RESTORE population_metrics.default.country_sub_regions VERSION AS OF 0")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 withSchemaEvolution() for Delta Table merges

# COMMAND ----------

# This is boilerplate code

from delta.tables import *

(targetTable
  .merge(sourceDF, "source.key = target.key")
  .withSchemaEvolution() # <- This allows the schema of the target table/columns to be automatically updated based on the schema of the source table/columns. 
  .whenMatchedUpdateAll()
  .whenNotMatchedInsertAll()
  .whenNotMatchedBySourceDelete()
  .execute()
)