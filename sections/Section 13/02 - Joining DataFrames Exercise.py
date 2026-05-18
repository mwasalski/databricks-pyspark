# Databricks notebook source
# MAGIC %md
# MAGIC ### 📌 Reading the Tables into DataFrame objects

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

# Load the countries_population table, picking only the country_id, name (aliased to country), population, area, and ID columns

df_countries = spark.read.table("population_metrics.default.countries_population").\
                select("country_id", col("name").alias("country"), "population", "area_km2", "region_id", "sub_region_id")

# Load the country_regions table, selecting the region ID and renaming 'name' to 'region'
df_regions = spark.read.table("population_metrics.default.country_regions").select("id", col("name").alias("region"))

# Load the country_sub_regions table, selecting the sub-region ID and renaming 'name' to 'sub_region'
df_sub_regions = spark.read.table("population_metrics.default.country_sub_regions").select("id", col("name").alias("sub_region"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Step by step multi-join operations

# COMMAND ----------

# Perform a left join between countries and regions to bring in region names
df_int = (
    df_countries
    .join(
        df_regions,
        df_countries.region_id == df_regions.id,
        how="left"  # keep all countries, even if they lack a matching region
    )
    # select only the columns we need for the intermediate result
    .select(
        "country_id",
        "country",
        "region",
        "population",
        "area_km2",
        "sub_region_id"
    )
)

# Perform a left join on the intermediate DataFrame to bring in sub-region names
df_final = (
    df_int
    .join(
        df_sub_regions,
        df_int.sub_region_id == df_sub_regions.id,
        how="left"  # keep all rows, even if no matching sub-region
    )
    # select and reorder final output columns (dropping the foreign key id)
    .select(
        "country_id",
        "country",
        "region",
        "sub_region",
        "population",
        "area_km2"
    )
)

# Save the result as a managed table
df_final.write.saveAsTable("population_metrics.default.countries_consolidated")

# COMMAND ----------

# This alternate syntax uses a single fluent method‐chain on the DataFrames (rather than intermediate variables) to perform both joins, selections, and the write in one continuous pipeline

df_countries.\
            join(df_regions,df_countries.region_id == df_regions.id, "left").\
            select("country_id", "country", "region", "population", "area_km2", "sub_region_id").\
            join(df_sub_regions, df_countries.sub_region_id == df_sub_regions.id, "left").\
            select("country_id", col("name").alias("country"), "region", "sub_region", "population", "area_km2").\
            write.saveAsTable("population_metrics.default.countries_consolidated")