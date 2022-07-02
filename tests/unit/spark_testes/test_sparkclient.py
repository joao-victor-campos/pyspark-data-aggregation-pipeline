from pyspark.sql import SparkSession

from spark_pipeline.base.spark_client import CreateSession


def test_spark_client():
    assert type(CreateSession()) == SparkSession
