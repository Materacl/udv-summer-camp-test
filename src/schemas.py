from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class Comment(BaseModel):
    id: Annotated[int, Field(gt=0)]
    news_id: Annotated[int, Field(gt=0)]
    title: Annotated[str, Field(max_length=255)]
    date: datetime
    comment: Annotated[str, Field(max_length=1000)]


class NewsItem(BaseModel):
    id: Annotated[int, Field(gt=0)]
    title: Annotated[str, Field(max_length=255)]
    date: datetime
    body: Annotated[str, Field(max_length=5000)]
    deleted: bool
    comments_count: Annotated[int, Field(ge=0)]


class NewsItemWithComments(NewsItem):
    comments: list[Comment]


class NewsResponse(BaseModel):
    news: list[NewsItem]
    news_count: Annotated[int, Field(ge=0)]
