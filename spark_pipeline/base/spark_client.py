from pyspark.sql import SparkSession

# class SparkClient:
#     def __init__(self, session: Optional[SparkSession] = None) -> None:
#         self._session = session


def CreateSession() -> SparkSession:
    """Creates a Spark Session.

    Returns:
        Spark session.
    """
    # if not self._session:
    session = SparkSession.builder.appName("aggregation").getOrCreate()
    return session
