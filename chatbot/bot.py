# -*- coding: utf-8 -*-

from random import randint
import logging
import os
import vk_api
from vk_api import bot_longpoll
import handlers

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


class UserState:
    def __init__(self, scenario: str, step, context=None):
        self.scenario_name = scenario
        self.current_step = step
        self.context = context or {}


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
        self.users_state = {} # key - user_id -> user_stage

    def run(self):
        """Runs echobot"""
        for event in self.long_poller.listen():
            logger.debug("Получено событие класса %s", event.type)
            try:
                self.event_handler(event)
            except Exception:
                logger.exception("Возникла ошибка при обработке события %s", event)

    def event_handler(self, event: bot_longpoll.VkBotEvent):
        if event.type != bot_longpoll.VkBotEventType.MESSAGE_NEW:
            logger.info("Мы пока не умеем обрабатывать событие такого типа: %s", event.type)
            return
        """Processing vk bot event"""
        text = event.object.text
        user_id = event.object.peer_id
        if user_id in self.users_state:
            response = self.continue_scenario(user_id=user_id, text=text)
        else:
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent["tokens"]):
                    logger.debug("Us gets intent")
                    if intent["answer"]:
                        response = intent["answer"]
                    else:
                        response = self.start_scenario(intent["scenario"], user_id)
                    break
            else:
                response = settings.DEFAULT_ANSWER
        logger.debug("Отправляем сообщение \"%s\"", response)
        self.api.messages.send(
            message=response,
            random_id=randint(0, 2 ** 20),
            user_id=user_id
        )

    def continue_scenario(self, user_id, text):
        state = self.users_state[user_id]
        steps = settings.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.current_step]
        handler = getattr(handlers, step["handler"])
        if handler(text, context=state.context):
            next_step = steps[step["next_step"]]
            response = next_step["text"]
            if next_step["next_step"]:
                logger.info(state.context)
                state.current_step = step["next_step"]
            else:
                name = state.context["name"]
                logger.info(f"Scenario {state.scenario_name} for user {name} id {user_id} finished")
                self.users_state.pop(user_id)

        else:
            response = step["failure_text"]
        response = response.format(**state.context)
        return response

    def start_scenario(self, scenario_name, user_id):
        scenario = settings.SCENARIOS[scenario_name]
        start = scenario["first_step"]
        step = scenario["steps"][start]
        self.users_state[user_id] = UserState(scenario_name, start)
        logger.debug(f"Пользователь {user_id} начал сценарий {scenario_name}")
        return step["text"]


logger = logging.getLogger("bot")
configure_logging(logger)


if __name__ == "__main__":
    bot = ChatBot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
else:
    logging.disable(logging.CRITICAL)



