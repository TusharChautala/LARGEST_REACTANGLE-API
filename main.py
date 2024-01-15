# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
import datetime
import time

# Define MatrixRequest directly in main.py
class MatrixRequest(BaseModel):
    matrix: List[List[int]]

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "log_entries"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    matrix_request = Column(String)
    result = Column(String)
    turnaround_time = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ... (rest of the code)


# Your largest_rectangle function
# def largest_rectangle(matrix: List[List[int]]) -> tuple:
#     # Your implementation here
#     # ...

# Include the route to handle the POST request
# main.py

# ... (previous code)

@app.post("/largest_rectangle")
async def largest_rectangle_endpoint(matrix_request: MatrixRequest) -> dict:
    start_time = time.time()
    try:
        result = largest_rectangle(matrix_request.matrix)

        # Use a session to interact with the database
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = Session()

        # Log the request, response, and turnaround time in the database
        log_entry = LogEntry(
            matrix_request=str(matrix_request.matrix),
            result=str(result),
            turnaround_time=time.time() - start_time
        )
        db.add(log_entry)
        db.commit()
        db.close()

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# # Include this startup event to connect to the database during application startup
# @app.on_event("startup")
# async def startup():
#     pass

# # Include this shutdown event to disconnect from the database during application shutdown
# @app.on_event("shutdown")
# async def shutdown():
#     pass
