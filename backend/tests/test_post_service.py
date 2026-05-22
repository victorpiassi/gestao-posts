import pytest
from datetime import datetime, timedelta, timezone
from backend.schemas.post import PostCreate
from backend.services.post_service import PostService

@pytest.mark.asyncio
async def test_create_post_success():
    service = PostService()
    future_time = datetime.now(timezone.utc) + timedelta(days=1)
    post_data = PostCreate(
        caption="My first scheduled post!",
        media_url="https://example.com/image.png",
        platforms=["instagram", "linkedin"],
        scheduled_at=future_time
    )
    
    response = await service.create_post(post_data)
    
    assert response.id is not None
    assert response.status == "pending"
    assert response.caption == post_data.caption
    assert response.platforms == post_data.platforms
    assert response.scheduled_at == post_data.scheduled_at

@pytest.mark.asyncio
async def test_create_post_past_date_raises_value_error():
    service = PostService()
    past_time = datetime.now(timezone.utc) - timedelta(days=1)
    post_data = PostCreate(
        caption="This should fail",
        media_url=None,
        platforms=["twitter"],
        scheduled_at=past_time
    )
    
    with pytest.raises(ValueError, match="Scheduled date and time must be in the future"):
        await service.create_post(post_data)
