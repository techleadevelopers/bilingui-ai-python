# Base leve com Python + FFmpeg
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dependências do sistema (inclui toolchain e headers de áudio para PyAudio)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libsndfile1 \
    portaudio19-dev \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia requirements separado para cachear melhor
COPY requirements.txt .

# Instala dependências (sem cache para reduzir layer)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia código
COPY . .

EXPOSE 8000

# Usa a porta do ambiente (Railway define PORT)
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
