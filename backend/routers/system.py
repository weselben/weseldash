"""
System Management Router
Handles system stats, subscriptions, and inventory management
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import SystemStats, Subscription, InventoryItem

router = APIRouter()


# Pydantic models
class SystemStatsCreate(BaseModel):
    hostname: str
    cpu_percent: float
    memory_percent: float
    disk_percent: float


class SubscriptionCreate(BaseModel):
    name: str
    cost: float
    billing_cycle: str
    next_billing_date: datetime
    notes: Optional[str] = None


class InventoryItemCreate(BaseModel):
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    purchase_date: Optional[datetime] = None
    purchase_price: Optional[float] = None
    warranty_until: Optional[datetime] = None
    location: Optional[str] = None


# System Stats endpoints
@router.post("/stats")
async def submit_system_stats(stats: SystemStatsCreate, db: Session = Depends(get_db)):
    """Submit system statistics from monitoring client"""
    db_stats = SystemStats(**stats.dict())
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats


@router.get("/stats")
async def get_system_stats(
    hostname: Optional[str] = None,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get system statistics"""
    query = db.query(SystemStats)
    
    if hostname:
        query = query.filter(SystemStats.hostname == hostname)
    
    stats = query.order_by(SystemStats.timestamp.desc()).limit(limit).all()
    return stats


@router.get("/stats/latest")
async def get_latest_stats(db: Session = Depends(get_db)):
    """Get latest system stats for all hosts"""
    # Get latest stats for each unique hostname
    from sqlalchemy import func
    
    subquery = db.query(
        SystemStats.hostname,
        func.max(SystemStats.timestamp).label('max_timestamp')
    ).group_by(SystemStats.hostname).subquery()
    
    latest_stats = db.query(SystemStats).join(
        subquery,
        (SystemStats.hostname == subquery.c.hostname) &
        (SystemStats.timestamp == subquery.c.max_timestamp)
    ).all()
    
    return latest_stats


# Subscription endpoints
@router.post("/subscriptions")
async def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    """Create a new subscription"""
    db_subscription = Subscription(**subscription.dict(), user_id=1)  # TODO: Get from auth
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


@router.get("/subscriptions")
async def get_subscriptions(active_only: bool = True, db: Session = Depends(get_db)):
    """Get all subscriptions"""
    query = db.query(Subscription)
    if active_only:
        query = query.filter(Subscription.is_active == True)
    
    subscriptions = query.order_by(Subscription.next_billing_date).all()
    return subscriptions


@router.put("/subscriptions/{subscription_id}")
async def update_subscription(
    subscription_id: int,
    subscription_update: SubscriptionCreate,
    db: Session = Depends(get_db)
):
    """Update a subscription"""
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    for field, value in subscription_update.dict().items():
        setattr(db_subscription, field, value)
    
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


@router.delete("/subscriptions/{subscription_id}")
async def cancel_subscription(subscription_id: int, db: Session = Depends(get_db)):
    """Cancel/deactivate a subscription"""
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    db_subscription.is_active = False
    db.commit()
    return {"message": "Subscription cancelled successfully"}


# Inventory endpoints
@router.post("/inventory")
async def create_inventory_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    """Add a new inventory item"""
    db_item = InventoryItem(**item.dict(), user_id=1)  # TODO: Get from auth
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/inventory")
async def get_inventory_items(
    category: Optional[str] = None,
    location: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get inventory items with optional filtering"""
    query = db.query(InventoryItem)
    
    if category:
        query = query.filter(InventoryItem.category == category)
    if location:
        query = query.filter(InventoryItem.location == location)
    
    items = query.order_by(InventoryItem.created_at.desc()).all()
    return items


@router.get("/inventory/categories")
async def get_inventory_categories(db: Session = Depends(get_db)):
    """Get unique inventory categories"""
    from sqlalchemy import distinct
    
    categories = db.query(distinct(InventoryItem.category)).filter(
        InventoryItem.category.isnot(None)
    ).all()
    
    return [cat[0] for cat in categories if cat[0]]


@router.get("/inventory/locations")
async def get_inventory_locations(db: Session = Depends(get_db)):
    """Get unique inventory locations"""
    from sqlalchemy import distinct
    
    locations = db.query(distinct(InventoryItem.location)).filter(
        InventoryItem.location.isnot(None)
    ).all()
    
    return [loc[0] for loc in locations if loc[0]]


@router.put("/inventory/{item_id}")
async def update_inventory_item(
    item_id: int,
    item_update: InventoryItemCreate,
    db: Session = Depends(get_db)
):
    """Update an inventory item"""
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    
    for field, value in item_update.dict().items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/inventory/{item_id}")
async def delete_inventory_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an inventory item"""
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Inventory item deleted successfully"}