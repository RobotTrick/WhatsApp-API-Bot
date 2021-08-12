<img src="https://img.icons8.com/ios/50/000000/whatsapp.png" width="100" height="100">

# WhatsApp API Bot

### Telegram bot to create direct links with pre-filled text for WhatsApp Chats

> You can check our bot [here](https://t.me/WhatsAppAPIbot).

The bot is based on the API [provided](https://faq.whatsapp.com/general/chats/how-to-use-click-to-chat/) by WhatsApp.

## Translation Contributions
You can add your language to the bot by editing the [strings.py](/strings.py) file and adding a translation in the appropriate format:
```python
strings = {
    "example1": {
        "en": "This string represents message exmple1",
        "he": "המחרוזת הזו מייצגת הודעת דוגמה 1",
        "ru": "Эта строка представляет сообщение exmple1"
    },
     "example2": {
        "en": "This string represents message exmple2",
        "he": "המחרוזת הזו מייצגת הודעת דוגמה 2",
        "ru": "Эта строка представляет сообщение exmple2"
    }
}
```
- Add your language code as key, the lang-code should be in `IETF language tag` format.
- Try to stick to the format and translate from the English language available in the file.
- Maintain the position of the special characters (emojis, `.*,-/\{}`).
- When you done, open a __pull request__ or send us the file to [our](https://t.me/RobotTrickSupport) Telegram.



## Run the bot by yourself

- Clone this reposetory:
```
git clone https://github.com/RobotTrick/WhatsApp-API-Bot.git
```
- Install requirements (``pyrogram, tgcrypto``):
```
pip3 install -U pyrogram tgcrypto
```
- Edit and insert the folowing values into the [config](/config.ini) file:
```
[pyrogram]
api_id = XXXXXXXXXXX
api_hash = XXXXXXXXXXXXXXXXXXXXXXXXXX
bot_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
* ``api_id`` & ``api_hash`` You can get from [my.telegram.org](https://my.telegram.org).
* ``bot_token`` you can get by create new bot on [BotFather](https://t.me/BotFather).
- Run the bot:
```
python3 main.py
```

## Supported languages
- [x] English
- [x] Hebrew

## TODO's
- [x] Send message to specific phone number.
- [ ] Open chat with specific number.
- [ ] Create link with pre-filled message to pick chat.
---
Created with ❤️ by [David Lev](https://t.me/davidlev) & [Yehuda By](https://t.me/M100achuzBots)
