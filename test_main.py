import pytest
from httpx import ASGITransport, AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_random_word():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/get-so-word")
        assert response.status_code == 200
        assert "word" in response.json()
        assert isinstance(response.json()["word"], str)

@pytest.mark.asyncio
async def test_get_random_host_word():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/get-host-so-word")
        assert response.status_code == 200
        assert "word" in response.json()
        assert isinstance(response.json()["word"], str)

@pytest.mark.asyncio
async def test_get_random_dvinyatin_word():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/get-dvinyatin-so-word")
        assert response.status_code == 200
        assert "word" in response.json()
        assert isinstance(response.json()["word"], str)
