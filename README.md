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
2. **Launch the infrastructure:**
   Build and start the isolated network of containers in the background.

   ```Bash
   docker compose up -d --build
3. **Access the Application:**

   * **Frontend UI:** http://localhost:8080

   * **API Documentation (Swagger):** http://localhost:8000/docs

   * **Database Connection: localhost:** 5432 (User: postgres | Password: admin)

Note: On the first launch, the database will be automatically structured but completely empty. You must register a user and inject dummy hospitals/doctors to populate the UI.

### 🗺️ API Endpoints Overview
Method    Endpoint       Description                            Auth Required
POST      /auth/signup   Register a new patient account               ❌
POST      /auth/login    Authenticate and receive JWT                 ❌
GET       /users/me      Fetch active user profile via token          ✅
GET       /hospitals/    Retrieve a list of all hospitals             ❌
GET       /doctors/      Directory of medical professionals           ❌
POST      /appointments/ Book a new consultation                      ✅

### 🗄️ Database Schema
* **Users Table:** Stores patient credentials (hashed) and contact info.

* **Hospitals Table:** Stores facility details and spatial coordinates (Geometry).

* **Doctors Table:** Foreign-keyed to Hospitals; stores specialty and bio.

* **Appointments Table:** The join table mapping Users to Doctors with timestamps.

### 📁 Project Structure
Plaintext
navicura-hospital/
├── app/
│   ├── api/          # API Routers (Auth, Doctors, Hospitals, etc.)
│   ├── core/         # Database connection & security configurations
│   ├── models/       # SQLAlchemy ORM database tables
│   ├── schemas/      # Pydantic models for incoming/outgoing data validation
│   └── main.py       # FastAPI application factory & CORS setup
├── frontend/         # Vanilla JS, HTML, CSS (Served by Nginx container)
├── docker-compose.yml# Multi-container orchestration instructions
├── Dockerfile        # Python FastAPI container blueprint
└── requirements.txt  # Python backend library dependencies
