# Multi-stage build for OpenAddons WebStore

# Stage 1: Build Frontend
FROM node:18-alpine AS frontend-builder

WORKDIR /build

# Copy frontend package files
COPY frontend/package*.json frontend/yarn.lock* ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy frontend source
COPY frontend/ ./

# Build the frontend
RUN yarn build

# Stage 2: Production Runtime
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install system dependencies and Python
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python and pip
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Copy requirements file first (for better caching)
COPY backend/requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend/ ./backend/

# Copy built frontend from stage 1
COPY --from=frontend-builder /build/dist ./frontend/dist

# Create a non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port 443 for HTTPS (production)
EXPOSE 443

# Set working directory to backend
WORKDIR /app/backend

# Run production server
CMD ["python", "production.py"]