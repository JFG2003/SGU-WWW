# SGU-WWW
Desarrollo del proyecto backend 
__________________________________________

Universidad del Valle
Programa: Ingeniería en Sistemas
Juan Felipe Guancha Durán – 2159950
Tuluá, Valle del Cauca
Fecha: 4/4/2025

____________________________________________

## Descripcion

Este proyecto es una API REST creada con FastAPI que permite gestionar libros (crear, listar, actualizar y eliminar). Utiliza SQLAlchemy como ORM para la base de datos y Pydantic para la validación de datos.

_____________________________________________

## Instrucciones para su ejecucion local:

1) clonar el repositorio:
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio

2) Crear un entorno virtual de python:
    NOTA: en este ejemplo usaremos un entorno virtual basado en UNIX (venv/bin/activate), el cual funciona si estas utilizando git bash, MSYS2 o similares

    si usas powershell o cmd consulta las instrucciones correspondientes. 
    o usa el python de windows para recrear el entorno virtual con la carpeta scripts   

    Para este ejemplo ejecutamos desde la raiz del codigo:

        * python -m venv venv

    Activar el entorno virtual:

        * source venv/bin/activate

    o alternativamente:

        * . venv/bin/activate

    si tienes windows con powershell y tienes la carpeta scripts:

        * .\venv\Scripts\Activate.ps1

3)  Instalar las dependencias:
        con el entorno virtual activado, instala las dependencias listadas en el archivo requirementes.txt

        * pip install -r requirements.txt

4)  Ejecutar la aplicacion:

        * uvicorn App.Main::app --reload


    * Luego podras abrir el siguiente enlace:

        http://127.0.0.1:8000/docs
    

## Tecnologías utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
