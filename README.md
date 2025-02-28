# Proyecto Polls de Django

Este es un proyecto de ejemplo basado en el tutorial oficial de Django. Consiste en una aplicación de encuestas (polls) donde los usuarios pueden votar por diferentes opciones y ver los resultados.

## Características

- Creación y gestión de preguntas (questions) y opciones (choices).
- Interfaz de administración para agregar, editar y eliminar preguntas y opciones.
- Votación en encuestas y visualización de resultados en tiempo real.
- Pruebas automatizadas para garantizar el correcto funcionamiento de la aplicación.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.10
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/polls.git
    cd polls
2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

4. Realiza las migraciones:

    ```bash
    python manage.py migrate

5. Crea un superusuario (para acceder al panel de administración):

    ```bash
    python manage.py createsuperuser
    
6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
7. Accede a la aplicación:
Abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento. Para acceder al panel de administración, visita http://127.0.0.1:8000/admin/.
