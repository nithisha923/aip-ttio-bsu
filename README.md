# AIP for TTIO – Bowie State University

## 📌 Project Overview

The **AIP for TTIO (Technology Transfer & Innovation Office)** is a full-stack web application developed for Bowie State University to provide a **secure authentication system** and a **scalable web platform** for TTIO operations.

The system integrates a **Next.js (React) frontend**, a **FastAPI backend**, and a **cloud-hosted Azure SQL Database**, following real-world enterprise application architecture.

---

## 🌐 Live Website

👉 **View Live Application**  
https://ttioaccessinnovation.systems
 
👉 [https://ttioaccessinnovation.systems](https://ttioaccessinnovation.systems)


> Note: This project is deployed on a cloud platform. GitHub hosts the source code only.

---

## 🎯 Project Objectives

- Implement secure student and faculty authentication
- Replace hardcoded credentials with database-backed authentication
- Integrate frontend, backend, and cloud database
- Follow enterprise-level security practices
- Build a scalable foundation for future TTIO services

---

## 🛠️ Tech Stack

### Frontend
- Next.js (React)
- TypeScript
- Tailwind CSS

### Backend
- FastAPI (Python)
- RESTful APIs
- Argon2 password hashing

### Database
- Azure SQL Database

### Deployment
- Frontend: Vercel / Azure
- Backend: Azure
- Database: Azure SQL

---

## 📁 Project Structure

aip_bsu_ttio/
├── frontend/ # Next.js frontend
├── backend/ # FastAPI backend
├── README.md
└── .gitignore

yaml
Copy code

---

## 🔐 Authentication Flow

1. User opens the login page
2. User enters email and password
3. Frontend sends credentials to backend API
4. Backend queries Azure SQL Database
5. Password is verified using Argon2 hashing
6. Backend returns success or failure response
7. Frontend redirects user or displays an error

Passwords are **never stored or transmitted in plaintext**.

---

## 🚀 Running the Project Locally

### Backend (FastAPI)

```bash
cd backend
.\venv\Scripts\activate
python -m uvicorn main:app --reload
Backend URL:

cpp
Copy code
http://127.0.0.1:8000
Swagger API Docs:

arduino
Copy code
http://127.0.0.1:8000/docs
Frontend (Next.js)
bash
Copy code
cd frontend
npm install
npm run dev
Frontend URL:

arduino
Copy code
http://localhost:3000
🔒 Security Features
Argon2 password hashing

Backend-only database access

Parameterized SQL queries

CORS protection

No credentials stored in frontend

node_modules excluded from GitHub

🧪 Test Credentials (Development Only)
graphql
Copy code
Email: danielle.johnson@bowiestate.edu
Password: Bowie@123
⚠️ For testing and academic use only.

⭐ Key Highlights
Enterprise-style client–server architecture

Secure API-based authentication

Cloud-ready deployment

Clean separation of concerns

Scalable for future enhancements

🔮 Future Enhancements
JWT-based authentication

Role-based access control

Admin dashboard

Event and research management modules

Single Sign-On (SSO)

Audit logging and HTTPS enforcement
