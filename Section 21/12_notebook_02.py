# Databricks notebook source
print("This is Notebook 2")

# COMMAND ----------

print(dbutils.widgets.get("football_team"))

# COMMAND ----------

tv_show = dbutils.jobs.taskValues.get(
                                        taskKey="task_01_notebook",
                                        key="fave_tv_show"
                                    )

# COMMAND ----------

print(f"The favourite tv show is: {tv_show}")

# COMMAND ----------

no_task_key = dbutils.jobs.taskValues.get(
                                        taskKey="task_01_notebook",
                                        key="no_task_key",
                                        default = "No key provided"
                                    )

# COMMAND ----------

print(no_task_key)