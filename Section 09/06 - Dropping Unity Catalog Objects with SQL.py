# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [DROP CATALOG](https://learn.microsoft.com/bs-latn-ba/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-drop-catalog)
# MAGIC - [DROP SCHEMA](https://learn.microsoft.com/bs-latn-ba/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-drop-schema)
# MAGIC - [DROP VOLUME](https://learn.microsoft.com/bs-latn-ba/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-drop-volume)
# MAGIC - [DROP TABLE](https://learn.microsoft.com/bs-latn-ba/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-drop-table)
# MAGIC - [DROP VIEW](https://learn.microsoft.com/bs-latn-ba/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-drop-view)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Syntax

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Dropping a catalog
# MAGIC
# MAGIC DROP CATALOG [ IF EXISTS ] catalog_name [ RESTRICT | CASCADE ]

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Dropping a schema
# MAGIC
# MAGIC DROP SCHEMA [ IF EXISTS ] schema_name [ RESTRICT | CASCADE ]

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Dropping a Volume
# MAGIC
# MAGIC DROP VOLUME [ IF EXISTS ] volume_name
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Dropping a Table
# MAGIC
# MAGIC DROP TABLE [ IF EXISTS ] table_name

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Dropping a View
# MAGIC
# MAGIC DROP VIEW [ IF EXISTS ] view_name