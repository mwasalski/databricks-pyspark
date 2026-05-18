# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Workspace Modules](https://docs.databricks.com/aws/en/files/workspace-modules)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Instructions

# COMMAND ----------

# MAGIC %md
# MAGIC Refer to the notebook named `calling_notebook` in the `modules_example` folder.
# MAGIC
# MAGIC The module imports work **without needing to explicitly add the project root to `sys.path`**.
# MAGIC
# MAGIC This is because, in Databricks, the **parent folder of the notebook is automatically added to `sys.path`** at runtime.
# MAGIC
# MAGIC If you create a notebook in a different location, you’ll need to manually add the path to the module's parent directory using `sys.path.append(...)` for the imports to work — go ahead and try it!