"""
AI Chat Router
Handles AI chat functionality with primary/fallback logic
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import os
import openai
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter()


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = None


class ChatResponse(BaseModel):
    message: str
    model_used: str


@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Chat with AI using primary/fallback logic
    Primary: Gemini -> Fallback: OpenRouter
    """
    try:
        # Convert messages to OpenAI format
        openai_messages = [
            {"role": msg.role, "content": msg.content}
            for msg in request.messages
        ]
        
        # Try Gemini first (would need Google AI client)
        # For now, use OpenAI as primary
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        if not openai.api_key:
            raise HTTPException(status_code=500, detail="No AI API key configured")
        
        response = openai.ChatCompletion.create(
            model=request.model or os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=openai_messages,
            max_tokens=1000,
            temperature=0.7
        )
        
        return ChatResponse(
            message=response.choices[0].message.content,
            model_used=response.model
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")


@router.get("/models")
async def get_available_models():
    """Get list of available AI models"""
    return {
        "models": [
            {"id": "gpt-3.5-turbo", "name": "GPT-3.5 Turbo", "provider": "OpenAI"},
            {"id": "gpt-4", "name": "GPT-4", "provider": "OpenAI"},
        ]
    }


@router.post("/search_wiki")
async def search_wiki(query: str, db: Session = Depends(get_db)):
    """AI function to search wiki notes"""
    # This would implement semantic search through vector database
    # For now, return placeholder
    return {"results": [], "query": query}


@router.post("/get_server_stats")
async def get_server_stats(db: Session = Depends(get_db)):
    """AI function to get server statistics"""
    # This would return current server stats
    return {"cpu": 0, "memory": 0, "disk": 0}