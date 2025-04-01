from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from src.api.v1 import dependencies
from src.main import app

pytest_plugins = ["pytest_asyncio"]


TEST_NEWS = {
    "news": [
        {
            "id": 1,
            "title": "News 1",
            "date": "2023-01-01",
            "body": "Content 1",
            "deleted": False,
        },
        {
            "id": 2,
            "title": "News 2",
            "date": "2023-01-02",
            "body": "Content 2",
            "deleted": True,
        },
        {
            "id": 3,
            "title": "News 3",
            "date": "2023-01-03",
            "body": "Content 3",
            "deleted": False,
        },
    ]
}

TEST_COMMENTS = {
    "comments": [
        {
            "id": 1,
            "news_id": 1,
            "title": "Comment 1",
            "date": "2023-01-01",
            "comment": "Text 1",
        },
        {
            "id": 2,
            "news_id": 1,
            "title": "Comment 2",
            "date": "2023-01-02",
            "comment": "Text 2",
        },
        {
            "id": 3,
            "news_id": 3,
            "title": "Comment 3",
            "date": "2023-01-03",
            "comment": "Text 3",
        },
    ]
}


@pytest.fixture(autouse=True)
def override_db_dependency():
    def mock_db():
        return {"news": TEST_NEWS, "comments": TEST_COMMENTS}

    app.dependency_overrides[dependencies.get_db] = mock_db
    yield
    app.dependency_overrides = {}


@pytest.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient]:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/api/v1",
    ) as client:
        yield client
