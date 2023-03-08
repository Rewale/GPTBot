from loguru import logger

logger.add('logs/bot.log',
           format="{time} {level} {message}",
           rotation="1 MB",
           filter=lambda record: "bot_logger" in record["extra"],
           compression="tar.gz")

bot_logger = logger.bind(bot_logger=True)
