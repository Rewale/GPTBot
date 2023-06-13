import dataclasses
from typing import List
from unittest.mock import patch

import pytest

from src.repo import GPTRepo


@dataclasses.dataclass
class MessageMock:
    content: str


@dataclasses.dataclass
class MockChoice:
    message: MessageMock


@dataclasses.dataclass
class MockResponseGPT:
    choices: List[MockChoice]


def _create_choice(content: str):
    return MockChoice(message=MessageMock(content=content))


def _create_response(answers: List[str]):
    return MockResponseGPT(choices=[_create_choice(x) for x in answers])


@pytest.fixture(scope='function')
def gpt_repo():
    return GPTRepo('test')


def test_simple_message(gpt_repo):
    question = "test question"
    answers = ['123\n', '456\n', '789\n']
    message = "123\n456\n789\n"
    with patch('openai.ChatCompletion.create') as createRequest:
        createRequest.return_value = _create_response(answers)
        got_message = gpt_repo.ask(question)

        assert message == got_message
