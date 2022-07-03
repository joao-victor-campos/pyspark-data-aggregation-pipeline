from pyspark.sql import DataFrame, SparkSession

from spark_pipeline.base.spark_client import CreateSession
from spark_pipeline.deaths_per_year import extract, load, transform


def test_spark_client():
    assert type(CreateSession()) == SparkSession


def test_extract():
    assert type(extract()) == DataFrame


def test_transform():
    assert type(transform(extract())) == DataFrame


def test_load():
    assert type(load(transform(extract()))) is None
