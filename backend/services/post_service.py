from datetime import datetime, timezone
import uuid
from backend.schemas.post import PostCreate, PostResponse

class PostService:
    async def create_post(self, post_data: PostCreate) -> PostResponse:
        # Validate scheduled_at is in the future
        now = datetime.now(post_data.scheduled_at.tzinfo) if post_data.scheduled_at.tzinfo else datetime.now()
        if post_data.scheduled_at <= now:
            raise ValueError("Scheduled date and time must be in the future")
        
        # Return the created post with a unique ID and "pending" status
        return PostResponse(
            id=str(uuid.uuid4()),
            caption=post_data.caption,
            media_url=post_data.media_url,
            platforms=post_data.platforms,
            scheduled_at=post_data.scheduled_at,
            status="pending"
        )
