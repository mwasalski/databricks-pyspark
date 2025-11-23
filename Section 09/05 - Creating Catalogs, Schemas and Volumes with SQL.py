# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [CREATE CATALOG](https://learn.microsoft.com/en-us/azure/databricks/schemas/create-catalog)
# MAGIC - [CREATE SCHEMA](https://learn.microsoft.com/en-us/azure/databricks/schemas/create-schema)
# MAGIC - [CREATE VOLUME](https://learn.microsoft.com/en-us/azure/databricks/schemas/create-volume)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Syntax

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Creating a Catalog
# MAGIC -- Managed Location is mandatory if a storage root URL has not been configured for the Metastore
# MAGIC
# MAGIC CREATE CATALOG [ IF NOT EXISTS ] <catalog-name>
# MAGIC    [ MANAGED LOCATION '<location-path>' ]
# MAGIC    [ COMMENT <comment> ];

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Creating a Schema
# MAGIC
# MAGIC CREATE { DATABASE | SCHEMA } [ IF NOT EXISTS ] <catalog-name>.<schema-name>
# MAGIC     [ MANAGED LOCATION '<location-path>' | LOCATION '<location-path>']
# MAGIC     [ COMMENT <comment> ]
# MAGIC     [ WITH DBPROPERTIES ( <property-key = property_value [ , ... ]> ) ];

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Creating a Volume
# MAGIC
# MAGIC CREATE VOLUME <catalog>.<schema>.<volume-name>
# MAGIC LOCATAION '<location-path>' 