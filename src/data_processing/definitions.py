import dagster as dg

import src.data_processing.modules as modules

assets = dg.load_assets_from_modules(modules=[modules])

defs = dg.Definitions(assets=assets)