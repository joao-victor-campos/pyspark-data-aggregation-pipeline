import pathlib
from unittest import mock

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import LongType, StringType, StructField, StructType

from spark_pipeline import deaths_per_year_pipeline

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()


@mock.patch("spark_pipeline.base.read_write.write_csv", autospec=True)
def test_pipeline(mock_write_csv: mock.Mock):
    # arrange
    spark = SparkSession.builder.getOrCreate()
    schema = StructType(
        [
            StructField("total_deaths", LongType(), True),
            StructField("death_year", StringType(), True),
        ]
    )
    expected_df = spark.read.load(
        path=f"{CURRENT_PATH}/expected_output.csv",
        format="csv",
        schema=schema,
        header="true",
    )
    pipeline = deaths_per_year_pipeline.DeathsPerYearPipeline(
        input_path=f"{CURRENT_PATH}/input.csv"
    )

    # act
    deaths_per_year_pipeline.run(pipeline)
    output_df: DataFrame = mock_write_csv.call_args.kwargs["df"]

    # assert
    assert sorted(output_df.collect()) == sorted(expected_df.collect())
    assert mock_write_csv.call_args.kwargs["mode"] == "overwrite"
