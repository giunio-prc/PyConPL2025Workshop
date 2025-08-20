from collections.abc import Iterator
from random import random
from time import sleep

from app.interfaces.agent import AIAgentInterface


class FakeAgent(AIAgentInterface):

    def query_with_context(self, question: str, context: str) -> str:
        return (
            f'You asked me the following question:\n "{question}" \n'
            f'With the following context "{context}"\n'
            "Unfortunately I am a fake agent I am not able to answer you"
        )

    def get_stream_response(
        self, question: str, context: str
        ) -> Iterator[str]:

        char_sleep = 5.0 / len(f"{context}{question}")
        phrase_sleep = char_sleep * 2

        for char in "You asked me the following question:\n":
            sleep(char_sleep * random())
            yield char

        sleep(phrase_sleep * random())

        for char in f'"{question}" \n':
            sleep(char_sleep * random())
            yield char

        sleep(phrase_sleep * random())


        for char in f'With the following context "{context}"\n':
            sleep(char_sleep * random())
            yield char

        sleep(phrase_sleep * random())

        for char in "Unfortunately I am a fake agent I am not able to answer you":
            sleep(char_sleep * random())
            yield char
