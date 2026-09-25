import logging
import httpx
from typing import Any, Dict, List, Optional
from backend.config import settings

logger = logging.getLogger(__name__)

class TwitterService:
    """Service to handle interactions with the X (Twitter) API v2."""

    def __init__(self, client: Optional[httpx.AsyncClient] = None) -> None:
        self.client = client or httpx.AsyncClient()
        self.base_url = "https://api.twitter.com/2"

    async def create_tweet(self, text: str, media_ids: Optional[List[str]] = None) -> Dict[str, Any]:
        """Publishes a new tweet to X.

        Args:
            text: The text content of the tweet.
            media_ids: Optional list of pre-uploaded media IDs.

        Returns:
            Dict containing the API response data.
        """
        url = f"{self.base_url}/tweets"
        headers = {
            "Authorization": f"Bearer {settings.X_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
        payload: Dict[str, Any] = {"text": text}
        if media_ids:
            payload["media"] = {"media_ids": media_ids}

        try:
            response = await self.client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Twitter API error during tweet creation: {e.response.text}")
            raise e

    async def delete_tweet(self, tweet_id: str) -> Dict[str, Any]:
        """Deletes an existing tweet from X.

        Args:
            tweet_id: The unique identifier of the tweet to delete.

        Returns:
            Dict containing the API response data.
        """
        url = f"{self.base_url}/tweets/{tweet_id}"
        headers = {
            "Authorization": f"Bearer {settings.X_BEARER_TOKEN}"
        }
        try:
            response = await self.client.delete(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Twitter API error during tweet deletion: {e.response.text}")
            raise e

    async def get_tweet_metrics(self, tweet_id: str) -> Dict[str, Any]:
        """Retrieves engagement metrics for a specific tweet.

        Args:
            tweet_id: The unique identifier of the tweet.

        Returns:
            Dict containing the public and non-public metrics.
        """
        url = f"{self.base_url}/tweets/{tweet_id}"
        headers = {
            "Authorization": f"Bearer {settings.X_BEARER_TOKEN}"
        }
        params = {
            "tweet.fields": "public_metrics,non_public_metrics,organic_metrics"
        }
        try:
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Twitter API error during fetching metrics: {e.response.text}")
            raise e
