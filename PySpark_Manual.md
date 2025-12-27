# PySpark Manual for Obsidian

## Introduction
This manual allows you to navigate disjointed PySpark notebooks as a coherent guide. It connects concepts, functions, and solutions logically.

---

## Section 07: Anatomy of PySpark Syntax

### Concept: Step-by-Step vs. Method Chaining
**Context**: When performing multiple transformations on a DataFrame.

#### 1. Step-by-Step Approach
Assign intermediate results to named variables.
**Pros**: Easy to debug, inspect intermediate states.
**Cons**: Verbose, potential memory overhead if not managed (though Spark is lazy).

```python
df = spark.read.format("csv").load("/path/to/file.csv")
df = df.filter("Age > 30")
df.write.format("csv").save("/path/to/directory/")
```

#### 2. Method Chaining
Chain methods in a single statement.
**Pros**: Concise, fluent interface, reads like a pipeline.
**Cons**: Harder to debug intermediate steps.

```python
spark.read.format("csv") \
    .load("/path/to/file.csv") \
    .filter("Age > 30") \
    .write.format("csv") \
    .save("/path/to/directory/")
```
*Note: Use backslash `\` for line continuation in Python to make chains readable.*

---

## Section 08: Reading and Writing Data

### 1. The DataFrameReader and Writer API
**Concept**: Spark uses a consistent API for reading and writing data across formats.
- **Reader**: `spark.read.format(...).option(...).load(path)` or `spark.read.csv(path)`
- **Writer**: `df.write.format(...).option(...).mode(...).save(path)` or `df.write.csv(path)`

### 2. Reading Data
#### Reading CSVs
```python
# Minimal
df = spark.read.csv(path, header=True, inferSchema=True)

# Full Syntax
df = spark.read.format("csv") \
    .option("header", True) \
    .option("sep", ",") \
    .option("inferSchema", True) \
    .load(path)
```
- **Single vs Multiple Files**: Providing a directory path reads *all* compatible files in that directory/partition.
- **Handling Schemas**:
    1.  **Inference**: `inferSchema=True` (Easy but potentially slow/inaccurate).
    2.  **DDL String**: `schema="id int, name string"` (Concise).
    3.  **Programmatic**: using `StructType` and `StructField` (Most robust, handles complex nested types).

#### Reading Other Formats
- **JSON**: `spark.read.json(path)` or `format("json")`. Multiline JSONs might need `option("multiline", True)`.
- **Parquet/ORC/Delta**: Binary, columnar formats. They store schema, so inference is usually automatic and fast.
    - `spark.read.parquet(path)`
    - `spark.read.format("delta").load(path)`

### 3. Writing Data
#### Write Modes (`df.write.mode(...)`)
- `"append"`: Add new files to existing data.
- `"overwrite"`: Replace existing data.
- `"error"` (default): Fail if data exists.
- `"ignore"`: Do nothing if data exists.

#### Partitioning
**Concept**: Organize data into folders based on column values to speed up queries (skipping irrelevant folders).
```python
df.write.partitionBy("region_id").parquet(output_path)
# Creates structure: /path/region_id=1/part-xxx.parquet
```

### 4. Viewing Data
- **`display(df)`**: Databricks-specific. Interactive, sortable, supports plotting.
- **`df.show(n=20, truncate=True)`**: Standard Spark. Text-based output. Good for logs.

### 5. Databricks Utilities (`dbutils`)
**Concept**: Interact with the file system (DBFS) similar to shell commands.
```python
dbutils.fs.ls("dbfs:/path")       # List files
dbutils.fs.cp(src, dst, recurse=True) # Copy
dbutils.fs.rm(path, recurse=True) # Remove
dbutils.fs.head(path)             # Read first bytes
```

---

## Section 09: Unity Catalog & SQL Integration

### 1. Interacting with Tables (Unity Catalog)
**Concept**: PySpark can interact seamlessly with Unity Catalog managed tables.
- **Save as Table**: `df.write.saveAsTable("catalog.schema.table_name")`
- **Read Table**: `spark.read.table("catalog.schema.table_name")`

### 2. Running SQL from PySpark
**Concept**: You can execute SQL queries directly and get a DataFrame back.
```python
# Execute SQL and get DataFrame
df = spark.sql("SELECT * FROM catalog.schema.table")

