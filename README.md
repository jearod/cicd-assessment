# DevOps CI/CD Pipeline Project

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.9-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Jenkins](https://img.shields.io/badge/jenkins-pipeline-red)

## 📋 Descripción del Proyecto

Este repositorio aloja una aplicación web basada en **Python (Flask)** diseñada para demostrar la implementación de un pipeline completo de **CI/CD (Integración y Despliegue Continuos)** en un entorno Ágil.

El objetivo principal es orquestar un flujo de trabajo automatizado que garantice la calidad, seguridad y desplegabilidad del software utilizando herramientas estándar de la industria.

## 🚀 Arquitectura del Pipeline

El flujo de trabajo automatizado (definido en el `Jenkinsfile`) abarca las siguientes etapas:

1.  **SCM (Source Code Management):** Control de versiones y gestión de ramas en GitHub.
2.  **Continuous Integration (CI):**
    * Ejecución de pruebas unitarias automatizadas (`unittest`).
    * Análisis de calidad de código estático mediante **SonarQube**.
3.  **Build:** Construcción de imagen de contenedor con **Docker**.
4.  **Security (DevSecOps):** Escaneo de vulnerabilidades en la imagen (CVEs) utilizando **Trivy**.
5.  **Continuous Delivery (CD):** Publicación de la imagen verificada en **DockerHub**.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.9 (Flask)
* **Contenedorización:** Docker
* **Orquestación CI/CD:** Jenkins
* **Calidad de Código:** SonarQube
* **Seguridad:** Trivy
* **Repositorio de Artefactos:** DockerHub

## ⚙️ Instalación y Ejecución Local

Para ejecutar la aplicación en un entorno local de desarrollo:

### Prerrequisitos
* Python 3.9+
* Docker (Opcional, para pruebas de contenedor)

### Ejecución Manual
```bash
# Instalar dependencias
pip install -r app/requirements.txt

# Ejecutar la aplicación
python app/app.py