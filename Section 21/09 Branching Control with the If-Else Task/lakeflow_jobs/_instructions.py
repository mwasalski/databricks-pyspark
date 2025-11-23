# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Add branching logic to a job with the If/else task](https://learn.microsoft.com/en-us/azure/databricks/jobs/if-else)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Instructions
# MAGIC
# MAGIC Create a job called **if_else_demo**.
# MAGIC
# MAGIC In this directory you’ll find three notebooks scripts:
# MAGIC
# MAGIC 1. **`run_if_true`**  
# MAGIC 2. **`run_if_false`**  
# MAGIC 3. **`branching_control_notebook`**
# MAGIC
# MAGIC Create a task called **if_else_task** and experiment with various conditions that evaluate to either true or false.
# MAGIC
# MAGIC - Assign the `True` branch to run a Notebook Task that executes **run_if_true**.
# MAGIC - Assign the `False` branch to run a Notebook Task that executes **run_if_false**.
# MAGIC
# MAGIC
# MAGIC You can also provide conditions via job parameters or even define a `taskValue` in an upstream Notebook Task:
# MAGIC - Use the **branching_control_notebook** to reference the `taskValue` in the If-else condition task.