# Parametrized SQL (using f-strings or format)
table_name = "catalog.schema.table"
df = spark.sql(f"SELECT * FROM {table_name}")
```

### 3. Managed Tables vs Views
- **Managed Table**: Data is managed by Databricks/Spark. Dropping the table deletes the data.
    - `CREATE TABLE ...`
    - `CREATE TABLE target AS SELECT * FROM source`
- **View**: A saved query. No data storage.
    - `CREATE VIEW view_name AS SELECT ...`

### 4. Temporary Views
**Concept**: Register a DataFrame as a temporary table to query it with SQL *within the current session*.
- **Local Temp View**: `df.createOrReplaceTempView("v_name")`. Visible only to current notebook/session.
- **Global Temp View**: `df.createOrReplaceGlobalTempView("gv_name")`. Visible across cluster. Accessed via `global_temp.gv_name`.

```python
df.createOrReplaceTempView("my_temp_view")
spark.sql("SELECT * FROM my_temp_view").show()
```

### 5. DDL Commands (Data Definition Language)
You can run DDL commands via `spark.sql()` or `%sql` cells:
- `CREATE CATALOG [IF NOT EXISTS] name ...`
- `CREATE SCHEMA [IF NOT EXISTS] name ...`
- `CREATE VOLUME ...`
- `DROP [CATALOG|SCHEMA|TABLE|VIEW] name [CASCADE]`

---

## Section 10: Creating DataFrames
**Concept**: Often you need to create small DataFrames for testing or lookup tables from Python lists/dictionaries.

```python
# From List of Lists
data = [["Alice", 30], ["Bob", 25]]
schema = "name string, age int"
df = spark.createDataFrame(data, schema)

# From List of Dictionaries
data_dicts = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
df = spark.createDataFrame(data_dicts) # Schema inferred (can be slow/random order)
```

---

## Section 11: Column Transformations

### 1. Selecting and Referencing Columns
**Concept**: Choosing which columns to keep or transform.
- **String**: `df.select("col_name")`
- **Attribute**: `df.select(df.col_name)`
- **Item**: `df.select(df['col_name'])`
- **Function**: `df.select(col("col_name"))` (Requires `from pyspark.sql.functions import col`)
    - *Best Practice*: `col()` is most flexible for transformations.

### 2. Basic Transformations (`select` vs `selectExpr`)
- **`select(...)`**: Use PySpark functions (`col("price") * 2`, `upper(col("name"))`).
- **`selectExpr(...)`**: Use SQL strings (`"price * 2"`, `"upper(name) as name_upper"`).

### 3. Adding/Replacing Columns
**Concept**: Adding a new derived column or modifying an existing one.
- **`withColumn("name", expr)`**: Adds/replaces a single column.
    - *Warning*: Chaining many `withColumn` calls can cause performance issues (large lineage plan).
- **`withColumns({"name": expr, ...})`**: Adds/replaces multiple columns at once. *Preferred over chaining*.

```python
# Multiple transformations efficiently
df = df.withColumns({
    "density": col("population") / col("area"),
    "name_upper": upper(col("name"))
})
```

### 4. Renaming Columns
- `df.withColumnRenamed("old", "new")`
- `df.withColumnsRenamed({"old1": "new1", "old2": "new2"})` (Spark 3.4+)

### 5. Changing Data Types (Casting)
**Concept**: converting one type to another (e.g., String to Integer).
```python
# Using string type alias
df.select(col("age").cast("string"))

