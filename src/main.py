from fastapi import FastAPI
from routers import words

app = FastAPI()


app.include_router(words.router)


if __name__ == "__main__":
    pass
