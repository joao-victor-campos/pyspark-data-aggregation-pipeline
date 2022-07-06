from pyspark.sql import DataFrame, functions

from spark_pipeline.base.read_write import read_csv, write_csv
from spark_pipeline.base.spark_client import SparkClient

QUERY = """
SELECT
    Id,
    Name,
    Death_year
FROM
    deaths
"""


def extract() -> DataFrame:
    """This function loads a .csv file and creates a Spark DataFrame.

    Returns:
        Spark DataFrame
    """
    read_csv("data/AgeDataset-V1.csv", header="true").createOrReplaceTempView("deaths")
    return SparkClient().session().sql(QUERY)


def transform(df: DataFrame) -> DataFrame:
    """This function counts the IDs grouping by death year.

    Args:
        df (DataFrame): Spark DataFrame

    Returns:
        DataFrame: Aggregated DataFrame
    """
    df_cast = df.select(
        functions.col("Id"), functions.col("Death_year").alias("death_year").cast("int")
    )

    agg_df = (
        df_cast.groupBy("death_year")
        .agg(functions.count(functions.col("Id")).alias("total_deaths"))
        .select("death_year", "total_deaths")
        .orderBy("death_year")
    )

    df_blank_agg = agg_df.select(
        functions.col("total_deaths"), functions.col("death_year").cast("string")
    ).fillna("Blank")

    return df_blank_agg


def load(df: DataFrame) -> None:
    """This function recieves a aggregated DataFrame and writes as a parquet file.

    Args:
        df (DataFrame): Aggregated DataFrame
    """
    write_csv(df, "data/output")
    return None
