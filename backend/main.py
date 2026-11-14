
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

# Create FastAPI application
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class UserDetails(BaseModel):
    name: str
    email: EmailStr


# GET API - Health Check
@app.get("/api/health")
def health_check():
    return {
        "status": "API is working successfully"
    }


# POST API - Submit User Details
@app.post("/api/submit")
def submit_details(user: UserDetails):
    return {
        "message": "Details received successfully",
        "name": user.name,
        "email": user.email
    }
