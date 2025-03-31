from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from src.main import app

pytest_plugins = ["pytest_asyncio"]


@pytest.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient]:

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/api/v1",
    ) as client:
        yield client

    app.dependency_overrides = {}
