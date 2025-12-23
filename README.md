# secure-user-profile
A secure full-stack identity management system built with Flask, React, and MySQL. Implements JWT-based authentication and AES-256 encryption to protect sensitive user data.

Project Overview
This project implements a secure identity management microservice that allows users to register, authenticate, and view their profile. Sensitive user information (Aadhaar/ID number) is encrypted at rest and decrypted only for authenticated access.
The system is built as a full-stack application using:
	•	Python (Flask) for backend APIs
	•	MySQL for persistent storage
	•	React.js for frontend UI
	•	JWT (JSON Web Tokens) for stateless authentication
	•	AES-256 encryption for sensitive fields
This project fulfills Assignment 1 – Secure User Profile & Access Control System as specified in the provided assignment document.

🏗️ Architecture Overview

React Frontend  →  Flask Backend  →  MySQL Database
     (JWT)           (AES)            (Encrypted Data)

🛠️ Technology Stack
Backend
	•	Python 3
	•	Flask
	•	Flask-JWT-Extended
	•	Flask-SQLAlchemy
	•	Flask-CORS
	•	PyMySQL
	•	Cryptography (AES-256)
	•	bcrypt
Frontend
	•	React.js
	•	Axios
	•	React Scripts
Database
	•	MySQL 8+
