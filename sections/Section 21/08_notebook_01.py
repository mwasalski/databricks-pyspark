# Databricks notebook source
print("This is Notebook 1")

# COMMAND ----------

print(dbutils.widgets.get("football_team"))

# COMMAND ----------

task_run_id = dbutils.widgets.get("task_run_id")

print(f"This is the task run id: {task_run_id}")