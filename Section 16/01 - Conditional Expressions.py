# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [expr()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.expr.html)
# MAGIC - [when()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.when.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading data into a Spark DataFrame

# COMMAND ----------

df = spark.read.table("population_metrics.default.countries_consolidated")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Case Statement in SQL string

# COMMAND ----------

from pyspark.sql.functions import expr, when

# COMMAND ----------

sql_string = """
case 
    when population > 300000000 then 'High' 
    when population > 30000000 then 'Medium' 
    else 'Small' 
end
"""

# COMMAND ----------

# You can use the SQL string in the withColumn method via the expr() function
# The expr() function parses the expression string into the column that it represents

df.withColumn("population_class", expr(sql_string)).display()

# COMMAND ----------

# You can use the SQL string in the select method via the expr() function

df.select("country", 
          "region", 
          "sub_region", 
          "population", 
          "area_km2", 
          expr(sql_string).alias("population_class")).\
display()

# COMMAND ----------

# selectExpr can take SQL strings without requiring the expr() function

df.selectExpr("country", 
          "region", 
          "sub_region", 
          "population", 
          "area_km2", 
          "case when population > 300000000 then 'High' when population > 30000000 then 'Medium' else 'Small' end as population_class").\
display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Conditional Expression using PySpark functions

# COMMAND ----------

df.withColumn(
    "population_class", 
    when(df.population > 300000000, 'High').\
    when(df.population > 30000000, 'Medium').\
    otherwise('Small')).\
    display()