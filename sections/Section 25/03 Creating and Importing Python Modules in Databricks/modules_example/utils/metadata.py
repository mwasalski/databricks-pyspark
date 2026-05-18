from pyspark.sql.functions import current_timestamp

def add_processed_timestamp(df):
    """
    Adds a 'processed_timestamp' column to the given DataFrame,
    containing the current timestamp for each row.

    Parameters:
        df (DataFrame): The input Spark DataFrame.

    Returns:
        DataFrame: A new DataFrame with the 'processed_timestamp' column added.
    """
    return df.withColumn("processed_timestamp", current_timestamp())


