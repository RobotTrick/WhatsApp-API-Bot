from typing import Union
from pyrogram.types import Message, InlineQuery

# Here you can add your language strings. just add on every dict new key with your language code
# and insert the value. after you done, scroll down and add your language code to the 'lang_msg' func check.
# keep you're mind that languages are displayed accordingly to your client (app, software) lang.

strings = {
    "ask_replay": {
        "en": "✍️ Replay to the phone-number-message with your text",
        "he": "✍️ הגיבו להודעה שבה שלחתם את מספר הטלפון עם הטקסט שתרצו"
    },
    "number_invalid": {
        "en": "☎️ You can only replay on messages that contains phone number",
        "he": "☎ ️ ניתן להגיב עם טקסט רק על הודעות שמכילות מספר טלפון"
    },
    "invalid_length": {
        "en": "❌ Please input correct number (International format, for example +97212345678)",
        "he": "❌ הזינו מספר טלפון תקין בפורמט בינלאומי"
    },
    "replay_url": {
        "en": "🔗 Your link is: `{}`",
        "he": "🔗 הקישור שלך הוא: `{}`"
    },
    "url_btn": {
        "en": "🔗 Url",
        "he": "🔗 לינק"
    },
    "share_btn": {
        "en": "♻ Share",
        "he": "♻️ שיתוף"
    },
    "do_not_replay_to_ask": {
        "en": "💬 Please replay to message with phone number",
        "he": "💬 אנא הגב על הודעה שבה מופיע מספר טלפון"
    },
    "inline_btn": {
        "en": "🔁 Try inline!",
        "he": "🔁 נסו באינליין!"
    },
    "start_msg": {
        "en": "Hi {} 👋\n"
              "you can send me a phone number and text and I will return you a link that by clicking on it "
              "will "
              "be transferred to WhatsApp chat with the same number and with the text ready to send!\n"
              "You can also use me Inline! Type in the bot user followed by the phone number and text.",
        "he": "היי {} 👋\n"
              " תוכל לשלוח לי מספר טלפון וטקסט ואני אחזיר לכם קישור שבלחיצה עליו תועברו לצ'אט וואטסאפ עם "
              "אותו "
              "המספר ועם הטקסט מוכן לשליחה!\n"
              "ניתן להשתמש בי גם באינליין! הקלידו את יוזר הבוט ולאחריו את מספר הטלפון והטקסט."
    },
    "repo": {
        "en": "🛠 GitHub",
        "he": "🛠 גיטהאב"
    }

}


def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> str:
    msg = strings.get(msg_to_rpl)
    if msg_obj.from_user.language_code == "he":
        return msg["he"]
    # Edit this if you want to add you're language to the bot:
    # elif msg_obj.from_user.language_code == "YOUR_LANG_CODE":
    #     return msg["YOUR_LANG_CODE"]
    else:
        return msg["en"]
