from fastapi import FastAPI, Depends
from pwdlib import PasswordHash
from database import get_db
from sqlalchemy import text
from routes import router
app= FastAPI()
app.include_router(router)

@app.get("/")
def test(test_db = Depends(get_db)):
    result = test_db.execute(text("Select 1"))
    value= result.scalar()
    print(value)
    return {"result":value}