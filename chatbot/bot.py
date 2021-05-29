# -*- coding: utf-8 -*-

from random import randint
import logging
import os
import vk_api
from vk_api import bot_longpoll

try:
    import settings
except ImportError:
    exit("Copy settings.py default to settings.py and specify your group id and token")


def configure_logging(log):
    log.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    date_time_format = "%d %m %Y, %H:%M"
    file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt=date_time_format)
    logging_path = "chatbot_logs"
    if not os.path.exists(logging_path):
        os.mkdir(logging_path)

    logging_debug_path = os.path.join(logging_path, "chatbot_debug_log.log")
    file_debug_handler = logging.FileHandler(logging_debug_path, "a", encoding="utf-8", delay=True)
    file_debug_handler.setLevel(logging.DEBUG)
    file_debug_handler.setFormatter(file_formatter)
    log.addHandler(file_debug_handler)

    logging_info_path = os.path.join(logging_path, "chatbot_info_log.log")
    file_info_handler = logging.FileHandler(logging_info_path, "a", encoding="utf-8", delay=True)
    file_info_handler.setLevel(logging.INFO)
    file_info_handler.setFormatter(file_formatter)
    log.addHandler(file_info_handler)


class ChatBot:
    """
    Echo bot for vk.com

    Use Python 3.8
    """
    def __init__(self, group_id, token):
        """

        :param group_id: group id from group on vk.com
        :param token: secret token from group on vk.com
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.api = self.vk.get_api()
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id, wait=1)

    def run(self):
        """Runs echobot"""
        for event in self.long_poller.listen():
            # TODO Здесь проверяется тип поступившего на вход события, и поэтому я вижу в логах,
            # TODO что события типа MESSAGE_RESPONSE не приходят
            # TODO хотя в остальном всё работает нормально
            logger.debug("Получено событие класса %s", event.type)
            try:
                self.event_handler(event)
            except Exception:
                logger.exception("Возникла ошибка при обработке события %s", event)

    def event_handler(self, event: bot_longpoll.VkBotEvent):
        """Processing kv bot event"""
        if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
            response = "Вы сказали \""+event.object.message["text"]+"\"?"
            logger.debug("Отправляем сообщение \"%s\"", response)
            self.api.messages.send(
                message=response,
                random_id=randint(0, 2 ** 20),
                peer_id=event.object.message["peer_id"]
            )
        else:
            # а где вы его ловите ? используем конструкцию if elif else
            # TODO Все события, которые не MESSAGE_NEW, должны прилетать в эту ветку кода.
            # TODO Но распечатка типа приходящих в event_handler событий во время теста показывает
            # TODO Что типа MESSAGE_REPLY там нет, хотя бот исправно отвечает
            # TODO Возможно,это какая-то особенность работы более новой версии билиотеки vk_api
            # TODO Хотя событие такого типа в ней всё ещё есть.
            # TODO Но на событиях с другим типом, например, MESSAGE_EDIT, всё работает нормально
            # Не генерятся события типа MESSAGE_REPLY
            logger.info("Мы пока не умеем обрабатывать событие такого типа: %s", event.type)
            raise ValueError("Не то событие")


logger = logging.getLogger("bot")
configure_logging(logger)


if __name__ == "__main__":
    bot = ChatBot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
else:
    logging.disable(logging.CRITICAL)



