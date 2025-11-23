# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Grant and Revoke privileges using SQL](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Grant privileges

# COMMAND ----------

spark.sql("GRANT USE CATALOG ON CATALOG population_metrics TO `insert user principal name here`")

spark.sql("GRANT USE SCHEMA ON CATALOG population_metrics.default TO `insert user principal name here`")

spark.sql("GRANT SELECT ON CATALOG population_metrics.default.countries_consolidated TO `insert user principal name here")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Revoke privileges

# COMMAND ----------

spark.sql("REVOKE USE CATALOG ON CATALOG population_metrics FROM `insert user principal name here`")

spark.sql("REVOKE USE SCHEMA ON CATALOG population_metrics.default FROM `insert user principal name here`")

spark.sql("REVOKE SELECT ON CATALOG population_metrics.default.countries_consolidated FROM `insert user principal name here`")