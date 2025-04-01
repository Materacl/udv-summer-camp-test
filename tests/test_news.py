import pytest
from fastapi import status
from httpx import AsyncClient

EXPECTED_NEWS_COUNT = 2
NEWS_1_ID = 1
NEWS_1_COMMENT_COUNT = 2
NEWS_3_ID = 3
NEWS_3_COMMENT_COUNT = 1


# --- Tests for GET /news/ ---
@pytest.mark.asyncio
async def test_get_news_success(client: AsyncClient):
    response = await client.get("/news/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Verify only non-deleted news are returned
    assert data["news_count"] == EXPECTED_NEWS_COUNT
    assert len(data["news"]) == EXPECTED_NEWS_COUNT
    assert data["news"][0]["id"] == NEWS_1_ID
    assert data["news"][1]["id"] == NEWS_3_ID

    # Verify comment counts
    assert data["news"][0]["comments_count"] == NEWS_1_COMMENT_COUNT
    assert data["news"][1]["comments_count"] == NEWS_3_COMMENT_COUNT


# --- Tests for GET /news/{news_id} ---
@pytest.mark.asyncio
async def test_get_news_by_id_success(client: AsyncClient):
    response = await client.get(f"/news/news/{NEWS_1_ID}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["id"] == NEWS_1_ID
    assert data["title"] == "News 1"
    assert len(data["comments"]) == NEWS_1_COMMENT_COUNT
    assert data["comments_count"] == NEWS_1_COMMENT_COUNT


@pytest.mark.asyncio
async def test_get_news_by_id_not_found(client: AsyncClient):
    # Test non-existent ID
    response = await client.get("/news/news/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "News not found"

    # Test deleted news
    response = await client.get("/news/news/2")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "News not found"
