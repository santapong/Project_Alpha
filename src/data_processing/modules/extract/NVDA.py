from dagster_pyspark import PySparkResource
from dagster import asset

@asset(
    name="Ingest-NVDA-Data",
    group_name="NVDA",
    kinds={"spark"}
)
def ingest_data(pyspark: PySparkResource):
    spark_session = pyspark.spark_session
    df = spark_session.read.json()
