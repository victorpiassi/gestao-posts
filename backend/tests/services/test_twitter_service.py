import pytest
import respx
from httpx import Response
from backend.services.twitter_service import TwitterService

@pytest.mark.asyncio
async def test_create_tweet_success(twitter_mock_data):
    """Tests successful tweet creation using mocked HTTP responses."""
    service = TwitterService()
    mock_response = twitter_mock_data["create_tweet"]
    
    with respx.mock as respx_mock:
        respx_mock.post("https://api.twitter.com/2/tweets").mock(
            return_value=Response(201, json=mock_response)
        )
        
        result = await service.create_tweet("This is a mock tweet caption!")
        assert result == mock_response
        assert result["data"]["id"] == "1234567890123456789"

@pytest.mark.asyncio
async def test_delete_tweet_success(twitter_mock_data):
    """Tests successful tweet deletion using mocked HTTP responses."""
    service = TwitterService()
    mock_response = twitter_mock_data["delete_tweet"]
    tweet_id = "1234567890123456789"
    
    with respx.mock as respx_mock:
        respx_mock.delete(f"https://api.twitter.com/2/tweets/{tweet_id}").mock(
            return_value=Response(200, json=mock_response)
        )
        
        result = await service.delete_tweet(tweet_id)
        assert result == mock_response
        assert result["data"]["deleted"] is True

@pytest.mark.asyncio
async def test_get_tweet_metrics_success(twitter_mock_data):
    """Tests successful retrieval of tweet metrics using mocked HTTP responses."""
    service = TwitterService()
    mock_response = twitter_mock_data["get_tweet_metrics"]
    tweet_id = "1234567890123456789"
    
    with respx.mock as respx_mock:
        respx_mock.get(f"https://api.twitter.com/2/tweets/{tweet_id}").mock(
            return_value=Response(200, json=mock_response)
        )
        
        result = await service.get_tweet_metrics(tweet_id)
        assert result == mock_response
        assert result["data"]["public_metrics"]["like_count"] == 85
