from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class PostCreate(BaseModel):
    caption: str = Field(..., description="The text caption of the post")
    media_url: Optional[str] = Field(None, description="Optional URL to media content")
    platforms: List[str] = Field(..., description="List of social media platforms to post to")
    scheduled_at: datetime = Field(..., description="The scheduled date and time for the post")

class PostResponse(BaseModel):
    id: str
    caption: str
    media_url: Optional[str]
    platforms: List[str]
    scheduled_at: datetime
    status: str
