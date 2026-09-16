import json
import os
import pytest

@pytest.fixture
def twitter_mock_data():
    path = os.path.join(os.path.dirname(__file__), "../mocks/twitter.json")
    with open(path, "r") as f:
        return json.load(f)

@pytest.fixture
def instagram_mock_data():
    path = os.path.join(os.path.dirname(__file__), "../mocks/instagram.json")
    with open(path, "r") as f:
        return json.load(f)

@pytest.fixture
def openai_mock_data():
    path = os.path.join(os.path.dirname(__file__), "../mocks/openai.json")
    with open(path, "r") as f:
        return json.load(f)
