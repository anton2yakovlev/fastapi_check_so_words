import pytest
from httpx import ASGITransport, AsyncClient
from main import app


async def template(url: str, plural=False):
    json_key = "words" if plural else "word"
    expected_type = list if plural else str
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/" + url)
        assert response.status_code == 200
        assert json_key in response.json()
        assert isinstance(response.json()[json_key], expected_type)


@pytest.mark.asyncio
async def test_get_random_word():
    await template("get-so-word")


@pytest.mark.asyncio
async def test_get_random_host_word():
    await template("get-host-so-word")


@pytest.mark.asyncio
async def test_get_random_dvinyatin_word():
    await template("get-dvinyatin-so-word")


@pytest.mark.asyncio
async def test_get_all_words():
    await template("get-all-so-word", plural=True)


@pytest.mark.asyncio
async def test_get_all_host_words():
    await template("get-all-host-so-word", plural=True)


@pytest.mark.asyncio
async def test_get_all_dvinyatin_words():
    await template("get-all-dvinyatin-so-word", plural=True)


@pytest.mark.asyncio
async def test_docs_redirect():
    expected_content = 'Сервис для русских слов, оканчивающихся на "со"'
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
        assert response.status_code == 200, "Expected a 200 OK status code"
        assert (
            "text/html" in response.headers["content-type"]
        ), "Response content-type should be HTML"
        html_content = response.text
        assert (
            expected_content in html_content
        ), f"Expected content '{expected_content}' not found in the HTML response"
