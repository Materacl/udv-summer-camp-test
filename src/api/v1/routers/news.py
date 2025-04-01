from fastapi import APIRouter, HTTPException

from src import schemas
from src.api.v1 import dependencies

router = APIRouter(prefix="/news", tags=["news"])


@router.get(
    "/",
    response_model=schemas.NewsResponse,
    responses={200: {"description": "News retrieved successfully"}},
)
async def get_news(db: dependencies.DB):
    comments_count = {item["news_id"]: 0 for item in db["comments"]["comments"]}
    for comment in db["comments"]["comments"]:
        comments_count[comment["news_id"]] += 1

    filtered_news = [
        schemas.NewsItem(**news, comments_count=comments_count.get(news["id"], 0))
        for news in db["news"]["news"]
        if not news["deleted"]
    ]

    return schemas.NewsResponse(news=filtered_news, news_count=len(filtered_news))


@router.get(
    "/news/{news_id}",
    response_model=schemas.NewsItemWithComments,
    responses={
        200: {"description": "News retrieved successfully"},
        404: {"description": "News not found"},
    },
)
async def get_news_by_id(news_id: int, db: dependencies.DB):
    news_item = next(
        (news for news in db["news"]["news"] if news["id"] == news_id), None
    )
    if not news_item or news_item["deleted"]:
        raise HTTPException(status_code=404, detail="News not found")

    news_comments = [
        schemas.Comment(**comment)
        for comment in db["comments"]["comments"]
        if comment["news_id"] == news_id
    ]

    return schemas.NewsItemWithComments(
        **news_item, comments=news_comments, comments_count=len(news_comments)
    )
