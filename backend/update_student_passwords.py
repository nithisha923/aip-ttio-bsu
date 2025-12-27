import pyodbc
from passlib.context import CryptContext

# ---------------------------
# CONFIG
# ---------------------------
TEMP_PASSWORD = "Bowie@123"

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

hashed_password = pwd_context.hash(TEMP_PASSWORD)

# ---------------------------
# DB CONNECTION
# ---------------------------
conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:<AZURE_SQL_SERVER>,1433;"
    "Database=<DATABASE_NAME>;"
    "Uid=<DB_USERNAME>;"
    "Pwd=<SET_VIA_ENVIRONMENT_VARIABLE>;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

cursor = conn.cursor()

# ---------------------------
# UPDATE
# ---------------------------
cursor.execute("""
    UPDATE dbo.student
    SET password_hash = ?
    WHERE password_hash IS NULL
       OR password_hash = 'TEMP_HASH'
""", hashed_password)

rows_updated = cursor.rowcount
conn.commit()

print(f"Password hashes updated for {rows_updated} students")

cursor.close()
conn.close()
