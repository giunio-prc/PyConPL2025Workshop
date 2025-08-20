from collections.abc import Generator

from app.interfaces import AIAgentInterface, DatabaseManagerInterface


def add_content_into_db(db: DatabaseManagerInterface, content: str):
    db.add_text_to_db(content)


def query_agent(
    db: DatabaseManagerInterface, ai_agent: AIAgentInterface, question: str
) -> str:
    context = db.get_context(question)
    answer = ai_agent.query_with_context(question, context)
    return answer


def query_agent_with_stream_response(
    db: DatabaseManagerInterface, ai_agent: AIAgentInterface, question: str
) -> Generator[str, None]:

    context = db.get_context(question)
    for chunk in ai_agent.get_stream_response(question, context):
        yield chunk
