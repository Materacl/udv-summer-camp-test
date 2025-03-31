from pydantic import BaseModel, Field
from typing import List

class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: str
    comment: str

class NewsItem(BaseModel):
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments_count: int = Field(default=0)

class NewsItemWithComments(NewsItem):
    comments: List[Comment] = Field(default_factory=list)

class NewsResponse(BaseModel):
    news: List[NewsItem]
    news_count: int