from collections.abc import Generator
from pathlib import Path

import pytest

from app.agents import FakeAgent
from app.databases import FakeDatabase

data_location = Path(__file__).parent / "data"

@pytest.fixture
def fake_database() -> Generator[FakeDatabase]:
    database = FakeDatabase()
    yield database
    database.empty_database()

@pytest.fixture
def fake_agent() -> FakeAgent:
    agent = FakeAgent()
    return agent
