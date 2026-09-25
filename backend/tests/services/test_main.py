import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta, timezone
from backend.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Gestão de Redes API"}

@pytest.mark.asyncio
async def test_api_create_post_success():
    future_time = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    payload = { 
        "caption": "API test post",
        "media_url": "http://example.com/img.jpg",
        "platforms": ["instagram"],
        "scheduled_at": future_time
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/posts", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["status"] == "pending"
    assert data["caption"] == "API test post"

@pytest.mark.asyncio
async def test_api_create_post_invalid_date():
    past_time = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    payload = {
        "caption": "API test post past",
        "media_url": None,
        "platforms": ["twitter"],
        "scheduled_at": past_time
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/posts", json=payload)
    
    assert response.status_code == 400
    assert "Scheduled date and time must be in the future" in response.json()["detail"]
