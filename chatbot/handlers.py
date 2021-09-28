# -*- coding: utf-8 -*-


import re
from generate_ticket import generate_ticket

name_pattern = re.compile(r"^[\w\-\s]{3,40}$")
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def handle_name(text: str, context: dict):
    match = re.match(name_pattern, text)
    if match:
        context["name"] = text
        return True
    else:
        return False


def handle_email(text: str, context: dict):
    matches = re.findall(email_pattern, text)
    if len(matches) > 0:
        context["email"] = matches[0]
        return True
    else:
        return False


def generate_ticket_handler(context: dict):
    return generate_ticket(context["name"], context["email"])
