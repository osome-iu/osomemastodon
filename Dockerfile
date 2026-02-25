# Stage 1: frontend build
FROM node:18-bullseye AS frontend-build
WORKDIR /frontend
ENV VUE_PUBLIC_PATH=/
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# Stage 2: python runtime
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install python dependencies
COPY backend/ ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy built frontend into a folder Flask will serve
COPY --from=frontend-build /frontend/dist ./frontend/dist

# Run as non-root
RUN useradd --create-home --home-dir /home/app --shell /bin/bash app \
    && chown -R app:app /app
USER app

EXPOSE 8323
CMD ["python", "backend/server.py"]
