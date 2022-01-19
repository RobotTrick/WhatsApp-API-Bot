from urllib import parse
import json
from pyrogram import Client, filters, types
import configparser
from re import search, sub
from strings import strings
from typing import Union
from pyrogram.types import Message, InlineQuery

config = configparser.ConfigParser()
config.read('config.ini')

app = Client("WA")


# Return message depend on the client language:
def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> Union[str, bool]:
    msg = strings.get(msg_to_rpl)
    if not msg:
        return False
    lang_client = msg_obj.from_user.language_code
    if msg.get(lang_client):
        return msg[lang_client]
    else:
        return msg["en"]


# Return encoded url
def create_url(phone: str, text: str) -> str:
    format_url = "https://wa.me/{}?text={}"
    phone = phone.replace("+", "")
    if phone.startswith("05"):
        phone = phone.replace("0", "972", 1)
    return format_url.format(phone, parse.quote(text))


def save_user(uid: int, save_use: bool = True):
    """ save user/chat id to DB """
    if save_use:
        save_uses()
    ids_file = "users.json"
    try:
        with open(ids_file, "r") as oFile:
            users: list = json.load(oFile)
    except FileNotFoundError:
        users = []

    if uid not in users:
        users.append(uid)

    with open(ids_file, "w") as nFile:
        json.dump(users, nFile, indent=4)


def save_uses():
    """ save count of uses to DB """
    uses_file = "uses.txt"
    try:
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    except FileNotFoundError:
        with open(uses_file, "w") as usesO:
            usesO.write("0")
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    uses += 1
    with open(uses_file, "w") as usesO:
        usesO.write(str(uses))


# Ask replay on messages with phone number
@app.on_message(filters.regex(r"^[0-9+].*$"))
def number_case(_, message: types.Message):
    message.reply(lang_msg(message, "ask_replay"), quote=True)


@app.on_message(filters.reply & filters.create(
    lambda _, __, m: m.reply_to_message.text != lang_msg(m, "ask_replay")))
def replay_url(_, message: types.Message):
    number = message.reply_to_message.text
    number = sub(r"[^0-9+]", "", number)
    ex = search(r'[0-9+].*', number)

    if not ex:  # check if phone number invalid
        message.reply(lang_msg(message, "number_invalid"))
        return

    if len(number) > 15 or len(number) < 10:  # check if is legal length number
        message.reply(lang_msg(message, "invalid_length"))
        return

    url = create_url(number, message.text)
    # send message with the url
    message.reply(lang_msg(message, "replay_url").format(f"`{url}`"),
                  reply_markup=types.InlineKeyboardMarkup([[
                      types.InlineKeyboardButton(lang_msg(message, "url_btn"), url=url),
                      types.InlineKeyboardButton(lang_msg(message, "share_btn"),
                                                 switch_inline_query=f"{number} {message.text}")
                  ]]))
    save_user(message.from_user.id)


valid_re = r"^(?P<number>[0-9+]{10,16}) (?P<text>.*)"


# handle inline queries
@app.on_inline_query(filters.regex(valid_re))
def inline(_, query: types.InlineQuery):
    match = query.matches[0].groupdict()
    url = create_url(match['number'], match['text'])

    query.answer([types.InlineQueryResultArticle(
        title=f"{match['number']} • {match['text']}",

        input_message_content=types.InputTextMessageContent(
            lang_msg(query, "replay_url").format(f"`{url}`")
        ),

        reply_markup=types.InlineKeyboardMarkup([[
            types.InlineKeyboardButton(lang_msg(query, "url_btn"), url=url),
            types.InlineKeyboardButton(lang_msg(query, "share_btn"),
                                       switch_inline_query=f"{match['number']} {match['text']}")
        ]]),

        description=lang_msg(query, "replay_url").format(url),

        thumb_url="https://user-images.githubusercontent.com/42866208/129119407-17ea2432-7057-4501-8015-119c6da33bad.png"
    )])
    save_user(query.from_user.id)


@app.on_inline_query(~filters.regex(valid_re))
def valid_re(_, query: types.InlineQuery):
    query.answer([]
                 , switch_pm_text=lang_msg(query, "input_sug"), switch_pm_parameter="help")


# When user replay to replay msg instead of phone-num msg
@app.on_message(filters.reply & filters.create(
    lambda _, __, m: m.reply_to_message.text == lang_msg(m, "ask_replay")))
def do_not_replay_to_ask(_, message: types.Message):
    message.reply(lang_msg(message, "do_not_replay_to_ask"))


# start command
@app.on_message(filters.command(["start", "help", "translate"]) & filters.private)
def start(_, message: types.Message):
    if message.command == ["start"]:
        txt = lang_msg(message, "start_msg").format(
            message.from_user.mention,
            "https://t.me/davidlev",
            "https://t.me/m100achuzBots",
            "https://t.me/robot_trick_channel"
        )
        message.reply(txt, disable_web_page_preview=True,
                      reply_markup=types.InlineKeyboardMarkup([[
                          types.InlineKeyboardButton(lang_msg(message, "repo"),
                                                     url=lang_msg(message, "url_repo")),
                          types.InlineKeyboardButton(lang_msg(message, "inline_btn"),
                                                     switch_inline_query_current_chat="")
                      ]]))
    elif "help" in message.command:
        message.reply(lang_msg(message, "help_msg"),
                      reply_markup=types.InlineKeyboardMarkup([[
                          types.InlineKeyboardButton(lang_msg(message, "inline_btn"),
                                                     switch_inline_query_current_chat="")
                      ]]))
    elif "translate" in message.command:
        message.reply(lang_msg(message, "translate"),
                      reply_markup=types.InlineKeyboardMarkup([[
                          types.InlineKeyboardButton(lang_msg(message, "repo"),
                                                     url=f"{lang_msg(message, 'url_repo')}/blob/main/strings.py"),
                          types.InlineKeyboardButton(lang_msg(message, "support"),
                                                     url="https://t.me/RobotTrickSupport")
                      ]]))

    save_user(message.from_user.id, False)


app.run()
