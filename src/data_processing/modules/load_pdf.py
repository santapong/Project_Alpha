import dagster as dg

@dg.asset
def asset1():
    # Perform some computation and produce a result
    result_value = 42
    # Return a MaterializeResult with metadata
    return dg.Output(
        result_value,
        metadata={"result_value":result_value}
        )

@dg.asset
def asset2(context: dg.AssetExecutionContext, asset1):
    # Access the metadata from asset1's MaterializeResult
    result_value = asset1
    context.log.info(f"Received result_value: {result_value}")
    # Perform further computations using result_value

    return dg.MaterializeResult(
        metadata={"Received result_value":result_value}
    )