# ==============================================================================
# Dockerfile: AegisEdge PPE Detection & 3-LED Safety Inspection System
# Target Hardware: Edge Gateway / Raspberry Pi 5 / Container Deployment
# ==============================================================================

FROM python:3.11-slim-bookworm

# Set container environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    PORT=8000

# Install required system packages for OpenCV, video processing, and hardware interfaces
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    curl \
    v4l-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency specifications first to leverage Docker layer caching
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code and models
COPY best.pt .
COPY engine.py .
COPY gpio_manager.py .
COPY debounce_filter.py .
COPY pipeline_two_stream.py .
COPY server.py .
COPY samples/ ./samples/
COPY static/ ./static/

# Create snapshots persistence directory
RUN mkdir -p /app/snapshots

# Expose web dashboard and telemetry port
EXPOSE 8000

# Healthcheck to verify dashboard responsiveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/api/config || exit 1

# Start FastAPI Uvicorn Server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

