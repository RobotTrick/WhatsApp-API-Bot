from typing import Union
from pyrogram.types import Message, InlineQuery

strings = {
    "ask_replay": {
        "en": "replay to this message with your text",
        "he": "הגיבו להודעה זו עם הטקסט"
    },
    "number_invalid": {
        "en": "You can only replay on messages that contains phone number",
        "he": "ניתן להגיב עם טקסט רק על הודעות שמכילות מספר טלפון"
    },
    "invalid_length": {
        "en": "Please input correct number",
        "he": "הזינו מספר טלפון תקין"
    },
    "replay_url": {
        "en": "Your link is: `{}`",
        "he": "הקישור שלך הוא: `{}`"
    },
    "url_btn": {
        "en": "URL",
        "he": "לינק"
    },
    "share_btn": {
        "en": "SHARE",
        "he": "שיתוף"
    },
    "do_not_replay_to_ask": {
        "en": "Please replay to message with phone number",
        "he": "אנא הגב על הודעה שבה מופיע מספר טלפון"
    },
    "inline_btn": {
        "en": "Try inline!",
        "he": "נסה באינליין!"
    },
    "start_msg": {
        "en": "Hi, you can send me a phone number and text and I will return you a link that by clicking on it will "
              "be transferred to WhatsApp chat with the same number and with the text ready to send!\n"
              "You can also use me Inline! Type in the bot user followed by the phone number and text.",
        "iw": "היי, תוכלו לשלוח לי מספר טלפון וטקסט ואני אחזיר לכם קישור שבלחיצה עליו תועברו לצ'אט וואטסאפ עם אותו "
              "המספר ועם הטקסט מוכן לשליחה!\n"
              "ניתן להשתמש בי גם באינליין! הקלידו את יוזר הבוט ולאחריו את מספר הטלפון והטקסט."
    },
    "repo": {
        "en": "GitHub",
        "he": "גיטהאב"
    }

}


def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> str:
    msg = strings.get(msg_to_rpl)
    if msg:
        return msg["he"] if msg_obj.from_user.language_code == "he" else msg["en"]
