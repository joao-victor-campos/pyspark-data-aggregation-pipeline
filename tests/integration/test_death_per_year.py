import os

from pyspark.sql import SparkSession
from pyspark.sql.types import LongType, StringType, StructField, StructType

from spark_pipeline.deaths_per_year import extract, load, transform

# def test_extract():
#     assert type(extract()) == DataFrame


# def test_transform():
#     assert type(transform(extract())) == DataFrame


# def test_load():
#     assert load(transform(extract())) is None


def test_pipeline():
    df1 = transform(extract())
    df1 = df1.limit(4)
    spark = SparkSession.builder.getOrCreate()
    schema = StructType(
        [
            StructField("total_deaths", LongType(), True),
            StructField("death_year", StringType(), True),
        ]
    )
    df2 = spark.read.load(
        path="tests/integration/expected_output.csv",
        format="csv",
        schema=schema,
        header="true",
    )
    assert df1.collect() == df2.collect()
    load(df1)
    if len(os.listdir("data/output")) != 0:
        assert True
    else:
        assert False
