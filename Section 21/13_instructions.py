# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Lakeflow Jobs](https://learn.microsoft.com/en-us/azure/databricks/jobs/)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Instructions
# MAGIC
# MAGIC In this directory you’ll find two python scripts:
# MAGIC
# MAGIC 1. **`python_script_01`**  
# MAGIC 2. **`python_script_02`**  
# MAGIC
# MAGIC **What was covered in the lecture:**  
# MAGIC - I defined a Lakeflow Job with **two Python Script Tasks**:  
# MAGIC   - **task_01_python_script:** Execute `python_script_01`.  
# MAGIC   - **task_02_python_script:** Execute `python_script_02`.  
# MAGIC - Configure **task_02_python_script** to run **task_01_python_script** Task A completes **successfully**.  
# MAGIC
# MAGIC **Serverless compute** was used in the demo with Performance Optimization enabled.
# MAGIC
# MAGIC **Parameters:**
# MAGIC I provided parameters in the task definitions `["John", "{{workspace.id}}"]` and retrieved them using the `sys` module
# MAGIC