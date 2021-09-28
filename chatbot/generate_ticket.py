import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from settings import TICKET_CONFIG as config


def generate_ticket(name, email):
    base = Image.open(config["template_path"]).convert("RGBA")
    font = ImageFont.truetype(config["font_path"], config["font_size"])
    draw = ImageDraw.Draw(base)

    url = "https://robohash.org/"+email
    response = requests.get(url=url)
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)
    avatar.thumbnail(config["avatar_size"])
    avatar_background = Image.new("RGBA", config["avatar_size"], "WHITE")
    avatar_background.paste(im=avatar, box=(0, 0), mask=avatar)
    avatar = avatar_background.convert("RGB")

    draw.text(config["name_space"], name, font=font, fill=config["font_colour"])
    draw.text(config["email_space"], email, font=font, fill=config["font_colour"])
    base.paste(avatar, box=config["avatar_place"])

    temp_file = BytesIO()
    base.save(temp_file, "png")
    temp_file.seek(0)

    return temp_file


if __name__ == "__main__":
    ticket = generate_ticket("Vasya", "email@email.com")
    with open("files/ticket_example.png", "wb") as file:
        file.write(ticket.read())