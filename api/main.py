import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dependencies.config import Config
from .dependencies.database import Base, engine
from .models import model_loader
from .routers import index as indexRoute
from .seed import seed_if_needed

model_loader.index()
Base.metadata.create_all(bind=engine)

seed_if_needed()

app = FastAPI()

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

indexRoute.load_routes(app)

if __name__ == "__main__":
	uvicorn.run(app, host=Config.app_host, port=Config.app_port)
