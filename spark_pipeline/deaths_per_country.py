from spark_pipeline.base.spark_client import CreateSession

from pyspark.sql import DataFrame


QUERY = """
SELECT 
    Id,
    Name,
    Country
FROM
    deaths
"""

def extract() -> DataFrame:
    """Mock function.

    Returns:
        number 51.
    """
    CreateSession().read.load("/home/nicholasbaraldi/repos/pyspark-data-aggregation-pipeline/data/AgeDataset-V1.csv", format="csv", inferSchema="true", header="true").createOrReplaceTempView("deaths")
    return CreateSession().sql(QUERY).write.csv("/home/nicholasbaraldi/repos/pyspark-data-aggregation-pipeline/data/output.csv")

extract()