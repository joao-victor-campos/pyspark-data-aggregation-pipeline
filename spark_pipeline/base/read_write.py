import warnings

from pyspark.sql import DataFrame

from spark_pipeline.base.spark_client import SparkClient


def read_csv(
    path: str,
    header: str,
) -> DataFrame:
    """Read a dataframe from a csv dataset.

    Args:
        spark_client: client used to connect to a Spark session.
        path: path to the file.
        schema: expected schema for the dataset.
        options: extra options to be passed to Spark.

    Returns:
        Spark dataframe.
    """
    return (
        SparkClient()
        .Session()
        .read.load(path=path, format="csv", inferSchema="true", header=header)
    )


def write_csv(df: DataFrame, path: str) -> None:
    """Write a Dataframe to a parquet file.

    Warning: This function does not use distributed operation
    so it might not be a good solution to bigger datasets.

    Args:
        df: dataframe to be written.
        path: path to write the file.
    """
    warnings.warn(
        "Warning: This function does not use distributed operation,"
        "\n"
        "so it might not be a good solution to bigger datasets."
    )
    df.coalesce(1).write.parquet(path=path, mode="overwrite")
