<img src="https://lh3.googleusercontent.com/proxy/8_-JRpJVLdqqxjkhqG6_p-akM2myMMwHgHU9Mg8JIgW7whClHBGptQZ3-jL0VFXDaxlfR0ffS5i61pJIuun3YhVxKja1EMKObKFOpkyTA3lkLpXrPaotjlofkhtfW7SF3q8cjGc" width="100" height="100">

# WhatsApp API Bot

### Telegram bot to create directs links to WhatsApp chats.

_You can check our bot [here](https://t.me/WhatsAppAPIbot)._

## configuration:
- Clone this reposetory:
```
git clone https://github.com/david-lev/WhatsApp-API-Bot.git
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
the ``api_id`` & ``api_hash`` You can get from [my.telegram.org](https://my.telegram.org).
``bot_token`` & ``bot_username`` you can get by create new bot on [BotFather](https://t.me/BotFather).
- To add your language to the bot, fork this repo and add your lines According to the [following](https://github.com/david-lev/WhatsApp-API-Bot/blob/main/strings.py#L4) instructions.
- Run the bot:
```
python3 main.py
```
---
![]()
Created with ❤️ by [David Lev](https://t.me/davidlev) & [Yehuda By](https://t.me/M100achuzBots)
