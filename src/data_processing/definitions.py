import dagster as dg
from dagster_pyspark import PySparkResource

import src.data_processing.modules as modules

assets = dg.load_assets_from_modules(modules=[modules])

defs = dg.Definitions(
    assets=assets,
    resources={
        "pyspark": PySparkResource(
            spark_config={
                "spark.executor.memory":"2g"
            }
        )
    }
)