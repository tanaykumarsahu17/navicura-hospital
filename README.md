# 🏥 NaviCura - Smart Hospital & Doctor Booking Engine

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

NaviCura is a production-ready, fully containerized backend microservice designed to handle hospital directories, doctor profiles, and patient appointment scheduling. 

## 🎯 Project Motivation
This project was built to demonstrate proficiency in **modern distributed systems**. By stepping away from simple monolithic scripts, this architecture proves the ability to securely manage communication across multiple isolated environments (Web Server, REST API, and Spatial Database) using Docker Compose.

---

## 🏗️ System Architecture

The application operates across three isolated Docker containers:
1. **Frontend (Nginx - Port 8080):** A lightweight web server statically hosting the Vanilla JavaScript, HTML, and CSS user interface.
2. **Backend API (FastAPI - Port 8000):** A high-performance Python RESTful API that processes business logic, handles JWT authentication, and dynamically routes data.
3. **Database (PostgreSQL + PostGIS - Port 5432):** A robust relational database utilizing the PostGIS extension to support complex geographical queries (e.g., finding the nearest hospital).

---

## ✨ Key Technical Features

* **Complete Containerization:** A single `docker compose up` command spins up the entire infrastructure. No local dependencies required.
* **Spatial Database Integration:** Integrates `GeoAlchemy2` and PostGIS, moving beyond standard CRUD operations to handle real-world location intelligence.
* **Secure Authentication Flow:** Implements end-to-end user login utilizing JSON Web Tokens (JWT) and Passlib Bcrypt password hashing.
* **CORS Middleware:** Configured to securely handle cross-origin requests between the Nginx frontend and the FastAPI backend.
* **Interactive API Documentation:** Auto-generated Swagger UI allows developers to test endpoints instantly without Postman.

---

## ⚙️ Quick Start Guide

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Git installed on your local machine.

### Installation & Deployment

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tanaykumarsahu17/navicura-hospital.git](https://github.com/tanaykumarsahu17/navicura-hospital.git)
   cd navicura-hospital
