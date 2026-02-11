from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

@app.get("/payments")
def get_payments():
    return [
        {"id": 1, "amount": 100, "status": "completed"},
        {"id": 2, "amount": 250, "status": "pending"}
    ]

