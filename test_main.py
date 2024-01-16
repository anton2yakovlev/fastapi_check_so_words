import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_read_random_word():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-so-word")
    assert response.status_code == 200
    assert "word" in response.json()
