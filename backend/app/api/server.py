from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title="Lesson2")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    return app


app = get_application()
