# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [dbutils.widgets.get()](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-utils#dbutils-widgets-get)
# MAGIC - [Configure Task Parameters](https://learn.microsoft.com/en-us/azure/databricks/jobs/task-parameters)
# MAGIC - [Configure Job Parameters](https://learn.microsoft.com/en-us/azure/databricks/jobs/job-parameters)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Instructions
# MAGIC
# MAGIC In this directory you’ll find two notebooks scripts:
# MAGIC
# MAGIC 1. **`notebook_01`**  
# MAGIC 2. **`notebook_02`**  
# MAGIC
# MAGIC **What was covered in the lecture:**  
# MAGIC - I defined a Lakeflow Job with **two Notebook Tasks**:  
# MAGIC   - **task_01_notebook:** Execute `notebook_01`.
# MAGIC   - **task_02_notebook:** Execute `notebook_02`.  
# MAGIC - Configure **task_02_notebook** to run **task_01_notebook** Task A completes **successfully**.  
# MAGIC
# MAGIC **Serverless compute** was used in the demo with Performance Optimization enabled.
# MAGIC
# MAGIC I added various task and job level parameters:
# MAGIC - **football_team**
# MAGIC - **task_run_id**
# MAGIC
# MAGIC Please ensure you follow along with the lecture.
# MAGIC