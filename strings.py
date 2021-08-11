from typing import Union
from pyrogram.types import Message, InlineQuery

# Here you can add your language strings. just add on every dict new key with your language code and insert the value.
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
        "en": "Click here to get/copy your link: {}",
        "he": "לחץ כאן כדי לקבל/להעתיק את הקישור: {}"
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
        "en": "Hi {} 👋\n\n"
              "you can send me a phone number and text and I will return you a link that by clicking on it "
              "will "
              "be transferred to WhatsApp chat with the same number and with the text ready to send!\n"
              "You can also use me Inline! Type in the bot user followed by the phone number and text.\n"
              "\n- For help send /help"
              "\n- We need your help translating the bot! For more information send /translate"
              "\n\n\n",
        "he": "היי {} 👋\n\n"
              "תוכל לשלוח לי מספר טלפון וטקסט ואני אחזיר קישור שבלחיצה עליו תועבר לצ'אט וואטסאפ עם "
              "אותו "
              "המספר ועם הטקסט מוכן לשליחה.\n"
              "ניתן להשתמש בי גם באינליין! הקלד את יוזר הבוט ולאחריו את מספר הטלפון והטקסט."
              "\n\n- לעזרה שלחו /help"
              "\n- אנו זקוקים לעזרתכם בתרגום הבוט! למידע נוסף שלחו /translate"
    },
    "repo": {
        "en": "🛠 GitHub",
        "he": "🛠 גיטהאב"
    },
    "url_repo": {
        "en": "https://github.com/RobotTrick/WhatsApp-API-Bot"
    },
    "support": {
        "en": "👤 Support",
        "he": "👤 תמיכה"
    },
    "input_sug": {
        "en": "Enter input like +97212345678 Hello from Telegram",
        "he": "הזינו טלפון וטקסט: 97212345678+ טקסט"
    },
    "help_msg": {
        "en": "This bot allows you to create direct links to WhatsApp chats with text ready to send."
              "\n\nhere are two ways to use this bot:"
              "\n1. --Messages and Replays:--"
              "\n- Send the phone number."
              "\n- Replay on the **number message** with text to send."
              "\n- Get a link ready to click and to copy.\n"
              "\n\n2. --Using Inline:--"
              "\n- Type the bot username in any chat."
              "\n- After that type a phone number and immediately after it a text to send."
              "\n- Click on the result that will be displayed and you will get the link ready to click and to copy.",
        "he": "רובוט זה מאפשר יצירת קישורים ישירים לצ'אט וואטסאפ עם טקסט מוכן לשליחה.\n"
              "קיימות שתי צורות שימוש בבוט:\n\n"
              "1. --הודעות ותגובות:--\n"
              "- שלחו את מספר הטלפון.\n"
              "- הגיבו על **המספר** עם טקסט לשליחה.\n"
              "- קבלו קישור מוכן להקלקה ולהעתקה.\n\n"
              "2. --שימוש באינליין:--\n"
              "- הקלידו את יוזר הבוט בכל צ'אט שתרצו.\n"
              "- לאחריו הקלידו מספר טלפון ומיד לאחריו טקסט לשליחה.\n"
              "- הקליקו על התוצאה שתוצג ותקבלו את הקישור."
    },
    "translate": {
        "en": "**🔡 We need your help translating the bot!**"
              "\n\nIf you are interested in translating the bot into your language or to another language, go to the "
              "strings file in GitHub, download it or edit it online and add the strings to the file according to the "
              "existing format. "
              "\n- Got tangled up, need help? Contact our support user.",
        "he": "**🔡 אנו צריכים את עזרתכם בתרגום הבוט!**"
              "\n\nאם הנכם מעוניינים לתרגם את הבוט לשפתכם או לשפה אחרת, עברו לקובץ ההודעות בגיטהאב, הורידו אותו או "
              "ערכו "
              "באונליין והוסיפו את המחרוזות לקובץ על פי הפורמט הקיים. \n\n- הסתבכתם, זקוקים לעזרה? פנו למשתמש התמיכה "
              "שלנו. "
    }

}


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
