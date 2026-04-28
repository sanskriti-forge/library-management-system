# Library Management System

A RESTful API-based Library Management System built using Flask that allows efficient management of books and users with full CRUD functionality. The system is tested using Postman to ensure reliable API performance.

---

## Features

- Add new books to the library  
- View all available books  
- Update book details  
- Delete books from the system  
- Manage user data  
- RESTful API architecture  
- Tested using Postman for endpoint validation  

---

## Tech Stack

- Python  
- Flask  
- REST API  
- Postman  

---

## Project Structure

Library-Management-System/
│
├── app.py
├── models.py
├── routes.py
├── requirements.txt
└── README.md

---

## Installation & Setup

### 1. Clone the repository
git clone https://github.com/sanskriti-forge/library-management-system.git

### 2. Navigate to project directory
cd library-management-system

### 3. Create virtual environment (optional but recommended)
python -m venv venv

### 4. Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 5. Install dependencies
pip install -r requirements.txt

### 6. Run the application
python app.py

---

## API Endpoints

### Books

GET /books → Get all books  
POST /books → Add a new book  
PUT /books/<id> → Update book details  
DELETE /books/<id> → Delete a book  

### Users

GET /users → Get all users  
POST /users → Add a new user  

---

## Testing

All API endpoints were tested using Postman to ensure correct request handling and response accuracy.

---

## Learning Outcomes

- Understanding of RESTful API design  
- CRUD operations using Flask  
- API testing using Postman  
- Backend development fundamentals  

---

## Author

Sanskriti Bilgaiyan  
GitHub: https://github.com/sanskriti-forge  
