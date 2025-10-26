# --- Stage 1: Base image ---
FROM python:3.10-slim AS base

# Prevent Python from writing .pyc files & enable clean logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# --- System dependencies ---
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (modern fast package manager)
RUN pip install --no-cache-dir uv

# --- Stage 2: Dependencies layer (caching) ---
FROM base AS deps

# Copy only the requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies (via uv for speed + reliability)
RUN uv pip install --system -r requirements.txt

# --- Stage 3: Runtime image ---
FROM base AS runtime

# Copy installed dependencies from deps layer
COPY --from=deps /usr/local /usr/local

# Copy your project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Default command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
