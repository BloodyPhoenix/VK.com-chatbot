# -*- coding: utf-8 -*-


from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import ANY

import vk_api
from vk_api import bot_longpoll

from bot import ChatBot
import logging


class RunTest(TestCase):

    NEW_MESSAGE = {'type': 'message_new',
                   'object': {
                       'date': 1622531851,
                       'from_id': 65612830,
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
                bot.event_handler = Mock()
                bot.run()
                bot.event_handler.assert_called()
                bot.event_handler.assert_any_call(event)
                self.assertEqual(bot.event_handler.call_count, count)

    def test_event_handler_new_message(self):
        event = bot_longpoll.VkBotEvent(raw=self.NEW_MESSAGE)
        response = "Вы сказали \"" + event.object.text + "\"?"
        send_mock = Mock()
        with patch("bot.vk_api.VkApi"):
            with patch("bot.bot_longpoll.VkBotLongPoll"):
                bot = ChatBot("", "")
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.event_handler(event)
        send_mock.assert_called_once_with(
            message=response,
            random_id=ANY,
            user_id=event.object.peer_id)


if __name__ == "__main__":
    tests = RunTest()