# -*- coding: utf-8 -*-


import re

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
