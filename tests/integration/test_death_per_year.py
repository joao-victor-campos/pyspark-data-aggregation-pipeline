from pyspark.sql import DataFrame

from spark_pipeline.deaths_per_year import extract, load, transform


def test_extract():
    assert type(extract()) == DataFrame


def test_transform():
    assert type(transform(extract())) == DataFrame


def test_load():
    assert load(transform(extract())) is None
