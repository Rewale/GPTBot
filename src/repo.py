import abc

import openai


class IGPTRepo(abc.ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abc.abstractmethod
    def ask(self, question: str) -> str:
        pass


class GPTRepo(IGPTRepo):
    def ask(self, question: str) -> str:
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question},
            ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content

        return result
