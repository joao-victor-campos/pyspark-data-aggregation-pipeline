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
        .session()
        .read.load(path=path, format="csv", inferSchema="true", header=header)
    )


def write_csv(
    df: DataFrame, path: str, output_partitions: int = 1, mode: str = "append"
) -> None:
    """Write a Dataframe to a parquet file.

    Args:
        df: dataframe to be written.
        path: path to write the file.
        output_partitions: number of partitions to coalesce before writing.
            This parameter will control the number generated files in the output path.
        mode: write mode. E.g. 'append' or 'overwrite'

    """
    df.coalesce(output_partitions).write.mode(mode).parquet(path=path, mode="overwrite")
