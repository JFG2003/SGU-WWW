from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware  # 👈 Importar CORS
from App.router import books

app = FastAPI()

# 👇 Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://sgu-www.onrender.com",  # 🔥 tu dominio en línea
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # solo permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],         # permitir todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],         # permitir todas las cabeceras
)

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir las rutas de libros
app.include_router(books.router)

# Montar el index.html en la raíz "/"
@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()
