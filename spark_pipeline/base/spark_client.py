from pyparsing import Optional
from pyspark.sql import SparkSession

# class SparkClient:
#     def __init__(self, session: Optional[SparkSession] = None) -> None:
#         self._session = session

def CreateSession() -> SparkSession:
    #if not self._session: 
        session = SparkSession \
            .builder \
            .appName("aggregation") \
            .getOrCreate()
        return session

