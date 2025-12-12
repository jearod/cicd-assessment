FROM jenkins/jenkins:lts

# Cambiamos a root para instalar
USER root

# 1. Instalamos dependencias base, Python y Docker
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    docker.io \
    wget \
    apt-transport-https \
    gnupg \
    lsb-release

# 2. Instalamos Trivy (CORRECCIÓN AQUÍ)
# En lugar de $(lsb_release -sc), forzamos el uso de 'bookworm'
RUN wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | tee /usr/share/keyrings/trivy.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb bookworm main" | tee /etc/apt/sources.list.d/trivy.list && \
    apt-get update && \
    apt-get install -y trivy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 3. Permisos de Docker para Jenkins
RUN usermod -aG docker jenkins

# Volvemos al usuario seguro
USER jenkins