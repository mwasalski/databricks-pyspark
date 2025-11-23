# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [What is a view?](https://learn.microsoft.com/en-us/azure/databricks/views/)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Creating a View
# MAGIC `CREATE VIEW <catalog-name>.<schema-name>.<view-name> AS
# MAGIC SELECT <query>;`

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Creating a demo view
# MAGIC
# MAGIC CREATE VIEW population_metrics.default.top_10_countries_population AS
# MAGIC SELECT * FROM population_metrics.default.countries_population ORDER BY population DESC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Querying a View

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Querying the view using SQL
# MAGIC
# MAGIC SELECT * FROM population_metrics.default.top_10_countries_population

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Returning the view as a DataFrame

# COMMAND ----------

# Returning the view as a DataFrame object via the spark.sql() method

spark.sql("SELECT * FROM population_metrics.default.top_10_countries_population").display()

# COMMAND ----------

# Returning the view as a DataFrame object via the table() method

spark.read.table("population_metrics.default.top_10_countries_population").display()