<h1 align="center">
  <a href="https://github.com/deep-neural/web-store"><img src="./assets/logo.png" alt="OpenAddons WebStore" height="120"></a>
  <br>
  OpenAddons WebStore
  <br>
</h1>
<h4 align="center">A modern, open-source addon store platform for developers and creators</h4>
<p align="center">
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/Frontend-React-61DAFB.svg?longCache=true&logo=react" alt="React" /></a>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/Language-TypeScript-3178C6.svg?longCache=true&logo=typescript" alt="TypeScript" /></a>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/Backend-Python-3776AB.svg?longCache=true&logo=python" alt="Python" /></a>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/Framework-FastAPI-009688.svg?longCache=true&logo=fastapi" alt="FastAPI" /></a>
  <br>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/State-Redux_Toolkit-764ABC.svg?longCache=true&logo=redux" alt="Redux Toolkit" /></a>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/badge/Icons-Lucide-F56565.svg?longCache=true" alt="Lucide React" /></a>
  <br>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-5865F2.svg" alt="License: MIT" /></a>
  <a href="https://github.com/deep-neural/web-store"><img src="https://img.shields.io/static/v1?label=Build&message=Documentation&color=brightgreen" /></a>
</p>

<div align="center">
  <img src="./assets/demo.png" alt="OpenAddons WebStore Demo" width="800"/>
</div>
<br>

## Overview

OpenAddons WebStore is a full-stack platform designed to host, distribute, and manage addons, extensions, and plugins. Built with modern technologies, it provides a seamless experience for both developers publishing their work and users discovering new addons.

## Features

- **Modern UI/UX** - Clean, responsive interface built with React and TypeScript
- **Developer Dashboard** - Comprehensive tools for addon management and analytics
- **User Reviews & Ratings** - Community-driven feedback system
- **Version Management** - Support for multiple addon versions and update notifications
- **Search & Discovery** - Advanced filtering and categorization
- **Secure Distribution** - Safe addon hosting with automated security scanning
- **REST API** - Full API access for integration and automation
- **Open Source** - Transparent, community-driven development

## Tech Stack

### Frontend
- **TypeScript** - Type-safe JavaScript
- **React** - Component-based UI library
- **Webpack/Vite** - Modern build tooling for development and production

### Backend
- **Python** - Fast and reliable backend services
- **FastAPI** - Modern web framework for development (with reverse proxy to Webpack dev server)
- **Django** - Production static file serving
- **RESTful API** - Clean API architecture
- **Database** - Scalable data storage

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.7+
- Docker and Docker Compose (for deployment)
- Google Cloud SDK (for deployment)

### Clone Repository

```bash
$ git clone https://github.com/deep-neural/web-store
$ cd web-store
```

### Setup Backend

#### Install Miniconda

```bash
# Download Miniconda installer
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Make it executable
$ chmod +x Miniconda3-latest-Linux-x86_64.sh

# Run installer
$ bash Miniconda3-latest-Linux-x86_64.sh

# Follow the prompts:
# - Press Enter to review license
# - Type "yes" to accept
# - Press Enter for default location or specify custom path
# - Type "yes" when asked to initialize conda

# Restart terminal or reload bash
$ source ~/.bashrc

# Verify installation
$ conda --version
```

#### Create Python Environment

```bash
$ conda create -n env1 python=3.7
$ conda activate env1
$ python --version
```

#### Install Dependencies

```bash
$ pip install fastapi uvicorn django gunicorn
```

### Development Mode

For development, use the FastAPI server which provides a reverse proxy to the Webpack dev server for hot reloading and rapid prototyping:

```bash
# Navigate to backend directory
$ cd backend

# Run development server (FastAPI with Webpack reverse proxy)
$ python development.py
```

The development server will:
- Start the FastAPI backend on `http://localhost:8000`
- Proxy frontend requests to the Webpack dev server
- Enable hot module replacement for frontend development
- Provide API endpoints at `/api/*`

### Production Mode

For production, use the Django server which serves pre-built static files from the Webpack bundle:

```bash
# First, build the frontend
$ cd frontend
$ npm run build

# Then run the production server
$ cd ../backend
$ python production.py
```

The production server will:
- Serve optimized, bundled static files using Django
- Run on HTTPS (port 443) with SSL certificates
- Use Gunicorn as the WSGI server for better performance
- Serve all static assets from `/home/ubuntu/webstore/frontend/dist`

### Frontend Development

If you want to run the frontend independently for development:

```bash
$ cd frontend
$ yarn

# Start Webpack dev server
$ yarn dev
```

The frontend will be available at `http://localhost:5173` (or the configured Webpack dev server port).

## Deployment

### GCP Authentication

```bash
# Install Google Cloud CLI
$ snap install google-cloud-cli --classic

# Authenticate with GCP
$ gcloud auth login --no-launch-browser

# Set your project
$ gcloud config set project your-project
```

### Docker Setup

```bash
# Install Docker
$ apt-get install docker.io docker-compose

# Configure Docker to authenticate with Artifact Registry
$ gcloud auth configure-docker us-central1-docker.pkg.dev
```

### Create Docker Artifact Registry

```bash
$ gcloud artifacts repositories create docker-repo \
  --repository-format=docker \
  --location=us-central1
```

### Build and Push Images

```bash
# Build images
$ docker-compose -f docker-compose.yml build

# Push to registry
$ docker-compose -f docker-compose.yml push
```

### Clean Docker Cache and Images

```bash
# Stop and remove all containers
$ docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

# Remove all images
$ docker rmi $(docker images -a -q) --force

# Clean up system
$ docker system prune -a --volumes --force

# Clean build cache
$ docker builder prune --all --force
```

## Project Structure

```
openaddons-webstore/
├── frontend/          # React TypeScript application
│   ├── src/
│   ├── public/
│   ├── dist/         # Production build output
│   └── package.json
├── backend/           # Python backend
│   ├── development.py    # FastAPI dev server with Webpack proxy
│   ├── production.py     # Django production server with static files
│   ├── api/
│   ├── models/
│   ├── services/
│   └── requirements.txt
├── assets/            # Project assets
│   ├── logo.png
│   └── demo.png
└── README.md
```

## Server Modes

### Development Server (`development.py`)
- **Purpose**: Rapid prototyping and development
- **Technology**: FastAPI with reverse proxy
- **Features**:
  - Hot module replacement
  - Fast rebuild times
  - Proxies to Webpack dev server
  - API endpoints available
  - Auto-reload on code changes

### Production Server (`production.py`)
- **Purpose**: Production deployment
- **Technology**: Django with Gunicorn
- **Features**:
  - Serves pre-built static bundles
  - SSL/HTTPS support
  - Optimized performance
  - Security-hardened file serving
  - Production-grade WSGI server

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Roadmap

- [ ] Multi-language support
- [ ] Enhanced analytics dashboard
- [ ] Mobile applications
- [ ] WebSocket support for real-time updates