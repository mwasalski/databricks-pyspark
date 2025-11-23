from pyspark.sql.functions import round

def divide_cols(col1, col2):
    """
    Divides one column by another and rounds the result to two decimal places.

    Parameters:
        col1 (Column): The numerator column.
        col2 (Column): The denominator column.

    Returns:
        Column: A Spark column expression representing the rounded division result.
    """
    return round(col1 / col2, 2)