from collections.abc import Generator

from app.controller.controller import (
    query_agent_with_stream_response,
)
from tests.conftest import data_location


def test_load_initial_documents__load_chunks_from_file_in_folder(fake_database):
    fake_database.load_documents_from_folder(data_location)

    chunks = fake_database.get_chunks()

    assert len(chunks) == 18
    expected_content_chunk = (
        "Little Steps Baby Shop\nCustomer Q&A (Short Version)\n"
        + "Format: .txt\nLast updated: June 2025\n"
        + "1. Products and Safety"
    )

    assert expected_content_chunk in chunks


def test_controller__can_stream_from_fake_agent(fake_database, fake_agent):
    streaming_response_generator = query_agent_with_stream_response(fake_database, fake_agent, "What time is it?")
    assert isinstance(streaming_response_generator, Generator)
    response = [chunk for chunk in streaming_response_generator]
    assert len(response) == 196
    assert response[0] == "Y"
