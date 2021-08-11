from urllib import parse

from pyrogram import Client, filters, types
import configparser
from re import search
from strings import lang_msg, strings

config = configparser.ConfigParser()
config.read('config.ini')

app = Client("WA")


def create_url(phone: str, text: str) -> str:
    format_url = "https://wa.me/{}?text={}"
    phone = phone.replace("+", "")
    if phone.startswith("05"):
        phone = phone.replace("0", "972", 1)
    return format_url.format(phone, parse.quote(text))


@app.on_message(filters.regex(r"^[0-9+].*$"))
def number_case(_, message: types.Message):
    message.reply(lang_msg(message, "ask_replay"), quote=True)


@app.on_message(filters.reply & filters.create(
    lambda _, __, m: m.reply_to_message.text != lang_msg(m, "ask_replay")))
def replay_url(_, message: types.Message):
    number = message.reply_to_message.text
    ex = search(r'[0-9+].*', number)

    if not ex:  # check if phone number invalid
        message.reply(lang_msg(message, "number_invalid"))
        return

    if len(number) > 15 or len(number) < 10:  # check if is legal length number
        message.reply(lang_msg(message, "invalid_length"))
        return

    url = create_url(number, message.text)

    message.reply(lang_msg(message, "replay_url").format(url),
                  reply_markup=types.InlineKeyboardMarkup([[
                      types.InlineKeyboardButton(lang_msg(message, "url_btn"), url=url),
                      types.InlineKeyboardButton(lang_msg(message, "share_btn"),
                                                 switch_inline_query=f"{number} {message.text}")
                  ]]))


@app.on_inline_query(filters.regex(r"^(?P<number>[0-9+]{10,16}) (?P<text>.*)"))
def inline(_, query: types.InlineQuery):
    match = query.matches[0].groupdict()
    url = create_url(match['number'], match['text'])

    query.answer([types.InlineQueryResultArticle(
        title=f"📞 {match['number']} • {match['text']} 📝",

        input_message_content=types.InputTextMessageContent(
            lang_msg(query, "replay_url").format(url)
        ),

        reply_markup=types.InlineKeyboardMarkup([[
            types.InlineKeyboardButton(lang_msg(query, "url_btn"), url=url),
            types.InlineKeyboardButton(lang_msg(query, "share_btn"),
                                       switch_inline_query=f"{match['number']} {match['text']}")
        ]]),

        description=lang_msg(query, "replay_url").format(url),

        thumb_url="https://telegra.ph/file/d89f5b180b532a85784a4.png"
    )])


@app.on_message(filters.reply & filters.create(
    lambda _, __, m: m.reply_to_message.text == lang_msg(m, "ask_replay")))
def do_not_replay_to_ask(_, message: types.Message):
    message.reply(lang_msg(message, "do_not_replay_to_ask"))


@app.on_message(filters.command("start") & filters.private)
def start(_, message: types.Message):
    txt = lang_msg(message, "start_msg")
    message.reply(txt, disable_web_page_preview=True,
                  reply_markup=types.InlineKeyboardMarkup([[
                      types.InlineKeyboardButton(lang_msg(message, "repo"),
                                                 url="https://github.com/david-lev/WhatsApp-API-Bot"),
                      types.InlineKeyboardButton(lang_msg(message, "inline_btn"),
                                                 switch_inline_query="+97212345678 TEXT")
                  ]]))


app.run()
