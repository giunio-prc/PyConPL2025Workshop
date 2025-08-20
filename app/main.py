import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TypedDict

from fastapi import FastAPI

from app.agents import FakeAgent
from app.api import database, prompting
from app.databases import FakeDatabase
from app.interfaces import AIAgentInterface, DatabaseManagerInterface

logger = logging.getLogger(__name__)


class State(TypedDict):
    db: DatabaseManagerInterface
    agent: AIAgentInterface


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    yield {"db": FakeDatabase(), "agent": FakeAgent()}


app = FastAPI(title="AI RAG Assistant", lifespan=lifespan)

# Include API routers
app.include_router(database.router)
app.include_router(prompting.router)
