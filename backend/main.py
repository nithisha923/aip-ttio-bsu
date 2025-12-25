from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc

from auth import verify_password

app = FastAPI(title="AIP Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------
# DB CONNECTION STRING
# ---------------------------
CONN_STR = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:<AZURE_SQL_SERVER>,1433;"
    "Database=<DATABASE_NAME>;"
    "Uid=<DB_USERNAME>;"
    "Pwd=<SET_VIA_ENVIRONMENT_VARIABLE>;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# ---------------------------
# REQUEST MODEL
# ---------------------------
class LoginRequest(BaseModel):
    email: str
    password: str


@app.get("/")
def root():
    return {"status": "Backend is running"}


@app.post("/login")
def login(data: LoginRequest):
    conn = pyodbc.connect(CONN_STR)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM dbo.student WHERE email = ?",
        data.email
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    password_hash = row[0]

    if not verify_password(data.password, password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "email": data.email
    }
