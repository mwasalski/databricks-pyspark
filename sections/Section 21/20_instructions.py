# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Use a For each task to run another task in a loop](https://learn.microsoft.com/en-us/azure/databricks/jobs/for-each)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Instructions
# MAGIC
# MAGIC Create a job called **for_each_demo**.
# MAGIC
# MAGIC In this directory you’ll find two notebooks scripts:
# MAGIC
# MAGIC 1. **`iterative_notebook`**  
# MAGIC 2. **`input_notebook`**  
# MAGIC
# MAGIC Create a task called **for_each_task** and provide a list of regions as input values.
# MAGIC
# MAGIC The nested task inside of the **for_each_task** should execute the **iterative_notebook**.
# MAGIC
# MAGIC You can also provide the input list via job parameters or even define a `taskValue` in an upstream Notebook Task:
# MAGIC - Use the **input_notebook** to reference the `taskValue` in the input for the for_each task.