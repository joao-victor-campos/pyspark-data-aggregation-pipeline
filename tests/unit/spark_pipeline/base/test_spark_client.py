from pyspark.sql import SparkSession

from spark_pipeline.base.spark_client import SparkClient


def test_spark_client():
    assert isinstance(SparkClient().session(), SparkSession)
