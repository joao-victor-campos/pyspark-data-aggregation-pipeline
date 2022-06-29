from spark_pipeline.base.spark_client import CreateSession
from pyspark.sql import SparkSession

def test_spark_client():
    assert type(CreateSession()) == SparkSession