import os
import dagster as dg

monthly_partition = dg.MonthlyPartitionsDefinition(
    start_date="2022-01-01",
    day_offset=2,
)