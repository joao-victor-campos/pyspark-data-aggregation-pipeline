from typing import Optional

from pyspark.sql import SparkSession


class SparkClient:
    """Handle the creation of a Spark session."""

    def __init__(self, session: Optional[SparkSession] = None) -> None:
        self._session = session

    def Session(self) -> SparkSession:
        """Get a created SparkSession or if it doesn't exist create one.

        Returns:
            Spark session.
        """
        if not self._session:
            self._session = self.CreateSession()
        return self._session

    def CreateSession(self) -> SparkSession:
        """Creates a Spark Session.

        Returns:
            Spark session.
        """
        # if not self._session:
        session = SparkSession.builder.getOrCreate()
        return session
