from pyspark.sql import DataFrame, SparkSession

from spark_pipeline.base.spark_client import SparkClient
from spark_pipeline.deaths_per_year import extract, load, transform


def test_spark_client():
    assert type(SparkClient().Session()) == SparkSession


def test_extract():
    assert type(extract()) == DataFrame


def test_transform():
    assert type(transform(extract())) == DataFrame


def test_load():
    assert load(transform(extract())) is None
