# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Delta Lake documentation - Updates](https://docs.delta.io/latest/delta-update.html#update-a-table)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Updating Records using the Delta Table API

# COMMAND ----------

# Previewing the country_regions table

spark.read.table("population_metrics.default.country_regions").display()

# COMMAND ----------

# Updating the records where name = 'Asia'
# When the condition is true the id column should contain the value 100 and the name column values should be in uppercase

from delta.tables import DeltaTable
from pyspark.sql.functions import lit, upper

dt = DeltaTable.forName(spark, "population_metrics.default.country_regions")

dt.update(
    condition = "name = 'Asia'",
    set = {
        "id": lit(100),
        "name": upper("name")
    }
)

# COMMAND ----------

# Updating all conditions by specifying the condition = None
# Updating the name column values to be in uppercase

dt.update(
    condition = None,
    set = {
        "name": upper("name")
    }
)