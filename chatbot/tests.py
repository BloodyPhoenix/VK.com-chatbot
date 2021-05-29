# -*- coding: utf-8 -*-


from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import ANY

import vk_api.bot_longpoll

from bot import ChatBot
import logging


class RunTest(TestCase):

    NEW_MESSAGE = {'type': 'message_new',
                 'object': {
                     'message':
                         {'date': 1622275648,
                          'from_id': 65612215,
                          'id': 87,
                          'out': 0,
                          'peer_id': 65612858,
                          'text': "Morning! Nice day for fishing, ain't it?",
                          'conversation_message_id': 87,
                          'fwd_messages': [],
                          'important': False,
                          'random_id': 0,
                          'attachments': [],
                          'is_hidden': False},
                     'client_info':
                         {'button_actions': [
                             'text',
                             'vkpay',
                             'open_app',
                             'location',
                             'open_link',
                             'callback',
                             'intent_subscribe',
                             'intent_unsubscribe'
                         ],
                             'keyboard': True,
                             'inline_keyboard': True,
                             'carousel': True,
                             'lang_id': 0}
                 },
                 'group_id': 204141185,
                 'event_id': 'f799398a530cec32da64eaf70853b0aa58c63d72'}

    def test_run(self):
        count = 5
        event = vk_api.bot_longpoll.VkBotEvent
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
        event = vk_api.bot_longpoll.VkBotEvent(raw=self.NEW_MESSAGE)
        response = "Вы сказали \"" + event.object.message["text"] + "\"?"
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
            peer_id=self.NEW_MESSAGE["object"]["message"]["peer_id"])


if __name__ == "__main__":
    tests = RunTest()