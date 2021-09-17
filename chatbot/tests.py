# -*- coding: utf-8 -*-


from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import ANY

from pony.orm import db_session, rollback
from vk_api import bot_longpoll

from bot import ChatBot
import logging
from copy import deepcopy

import settings


def isolate_db(func):
    def wrapper(*args, **kwargs):
        with db_session:
            func(*args, **kwargs)
            rollback()
    return wrapper


class RunTest(TestCase):

    INPUTS = ["Привет",
              "А когда?",
              "Где будет конференция?",
              "Зарегистрируй меня",
              "Вениамин",
              "мой адрес email@email",
              "email@email.ru",
]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]["answer"],
        settings.INTENTS[1]["answer"],
        # TODO мне кажется вы тут пропустили settings.INTENTS[2]["answer"],
        # TODO поэтому тест падает
        settings.SCENARIOS["registration"]["steps"]["step1"]["text"],
        settings.SCENARIOS["registration"]["steps"]["step2"]["text"],
        settings.SCENARIOS["registration"]["steps"]["step2"]["failure_text"],
        settings.SCENARIOS["registration"]["steps"]["step3"]["text"].format(name="Вениамин", email="email@email.ru")
    ]

    NEW_MESSAGE = {'type': 'message_new',
                   'object': {
                       'date': 1622531851,
                       'from_id': 65612830123,
                       'id': 132,
                       'out': 0,
                       'peer_id': 65612830,
                       'text': "Morning! Nice day for fishing, ain't it? Huh-ha!",
                       'conversation_message_id': 132,
                       'fwd_messages': [],
                       'important': False,
                       'random_id': 0,
                       'attachments': [],
                       'is_hidden': False},
                   'group_id': 204141185,
                   'event_id': '9148e93b9b01f7a60cde729c31a0040f5d77ab75'}

    def test_run(self):
        count = 5
        event = bot_longpoll.VkBotEvent
        events = [event] * count
        long_poller_listen_mock = Mock(return_value=events)
        long_poller_mock = Mock()
        logging.Logger = Mock()
        long_poller_mock.listen = long_poller_listen_mock
        with patch("bot.vk_api.VkApi"):
            with patch("bot.bot_longpoll.VkBotLongPoll", return_value=long_poller_mock):
                bot = ChatBot("", "")
                bot._event_handler = Mock()
                bot.run()
                bot._event_handler.assert_called()
                bot._event_handler.assert_any_call(event)
                self.assertEqual(bot._event_handler.call_count, count)

    def test_event_handler_new_message(self):
        event = bot_longpoll.VkBotEvent(raw=self.NEW_MESSAGE)
        response = settings.DEFAULT_ANSWER
        send_mock = Mock()
        with patch("bot.vk_api.VkApi"):
            with patch("bot.bot_longpoll.VkBotLongPoll"):
                bot = ChatBot("", "")
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot._event_handler(event)
        send_mock.assert_called_once_with(
            message=response,
            random_id=ANY,
            user_id=event.object.peer_id)

    @isolate_db
    def test_run_scenario(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.NEW_MESSAGE)
            event["object"]["text"] = input_text
            events.append(bot_longpoll.VkBotEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch("bot.bot_longpoll.VkBotLongPoll", return_value=long_poller_mock):
            bot = ChatBot("", "")
            bot.api = api_mock
            bot.run()

        self.assertEqual(len(self.INPUTS), send_mock.call_count)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs["message"])
        self.assertEqual(self.EXPECTED_OUTPUTS, real_outputs)


if __name__ == "__main__":
    tests = RunTest()
