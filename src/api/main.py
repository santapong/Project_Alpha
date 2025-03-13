import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import router_login

load_dotenv()

# Create FASTAPI Instance
app = FastAPI(
    title="Project Alpha"
)

# Add redirect top /docs
@app.get("/")
def docs():
    return RedirectResponse(url="/docs")

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Add router for fastapi
app.include_router(router_login)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True)

