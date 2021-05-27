# -*- coding: utf-8 -*-

from random import randint
import logging
import os
import settings
import vk_api
from vk_api import bot_longpoll


# TODO параметр не должен быть подчеркнут
def configure_logging(logger):
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    date_time_format = "%d %m %Y, %H:%M"
    file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt=date_time_format)
    logging_path = "chatbot_logs"
    if not os.path.exists(logging_path):
        os.mkdir(logging_path)

    logging_debug_path = os.path.join(logging_path, "chatbot_debug_log.log")
    file_debug_handler = logging.FileHandler(logging_debug_path, "a", encoding="utf-8", delay=True)
    file_debug_handler.setLevel(logging.DEBUG)
    file_debug_handler.setFormatter(file_formatter)
    logger.addHandler(file_debug_handler)

    logging_info_path = os.path.join(logging_path, "chatbot_info_log.log")
    file_info_handler = logging.FileHandler(logging_info_path, "a", encoding="utf-8", delay=True)
    file_info_handler.setLevel(logging.INFO)
    file_info_handler.setFormatter(file_formatter)
    logger.addHandler(file_info_handler)


class ChatBot:

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.api = self.vk.get_api()
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id, wait=1)

    def run(self):
        for event in self.long_poller.listen():
            logger.debug("Получено событие класса %s", event.type)
            try:
                self.event_handler(event)
            except Exception:
                logger.exception("Возникла ошибка при обработке события %s", event)

    def event_handler(self, event):
        if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
            response = "Вы сказали \""+event.object.message["text"]+"\"?"
            logger.debug("Отправляем сообщение \"%s\"", response)
            self.api.messages.send(
                message=response,
                random_id=randint(0, 2 ** 20),
                peer_id=event.object.message["peer_id"]
            )
        else:
            # TODO а где вы его ловите ? используем конструкцию if elif else
            # Не генерятся события типа MESSAGE_REPLY
            logger.info("Мы пока не умеем обрабатывать событие такого типа: %s", event.type)
            raise ValueError("Не то событие")


if __name__ == "__main__":
    bot = ChatBot(settings.group_id, settings.token)
    logger = logging.getLogger("bot")
    configure_logging(logger)
    bot.run()


