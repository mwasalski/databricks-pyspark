# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC [Python API Reference](https://spark.apache.org/docs/latest/api/python/reference/index.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Step by Step Approach
# MAGIC
# MAGIC The step-by-step approach breaks your code into clear, discrete stages—first ingest, then transform, then persist—by assigning each intermediate result to a named variable. 
# MAGIC
# MAGIC That modular style makes it easy to inspect and debug at each point.

# COMMAND ----------

df = spark.read.format("csv").load("/path/to/file.csv")

# COMMAND ----------

df = df.filter("Age > 30")

# COMMAND ----------

df.write.format("csv").save("/path/to/directory/")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Chaining Methods
# MAGIC Method chaining is a “fluent” interface pattern where each method returns an object—often the same instance or a new immutable one—so you can immediately call the next operation on it. 
# MAGIC
# MAGIC Instead of breaking your logic into named, intermediate variables, you stitch calls together in a linear flow that reads like a pipeline: each step consumes the output of the previous one. 
# MAGIC
# MAGIC This style makes the overall sequence of transformations concise and expressive, emphasizes the order of operations, and reduces boilerplate—though for very complex or conditional logic you might still choose to pull out intermediate results for clarity or debugging.

# COMMAND ----------

spark.read.format("csv").load("/path/to/file.csv").filter("Age > 30").write.format("csv").save("/path/to/directory/")

# COMMAND ----------

# MAGIC %md
# MAGIC You can use backslashes to break a long method chain into readable, indented lines.
# MAGIC
# MAGIC In Python, a backslash (\) indicates that a statement continues onto the next line. Without it, Python would assume the code ends at the newline and you’d get a syntax error.

# COMMAND ----------

spark.read.format("csv").load("/path/to/file.csv").\
filter("Age > 30").\
write.format("csv").save("/path/to/directory/")