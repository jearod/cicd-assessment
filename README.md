
# DevOps CI/CD Pipeline Project

  

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.9-blue)
![Jenkins](https://img.shields.io/badge/jenkins-2.x-red)
![Docker](https://img.shields.io/badge/docker--compose-v2-blue)
![Security](https://img.shields.io/badge/security-trivy-orange)

## 📋 Descripción del Proyecto

Este repositorio contiene una implementación completa de una arquitectura **DevSecOps**, diseñada para orquestar el ciclo de vida de una aplicación web basada en **Python (Flask)**.

El proyecto va más allá del código fuente, incluyendo la **Infraestructura como Código (IaC)** necesaria para desplegar un entorno de CI/CD local utilizando contenedores. El pipeline automatizado garantiza la calidad del código, la ejecución de pruebas, el análisis de seguridad y la entrega continua de artefactos inmutables.

## 📂 Estructura del Repositorio

El proyecto se organiza en módulos funcionales para separar responsabilidades: 
```bash
.
├──  app/  # Código fuente de la aplicación Flask y Tests Unitarios
├──  infrastructure/  # IaC: Docker Compose y Dockerfile personalizado para Jenkins
├──  pipeline/  # Definición del Pipeline (Jenkinsfile) y Dockerfile de la App
└──  README.md  # Documentación del proyecto
```
  
## 🚀 Arquitectura del Pipeline  

El  flujo  de  trabajo  automatizado (`Jenkinsfile`) se ejecuta sobre agentes efímeros y abarca las siguientes etapas:  

1.  **Checkout & SCM:**  Detección  automática  de  cambios  en  ramas (`development`,  `main`) mediante Polling.

2.  **Test & Code  Quality:**
	*  Creación  de  entornos  virtuales  aislados (`venv`) para cumplimiento de PEP-668.
	*  Ejecución  de  pruebas  unitarias  con  `xmlrunner`.
	*  Análisis  estático  de  código  y  deuda  técnica  mediante  **SonarQube**.

3.  **Build:**  Construcción  de  la  imagen  Docker  de  la  aplicación  optimizada (Base `python:3.9-slim`).
4.  **Security  Audit (DevSecOps):** Escaneo de vulnerabilidades (CVEs) en el sistema base y librerías utilizando **Trivy**.
5.  **Push  to  Registry:**  Autenticación  segura  y  publicación  de  la  imagen  en  **DockerHub**.
6.  **Cleanup:**  Limpieza  de  espacios  de  trabajo  y  artefactos  temporales.  

## 🛠️ Tecnologías e Infraestructura  

*  **Aplicación:** Python 3.9, Flask, Werkzeug.
*  **Contenedorización:** Docker & Docker  Compose.
*  **Orquestación:** Jenkins (Imagen  personalizada  con  Python,  Docker  CLI  y  Trivy  preinstalados).
*  **Calidad:** SonarQube Community Edition.
*  **Seguridad:** Trivy (Aqua  Security).
*  **Repositorio:** DockerHub.

## ⚙️ Despliegue de la Infraestructura (Local)

Este  proyecto  incluye  todo  lo  necesario  para  levantar  los  servidores  de  Jenkins  y  SonarQube  localmente  sin  instalaciones  complejas. 

### Prerrequisitos

	* Docker Desktop / Docker Engine
	* Git  

### Pasos de Instalación  

1.  **Clonar  el  repositorio:**

```bash
	git clone [https://github.com/tu-usuario/cicd-assessment.git](https://github.com/tu-usuario/cicd-assessment.git)
	cd cicd-assessment
```

2.  **Levantar la Infraestructura DevOps:** Navega a la carpeta de infraestructura y construye los contenedores. Es crítico usar `--build` la primera vez para generar la imagen personalizada de Jenkins.
    
```bash
	cd infrastructure
	docker-compose up -d --build
```
    
3.  **Acceder a los Servicios:**
    
    -   **Jenkins:** `http://localhost:8080`
    -   **SonarQube:** `http://localhost:9000`

### Ejecución de la Aplicación (Standalone)

Si solo deseas probar la aplicación web sin el pipeline:

```bash
	# Crear entorno virtual e instalar dependencias
	cd app
	python3 -m venv venv
	source venv/bin/activate  # O venv\Scripts\activate en Windows
	pip install -r requirements.txt

	# Ejecutar
	python app.py
	# Acceder en http://localhost:5000
```

## 🔐 Notas de Configuración

Para que el pipeline funcione correctamente en el entorno local:

-   **SonarQube:** Requiere configurar un Webhook y generar un Token de análisis.
-   **DockerHub:** Se deben configurar las credenciales en Jenkins (ID: `dockerhub-credentials`) utilizando un _Access Token_ por seguridad.
-   **Trivy:** El escáner se actualiza automáticamente gracias a la configuración del `Dockerfile` de infraestructura.