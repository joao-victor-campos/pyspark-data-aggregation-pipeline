from pyspark.sql import DataFrame, functions

from spark_pipeline.base import read_write


class DeathsPerYearPipeline:
    """Pipeline that generates the aggregated dataset 'DeathsPerYear'."""

    def __init__(
        self,
        input_path: str = "data/input/AgeDataset-V1.csv",
        output_path: str = "data/output",
    ):
        self.input_path = input_path
        self.output_path = output_path

    def extract(self) -> DataFrame:
        """This function loads a .csv file and creates a Spark DataFrame.

        Returns:
            Spark DataFrame
        """
        return read_write.read_csv(path=self.input_path, header="true").select(
            "Id", "Name", "Death_year"
        )

    def transform(self, df: DataFrame) -> DataFrame:
        """This function counts the IDs grouping by death year.

        Args:
            df (DataFrame): Spark DataFrame

        Returns:
            DataFrame: Aggregated DataFrame
        """
        df_cast = df.select(
            functions.col("Id"),
            functions.col("Death_year").alias("death_year").cast("int"),
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

    def load(self, df: DataFrame) -> None:
        """This function recieves a aggregated DataFrame and writes as a parquet file.

        Args:
            df (DataFrame): Aggregated DataFrame
        """
        read_write.write_csv(df=df, path=self.output_path, mode="overwrite")


def run(pipeline: DeathsPerYearPipeline = DeathsPerYearPipeline()) -> None:
    """Run DeathsPerYearPipeline pipeline."""
    extract_df = pipeline.extract()
    transform_df = pipeline.transform(extract_df)
    return pipeline.load(transform_df)
