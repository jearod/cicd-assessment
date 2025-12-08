# Usar una imagen base ligera de Python
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos e instalar dependencias
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY app/ .

# Exponer el puerto
EXPOSE 5000

# Usuario para Trivy/Sonar
RUN useradd -mmyuser
USER myuser

# Comando de inicio
CMD ["python", "app.py"]