# -*- coding: utf-8 -*-

from random import randint
import group_info
import vk_api
from vk_api import bot_longpoll


class Chatbot:

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.api = self.vk.get_api()
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id, wait=1)

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.event_handler(event)
            except Exception as exception:
                print(exception)

    def event_handler(self, event):
        if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.object.message["text"])
            self.api.messages.send(
                message=event.object.message["text"],
                random_id=randint(0, 2 ** 20),
                peer_id=event.object.message["peer_id"]
            )


if __name__ == "__main__":
    bot = Chatbot(group_info.group_id, group_info.token)
    bot.run()
