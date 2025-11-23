---
---
## Repository Information

This repo is the companion project for the Udemy course **Azure Databricks and Spark SQL (Python)**. Please follow the step-by-step instructions in the course videos; this README is a short reference for structure and run order.

---
## Setup (generic)

1. Open project in a Databricks workspace
2. Create the appropriate catalogs, schemas and volume
3. Run `one_off` scripts for initial load
4. Create Databricks Job consisting of Notebook tasks for incremental loads


## How to run

**Initial backfill (order):**
1) `00_landing`: `backfill_historical_yellow_trips.py`, `load_taxi_zone_lookup.py`  
2) `01_bronze`: `yellow_trips_raw.py`  
3) `02_silver`: `taxi_zone_lookup.py`, `yellow_trips_cleansed.py`, `yellow_trips_enriched.py`  
4) `03_gold`: `daily_trip_summary.py`
5) `04_export`: `yellow_trips_export.py`

**Ongoing loads:**
- Use `transformations/notebooks`: run `ingest_yellow_trips.py` (recent period) and `ingest_lookup.py`, then process through bronze → silver → gold → export in the same order. The landing step sets a simple job gate via `continue_downstream`.

---

## Outputs

- Bronze: `yellow_trips_raw`  
- Silver: `taxi_zone_lookup`, `yellow_trips_cleansed`, `yellow_trips_enriched`  
- Gold: `daily_trip_summary`
- Export: `yellow_trips_export`

---

## Helper modules (optional)

- `file_exists(path)`
- `download_file(url, dir_path, path)`  
- `add_processed_timestamp(df)`  
- `get_target_yyyymm(months_ago)`  
- `set_continue_downstream("yes"|"no")`

---

## Notes

- Adjust paths, catalogs/schemas, and date ranges for your environment.  