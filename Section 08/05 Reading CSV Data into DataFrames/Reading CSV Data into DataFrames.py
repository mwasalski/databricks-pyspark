# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [DataFrameReader](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.read.html)
# MAGIC - [csv()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.csv.html)
# MAGIC - [load()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.load.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using the csv() method

# COMMAND ----------

# Path to the single CSV file containing country population data
path = "/Volumes/population_metrics/landing/datasets/countries_dataset/csv_data/countries_population/countries_population.csv"

# COMMAND ----------

path

# COMMAND ----------

# This is a DataFrameReader Object
type(spark.read)

# COMMAND ----------

# Load the CSV file from the specified path into a Spark DataFrame
countries_population_df = spark.read.csv(path = path)

# COMMAND ----------

# This is a DataFrame object
type(spark.read.csv(path = path))

# COMMAND ----------

# The display function renders the DataFrame loaded from the CSV path as an interactive table within the notebook.
display(countries_population_df)

# COMMAND ----------

# display() can also be used as a method and chained onto the DataFrame object

countries_population_df.display()

# COMMAND ----------

# Passing the path as a positional argument instead of using the 'path=' keyword
# spark.read.csv(path).display()

# COMMAND ----------


# Storing the resulting DataFrame into a variable 'df'
# df = spark.read.csv(path)

# COMMAND ----------

# Confirming 'df' is a DataFrame object
type(countries_population_df)

# COMMAND ----------

# Rendering the DataFrame as an interactive table
countries_population_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC #### Providing additional options

# COMMAND ----------

# We can provide additional arguments
# We can specify header=True so that the first row gets read in as a header row
# Since header is out of position, we need to provide it as a keyword argument 'header='

df = spark.read.csv(path, header=True)

df.display()

# COMMAND ----------

# Specifying sep=';' on a comma-delimited CSV will mis-parse the file (default delimiter is comma)

df = spark.read.csv(path, header=True, sep=";")

df.display()

# COMMAND ----------

# Specifying sep=',' is redundant as the seperator is ',' by default

df = spark.read.csv(path, header=True, sep=",")

df.display()

# COMMAND ----------

# Using the option method to provide the same header argument as above

df = spark.read.option("header", True).csv(path)

df.display()

# COMMAND ----------

# Using the multiple option methods chained together

df = spark.read.option("header", True).option("sep", ",").csv(path)

df.display()

# COMMAND ----------

# The options method can be used to provide multiple options

df = spark.read.options(header=True, sep=",").csv(path)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ### 📌 Using the load() method

# COMMAND ----------

# The load method can be used generically, pick any data source ("csv", "parquet", "json", etc.) then call .load()
# The path and format are required

df = spark.read.load(path, format="csv", header=True)

df.display()

# COMMAND ----------

# The format can be provided via it's own method

df = spark.read.format("csv").load(path, header=True)

df.display()

# COMMAND ----------

# Header cannot be provided via it's own method it must be passed in as an option

df = spark.read.format("csv").option("header", True).load(path)

df.display()