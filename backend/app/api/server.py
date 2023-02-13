from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def get_application():
    app = FastAPI(title="Lesson2")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_application()