# Using DataType object
from pyspark.sql.types import IntegerType
df.withColumn("age", col("age").cast(IntegerType()))
```

---

## Section 12: Built-in Functions
**Concept**: PySpark has a rich library of functions in `pyspark.sql.functions`.

### 1. Math Functions
- `round(col, scale)`: Round to decimal places.
- `greatest(col1, col2)`: Returns the max value among columns (row-wise).
- `least(col1, col2)`: Returns the min value.

### 2. String Functions
- `upper(col)`, `lower(col)`, `initcap(col)`: Case conversion.
- `length(col)`: Character count.
- `concat(col1, lit(" "), col2)`: Join strings.
- `concat_ws(sep, col1, col2)`: Join with separator.

### 3. Date & Time
**Concept**: Dates (`yyyy-MM-dd`) vs Timestamps (`yyyy-MM-dd HH:mm:ss`).
- **Conversion**:
    - `to_date(col, format)`: String -> Date.
    - `to_timestamp(col, format)`: String -> Timestamp.
- **Current**: `curdate()`, `current_timestamp()`.
- **Manipulation**:
    - `date_add(col, days)`: Add days.
    - `timestamp_diff(unit, start, end)`: Difference between times.
    - `date_format(col, pattern)`: Format as string (e.g., "MMMM, yyyy").

---

## Section 13: Joins and Unions

### 1. Joining DataFrames (`join`)
**Concept**: Combining two DataFrames based on a common key.
```python
joined_df = df1.join(df2, df1.id == df2.id, "left")
```
- **Join Types**:
    - `"inner"`: Matching rows only (default).
    - `"left"`, `"right"`, `"fullouter"`: Standard SQL joins.
    - `"left_anti"`: Rows in left that do NOT exist in right.
    - `"cross"`: Cartesian product (use `df1.crossJoin(df2)`).

### 2. Unioning DataFrames (`union`)
**Concept**: Stacking DataFrames vertically (appending rows).
- **`df1.union(df2)`**: Resolves by **position**. Columns must be in same order.
- **`df1.unionByName(df2)`**: Resolves by **name**. Safer.
    - `unionByName(df2, allowMissingColumns=True)`: Fills missing columns with nulls.

---

## Section 14: Filtering, Sorting, and Deduplication
**Concept**: Row-level operations to slice and dice data.

### 1. Filtering (`filter` or `where`)
Both are aliases.
- **Expression**: `df.filter(col("region") == "Asia")`
- **SQL String**: `df.filter("region = 'Asia'")`
- **Logic**:
    - `(col("a") > 1) & (col("b") < 5)` (AND)
    - `(col("a") > 1) | (col("b") < 5)` (OR)

### 2. Sorting (`sort` or `orderBy`)
```python
df.sort(col("population").desc())
df.orderBy("region", "population") # Ascending by default
```

### 3. Deduplication
- `df.dropDuplicates()`: Unique rows across all columns.
- `df.dropDuplicates(["col1", "col2"])`: Unique based on specific subset.

### 4. Handling Nulls (`dropna`)
- `df.dropna()`: Drop row if *any* column is null.
- `df.dropna(how="all")`: Drop row if *all* columns are null.
- `df.dropna(subset=["id"])`: Drop if *specific* column is null.

---

## Section 15: Aggregation and Pivoting

### 1. Grouping and Aggregating
**Concept**: Split data into groups and compute metrics.
- **`groupBy("col")`**: Returns a `GroupedData` object.
- **`agg(...)`**: Apply functions (`sum`, `avg`, `max`, `count`) to groups.

```python
from pyspark.sql.functions import sum, avg

df.groupBy("region").agg(
    sum("population").alias("total_pop"),
    avg("area").alias("avg_area")
)
```

### 2. Pivoting (`pivot`)
**Concept**: Rotate unique values of a column into multiple columns (Long to Wide).
```python
# Turns "region" values (Asia, Europe...) into columns
df.groupBy("sub_region") \
  .pivot("region") \
  .sum("population")
```

### 3. Unpivoting (`unpivot`)
**Concept**: Rotate columns into rows (Wide to Long). (Spark 3.4+)
```python
df.unpivot(
    ids=["id"], 
    values=["2023_sales", "2024_sales"], 
    variableColumnName="year", 
    valueColumnName="sales"
)
```

---

## Section 16: Conditional Logic

### 1. The `when` Function
**Concept**: PySpark's equivalent of `IF...ELSE` or `CASE WHEN`.
```python
from pyspark.sql.functions import when

df.withColumn("size_class", 
    when(col("pop") > 1_000_000, "Large")
    .when(col("pop") > 100_000, "Medium")
    .otherwise("Small")
)
```

### 2. SQL Expressions (`expr`)
**Concept**: Use raw SQL strings for complex conditions without importing many functions.
```python
from pyspark.sql.functions import expr

