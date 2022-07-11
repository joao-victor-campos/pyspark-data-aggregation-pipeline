import os
from unittest.mock import Mock, patch

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StructField, StructType

from spark_pipeline.base.read_write import read_csv, write_csv


def test_read_csv() -> None:
    expected_output = [{"test": 1, "test_2": 2}, {"test": 1, "test_2": 2}]
    file_path = "/tmp/read_test.csv"
    with open(file_path, "w") as f:
        f.write("test,test_2\n")
        f.write("1,2\n")
        f.write("1,2\n")
    spark = SparkSession.builder.getOrCreate()
    schema = StructType(
        [
            StructField("test", IntegerType(), True),
            StructField("test_2", IntegerType(), True),
        ]
    )
    df1 = spark.createDataFrame(expected_output, schema=schema)
    df2 = read_csv(path=file_path, header="true")
    assert df1.schema == df2.schema
    assert df1.collect() == df2.collect()
    os.remove(file_path)


@patch("pyspark.sql.readwriter.DataFrameWriter.parquet")
def test_write_csv(mock_load: Mock) -> None:
    input = [{"test": 1, "test_2": 2}, {"test": 1, "test_2": 2}]
    spark = SparkSession.builder.getOrCreate()
    df1 = spark.createDataFrame(input, schema="test int, test_2 int")
    write_csv(df=df1, path="path")
    mock_load.assert_called_once_with(path="path", mode="overwrite")
