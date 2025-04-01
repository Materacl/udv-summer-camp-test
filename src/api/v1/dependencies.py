import json
from typing import Annotated

from aiofiles import open as aioopen
from fastapi import Depends, HTTPException


async def load_json(filename: str):
    try:
        async with aioopen(filename, encoding="utf-8") as f:
            return json.loads(await f.read())
    except (FileNotFoundError, json.JSONDecodeError) as err:
        raise HTTPException(status_code=500, detail="Failed to load json") from err


async def get_db() -> dict:
    data_news = await load_json("src/db/news.json")
    data_comments = await load_json("src/db/comments.json")
    return {"news": data_news, "comments": data_comments}


DB = Annotated[dict, Depends(get_db)]
