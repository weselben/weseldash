"""
Knowledge Management Router
Handles RSS feeds, wiki notes, and bookmark management
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import WikiNote, RSSFeed, RSSItem, Bookmark

router = APIRouter()


# Pydantic models
class WikiNoteCreate(BaseModel):
    title: str
    content: str
    tags: Optional[str] = None


class WikiNoteResponse(BaseModel):
    id: int
    title: str
    content: str
    tags: Optional[str] = None
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True


class RSSFeedCreate(BaseModel):
    name: str
    url: str
    description: Optional[str] = None


class BookmarkCreate(BaseModel):
    url: str
    title: Optional[str] = None
    description: Optional[str] = None


# Wiki endpoints
@router.post("/wiki/notes", response_model=WikiNoteResponse)
async def create_wiki_note(note: WikiNoteCreate, db: Session = Depends(get_db)):
    """Create a new wiki note"""
    db_note = WikiNote(**note.dict(), user_id=1)  # TODO: Get from auth
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("/wiki/notes", response_model=List[WikiNoteResponse])
async def get_wiki_notes(db: Session = Depends(get_db)):
    """Get all wiki notes"""
    notes = db.query(WikiNote).all()
    return notes


@router.get("/wiki/notes/{note_id}", response_model=WikiNoteResponse)
async def get_wiki_note(note_id: int, db: Session = Depends(get_db)):
    """Get a specific wiki note"""
    note = db.query(WikiNote).filter(WikiNote.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/wiki/notes/{note_id}", response_model=WikiNoteResponse)
async def update_wiki_note(note_id: int, note_update: WikiNoteCreate, db: Session = Depends(get_db)):
    """Update a wiki note"""
    db_note = db.query(WikiNote).filter(WikiNote.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    for field, value in note_update.dict().items():
        setattr(db_note, field, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note


@router.delete("/wiki/notes/{note_id}")
async def delete_wiki_note(note_id: int, db: Session = Depends(get_db)):
    """Delete a wiki note"""
    db_note = db.query(WikiNote).filter(WikiNote.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted successfully"}


# RSS endpoints
@router.post("/rss/feeds")
async def create_rss_feed(feed: RSSFeedCreate, db: Session = Depends(get_db)):
    """Subscribe to a new RSS feed"""
    db_feed = RSSFeed(**feed.dict(), user_id=1)  # TODO: Get from auth
    db.add(db_feed)
    db.commit()
    db.refresh(db_feed)
    return db_feed


@router.get("/rss/feeds")
async def get_rss_feeds(db: Session = Depends(get_db)):
    """Get all RSS feeds"""
    feeds = db.query(RSSFeed).all()
    return feeds


@router.get("/rss/items")
async def get_rss_items(feed_id: Optional[int] = None, db: Session = Depends(get_db)):
    """Get RSS items, optionally filtered by feed"""
    query = db.query(RSSItem)
    if feed_id:
        query = query.filter(RSSItem.feed_id == feed_id)
    items = query.order_by(RSSItem.pub_date.desc()).limit(50).all()
    return items


# Bookmark endpoints
@router.post("/bookmarks")
async def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    """Create a new bookmark and capture snapshot"""
    # TODO: Implement HTML snapshot capture
    db_bookmark = Bookmark(**bookmark.dict(), user_id=1)  # TODO: Get from auth
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark


@router.get("/bookmarks")
async def get_bookmarks(db: Session = Depends(get_db)):
    """Get all bookmarks"""
    bookmarks = db.query(Bookmark).all()
    return bookmarks


@router.post("/wiki/search")
async def search_wiki_notes(query: str, db: Session = Depends(get_db)):
    """Search wiki notes (semantic search would go here)"""
    # For now, simple text search
    notes = db.query(WikiNote).filter(
        WikiNote.title.contains(query) | WikiNote.content.contains(query)
    ).all()
    return notes