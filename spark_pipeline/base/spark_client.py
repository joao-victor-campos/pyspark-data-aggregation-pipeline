from typing import Optional

from pyspark.sql import SparkSession


class SparkClient:
    """Handle the creation of a Spark session."""

    def __init__(self, session: Optional[SparkSession] = None) -> None:
        self._session = session

    def session(self) -> SparkSession:
        """Get a created SparkSession or if it doesn't exist create one.

        Returns:
            Spark session.
        """
        if not self._session:
            self._session = self.create_session()
        return self._session

    def create_session(self) -> SparkSession:
        """Creates a Spark Session.

        Returns:
            Spark session.
        """
        # if not self._session:
        session = SparkSession.builder.getOrCreate()
        return session
