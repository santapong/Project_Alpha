from dagster_pyspark import PySparkResource
from dagster import asset, Output, AssetIn
from dagster import AssetExecutionContext

from pyspark.sql import SparkSession

kinds={"spark"}

@asset(
    name="Extract-NVDA-Data",
    group_name="NVDA",
    kinds=kinds,
)
def extract_data(pyspark: PySparkResource):
    
    file_path = "data/kaggle/NVDA.csv"
    
    # Read CSV from fliepath.
    # TODO: Make it can Parsing file. 
    spark_session: SparkSession = pyspark.spark_session
    df = spark_session.read.csv(path=file_path)
    
    # Save file as a parquet. 
    output_path = "data/parquet/NVDA.parquet"
    df.write.mode("overwrite").parquet(output_path)
    
    return Output(output_path)


@asset(
    name="Load-NVDA-Data",
    group_name="NVDA",
    kinds=kinds,
    ins={"NVDA_path": AssetIn(key="Extract-NVDA-Data")}
    )
def load_data(context: AssetExecutionContext, NVDA_path, pyspark: PySparkResource):
    
    # Read Parquet.
    spark_session: SparkSession = pyspark.spark_session
    df = spark_session.read.parquet(NVDA_path)
    
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "alpha.nvda_data") \
        .option("user", "postgres") \
        .option("password", "santapong") \
        .option("driver", "org.postgresql.Driver") \
        .mode("overwrite") \
        .save()

    return 