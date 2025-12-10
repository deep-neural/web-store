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
- **Modern tooling** - Vite/Webpack for optimal build performance

### Backend
- **Python** - Fast and reliable backend services
- **FastAPI** - Modern web framework
- **RESTful API** - Clean API architecture
- **Database** - Scalable data storage

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.7+
- Docker and Docker Compose
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
$ pip install fastapi uvicorn
```

#### Run Backend Server

```bash
$ python server.py
```

The backend API will be available at `http://localhost:8000`.

### Setup Frontend

```bash
$ cd frontend
$ yarn

# Start development server
$ yarn dev
```

The frontend will be available at `http://localhost:5173`.

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
│   └── package.json
├── backend/           # Python backend
│   ├── api/
│   ├── models/
│   ├── services/
│   └── requirements.txt
├── assets/            # Project assets
│   ├── logo.png
│   └── demo.png
└── README.md
```

## API Documentation

API documentation is available at `/api/docs` when running the backend server.

## Contributing

We welcome contributions from the community. Please read our contributing guidelines before submitting pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Roadmap

- [ ] Payment integration for premium addons
- [ ] Multi-language support
- [ ] Enhanced analytics dashboard
- [ ] Mobile applications
- [ ] WebSocket support for real-time updates
