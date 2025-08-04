"""
Personal Dashboard Backend
FastAPI application for managing personal data and integrations
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers (will be created)
from routers import ai_chat, knowledge, analytics, system

# Database imports
from database.database import engine, Base
from database.models import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    print("🚀 Starting Personal Dashboard Backend...")
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    print("📊 Database tables created/verified")
    
    # Initialize vector database
    os.makedirs(os.getenv("VECTOR_DB_PATH", "/data/vectordb"), exist_ok=True)
    print("🔍 Vector database initialized")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Personal Dashboard Backend...")


# Create FastAPI app
app = FastAPI(
    title="Personal Dashboard API",
    description="A self-hosted personal hub for managing digital life",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ai_chat.router, prefix="/api/ai", tags=["AI Chat"])
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["Knowledge Management"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Personal Analytics"])
app.include_router(system.router, prefix="/api/system", tags=["System Management"])

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "personal-dashboard-backend",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Personal Dashboard API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("BACKEND_HOST", "0.0.0.0"),
        port=int(os.getenv("BACKEND_PORT", 8000)),
        reload=os.getenv("DEBUG", "false").lower() == "true"
    )