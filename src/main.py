from fastapi import FastAPI
from src.routers import words

app = FastAPI()


app.include_router(words.router)


if __name__ == "__main__":
    pass
