import os
from dataclasses import dataclass
from typing import List

from environs import Env

__abs_path_dir = os.path.dirname(os.path.abspath(__file__))
schedule_xlsx_dir_path = os.path.join(__abs_path_dir, "schedules_xlsx")


@dataclass
class DbConfig:
    host: str
    port: int


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class GPTBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous
    gpt: GPTBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        misc=Miscellaneous(),
        gpt=GPTBot(token=env.str('GPT_TOKEN'))
    )
