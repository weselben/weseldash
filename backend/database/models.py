"""
Database models for Personal Dashboard
"""

from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base


class User(Base):
    """User model for authentication and preferences"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class WikiNote(Base):
    """Wiki/Digital Garden notes"""
    __tablename__ = "wiki_notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=False)
    tags = Column(String(500))  # JSON string of tags
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class Bookmark(Base):
    """Wayback bookmark manager"""
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(2000), nullable=False)
    title = Column(String(500))
    description = Column(Text)
    snapshot_path = Column(String(500))  # Path to HTML snapshot
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class RSSFeed(Base):
    """RSS Feed subscriptions"""
    __tablename__ = "rss_feeds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    url = Column(String(2000), nullable=False)
    description = Column(Text)
    last_updated = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class RSSItem(Base):
    """RSS Feed items"""
    __tablename__ = "rss_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    link = Column(String(2000))
    description = Column(Text)
    pub_date = Column(DateTime(timezone=True))
    guid = Column(String(500), unique=True, index=True)
    is_read = Column(Boolean, default=False)
    feed_id = Column(Integer, ForeignKey("rss_feeds.id"))
    
    feed = relationship("RSSFeed")


class MediaLog(Base):
    """Media consumption tracking"""
    __tablename__ = "media_logs"

    id = Column(Integer, primary_key=True, index=True)
    media_type = Column(String(50), nullable=False)  # book, movie, music, etc.
    title = Column(String(500), nullable=False)
    creator = Column(String(200))  # author, director, artist
    status = Column(String(50))  # completed, in_progress, planned
    rating = Column(Float)
    notes = Column(Text)
    started_date = Column(DateTime(timezone=True))
    completed_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class Habit(Base):
    """Habit tracking"""
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    frequency = Column(String(50))  # daily, weekly, monthly
    target_count = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class HabitLog(Base):
    """Habit completion tracking"""
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    completed_at = Column(DateTime(timezone=True), server_default=func.now())
    count = Column(Integer, default=1)
    notes = Column(Text)
    
    habit = relationship("Habit")


class DailyJournal(Base):
    """AI-generated daily journal entries"""
    __tablename__ = "daily_journals"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), nullable=False, index=True)
    content = Column(Text, nullable=False)
    mood_score = Column(Float)
    activity_summary = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class SystemStats(Base):
    """System monitoring data"""
    __tablename__ = "system_stats"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(100), nullable=False)
    cpu_percent = Column(Float)
    memory_percent = Column(Float)
    disk_percent = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


class Subscription(Base):
    """Subscription tracking"""
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    cost = Column(Float, nullable=False)
    billing_cycle = Column(String(50))  # monthly, yearly, etc.
    next_billing_date = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))


class InventoryItem(Base):
    """Home inventory management"""
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100))
    description = Column(Text)
    purchase_date = Column(DateTime(timezone=True))
    purchase_price = Column(Float)
    warranty_until = Column(DateTime(timezone=True))
    location = Column(String(200))
    photo_path = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))