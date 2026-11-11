# Imagen base oficial de Python, version ligera
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto MVC (modelo, vista, controlador, main.py)
COPY . .

# Ejecutar las pruebas al construir la imagen (control de calidad)
RUN pytest -q

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "main.py"]
