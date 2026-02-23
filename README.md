# 💳 Payment Transactions API

Backend API for managing payment transactions, built with FastAPI and SQLAlchemy.

This project simulates a simplified fintech backend system with transaction management, pagination, filtering, and structured architecture.

---

## 🚀 Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📦 Features

- Create transactions
- Retrieve transactions
- Update transactions (PATCH)
- Delete transactions
- Pagination support
- Filter by status
- Structured layered architecture
- Input validation with Pydantic
- Clean RESTful design

---

## 📁 Project Structure

```text
app/
│
├── main.py
├── database.py
│
├── models/
│   └── transaction.py
│
├── routes/
│   └── transactions.py
│
└── schemas/
    └── transaction.py
```

## 📊 Pagination Example

```
GET /transactions?page=1&limit=10
```

Response:

```json
{
  "total": 25,
  "page": 1,
  "limit": 10,
  "total_pages": 3,
  "data": [...]
}
```

## 🔎 Filtering Example

```
GET /transactions?status=approved&page=1&limit=5
```

## 🛠️ How to Run

1) Clone the repository:

```bash
git clone <repo-url>
```

2) Create virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3) Install dependencies:

```bash
pip install -r requirements.txt
```

4) Run server:

```bash
uvicorn app.main:app --reload
```

5) Server will run on:

```
http://127.0.0.1:8000
```

6) Swagger documentation available at:

```
http://127.0.0.1:8000/docs
```

## 🎯 Purpose

This project was built to:

- Strengthen backend architecture skills
- Implement RESTful APIs
- Apply pagination and filtering patterns
- Prepare for fullstack fintech-oriented systems

## 🔜 Next Steps

- Migrate to PostgreSQL
- Add authentication (JWT)
- Deploy with Docker
- Connect to frontend dashboard (Next.js)


