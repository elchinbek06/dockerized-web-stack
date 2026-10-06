# Dockerized Multi-Container Web Stack

A production-ready microservices architecture built with **Nginx**, **FastAPI (Python)**, and **PostgreSQL**, orchestrated using **Docker Compose**.

## 🏗️ Architecture
- **Nginx**: Reverse Proxy serving as the entry point on port 80.
- **FastAPI**: Backend REST API executing logic and connecting to the database.
- **PostgreSQL**: Relational Database storing application data with persistent volume storage.
- **Docker Network**: Isolated bridge network for internal inter-service communication.

## 🚀 How to Run

### Prerequisites
- Docker Engine installed
- Docker Compose installed
```bash
   git clone [https://github.com/YOUR_USERNAME/dockerized-web-stack.git](https://github.com/elchinbek06/dockerized-web-stack.git)
   cd dockerized-web-stack