# CASE WHEN inside a select/withColumn
df.withColumn("category", expr("CASE WHEN pop > 100 THEN 'A' ELSE 'B' END"))
```

### 3. Handling Nulls (`coalesce`)
- **`coalesce(col1, col2, lit(default))`**: Returns the first non-null value. Useful for filling nulls.

---

## Section 19: Delta Lake Operations
**Concept**: Delta Lake adds ACID transactions, DML support (delete/update), and history to standard Parquet lakes.

### 1. The `DeltaTable` API
To perform DML operations (Update, Delete, Merge), you need a `DeltaTable` object, not a DataFrame.
```python
from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "catalog.schema.table")
# OR
dt = DeltaTable.forPath(spark, "/path/to/delta/table")
```

### 2. DML Operations
- **Delete**: `dt.delete("region = 'North'")`
- **Update**:
    ```python
    dt.update(
        condition = "id = 5",
        set = { "status": lit("Active") }
    )
    ```
- **Merge (Upsert)**:
    ```python
    dt.alias("target").merge(
        source_df.alias("source"),
        "target.id = source.id"
    ).whenMatchedUpdateAll() \
     .whenNotMatchedInsertAll() \
     .execute()
    ```

### 3. Time Travel & History
**Concept**: Query older versions of the table.
- **View History**: `spark.sql("DESCRIBE HISTORY table_name")`
- **Read Old Version**:
    ```python
    spark.read.format("delta").option("versionAsOf", 5).load(path)
    # OR
    spark.read.format("delta").option("timestampAsOf", "2023-10-01").load(path)
    ```
- **Restore**: `RESTORE TABLE table_name TO VERSION AS OF 5`

### 4. Schema Evolution
**Concept**: Automatically add new columns from source to target during write/merge.
- **Write**: `.option("mergeSchema", "true")`
- **Merge**: `.withSchemaEvolution()`

---

## Section 21: Workflows (Jobs)
**Concept**: Orchestrating notebooks as production jobs.
- **Parameters**: Pass variables into notebooks using widgets or task values.
    - `dbutils.widgets.text("param", "default")`
    - `val = dbutils.widgets.get("param")`
- **Task Values**: Pass data *between* tasks in a workflow.
    - Set: `dbutils.jobs.taskValues.set(key="k", value=v)`
    - Get: `dbutils.jobs.taskValues.get(taskKey="t", key="k")`

## Section 22: Performance Optimization

### 1. Lazy Evaluation
**Concept**: Transformations (e.g., `select`, `filter`) are logically planned but not executed until an **Action** (e.g., `show`, `count`, `save`) is called.

### 2. Caching
**Concept**: Store DataFrame in memory/disk to avoid recomputing it for multiple downstream actions.
- **Disk Cache**: Automatic on Databricks (copy of remote data to local SSD).
- **Spark Cache**: `df.cache()` (Memory) or `df.persist()` (Configurable storage level).
    - *Best Practice*: Cache only if reused significantly. `df.unpersist()` when done.

### 3. Broadcast Joins
**Concept**: Copy the smaller table to all nodes to avoid shuffling the large table.
- **Automatic**: Triggered if table < 10MB (default).
- **Manual**: `df_large.join(broadcast(df_small), ...)`

### 4. Liquid Clustering (Delta)
**Concept**: Replaces Hive-style partitioning. Clusters data based on column access patterns.
- **Write**: `df.write.format("delta").clusterBy("col").save(path)`
- **Optimize**: `OPTIMIZE table_name`

---

## Section 25: User Defined Functions (UDFs)
**Concept**: Apply custom Python code to DataFrame columns.
*Warning*: Slower than native functions due to serialization overhead. Use only when logical cannot be expressed with `pyspark.sql.functions`.

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

@udf(IntegerType())
def count_chars(s):
    return len(s)

df.withColumn("len", count_chars("name"))
```

## Section 18, 20, 23, 26, 28: End-to-End Projects
These sections contain iterative implementation of an ETL pipeline (e.g., NYC Taxi data).
- **Core Pattern**:
    1.  **Ingest** (Bronze): Read raw CSV/JSON, add metadata (`_ingest_time`), save as Delta.
    2.  **Refine** (Silver): Clean, dedup, join (Star Schema).
    3.  **Agg** (Gold): Business-level aggregations.
- **Key Features Used**: Delta Lake (Merge), Orchestration (Jobs), and Medallion Architecture.

---

## Section 29: Structured Streaming
**Concept**: Process data as it arrives (unbounded table) rather than in batches.

### 1. Auto Loader (`cloudFiles`)
**Concept**: Efficiently ingests new files from cloud storage using file notifications.
```python
df = spark.readStream.format("cloudFiles") \
    .option("cloudFiles.format", "csv") \
    .option("cloudFiles.schemaLocation", "/path/to/schema") \
    .load("/path/to/source")
```

### 2. Watermarking & Aggregation
**Concept**: Handle late data by specifying how long to wait.
```python
from pyspark.sql.functions import window

df.withWatermark("timestamp_col", "10 minutes") \
  .groupBy(window("timestamp_col", "1 hour")) \
  .count()
```

### 3. Writing Streams
**Concept**: Output stream to sink. *Always* specify a checkpoint location.
```python
query = df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start("/path/to/output")
```
- **Output Modes**:
    - `append`: Only new rows (default).
    - `complete`: Entire updated result table.
    - `update`: Only rows that changed.

## Section 30: Streaming Project
**Concept**: Applies Section 29 concepts to build a real-time pipeline (e.g., IoT data, real-time weather).
- **Pattern**: Auto Loader (Ingest) -> Transformation -> Delta Table (Sink).
---
