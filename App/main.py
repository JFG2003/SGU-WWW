from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from App.router import books
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta donde está tu index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(books.router)



app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()
