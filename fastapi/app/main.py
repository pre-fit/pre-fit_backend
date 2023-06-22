from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

# from . import config
import sys
sys.path.append('/home/ubuntu/fastapi/fastapi')
from settings import settings

app = FastAPI()


@lru_cache()
def get_settings():
    return settings


@app.get("/info")
async def info(settings: Annotated[type(settings), Depends(get_settings)]):
    return {
        "db_host": settings.db_host,
        "db_port": settings.db_port,
        "db_base": settings.db_base,
    }
