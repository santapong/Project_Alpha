from dagster_pyspark import PySparkResource
from dagster import asset, Output, AssetIn

kinds={"spark"}

@asset(
    name="Ingest-NVDA-Data",
    group_name="NVDA",
    required_resource_keys={"pyspark"},
    kinds=kinds,
)
def ingest_data(pyspark: PySparkResource):
    spark_session = pyspark.spark_session
    df = spark_session.read.json()
    
    return 


@asset(
    name="Extract-NVDA-Data",
    group_name="NVDA",
    kinds=kinds,
    ins={"NVDA_df": AssetIn(key="Ingest-NVDA-Data")}
    )
def extract_data(context, NVDA_df):
    pass


@asset(
    name="Load-NVDA-PSQL",
    group_name="NVDA",
    kinds=kinds,
    ins={"NVDA_df": AssetIn(key="Extract-NVDA-Data")}
)
def load_data(context, NVDA_df):
    pass