from typing import Union
from pyrogram.types import Message, InlineQuery

# Here you can add your language strings. just add on every dict new key with your language code and insert the value.
# keep you're mind that languages are displayed accordingly to your client (app, software) lang.

strings = {
    "ask_replay": {
        "en": "✍️ Replay to the phone-number-message with your text",
        "it": "✍️ Rispondi al messaggio del numero di telefono con il tuo testo",
        "he": "✍️ הגיבו להודעה שבה שלחתם את מספר הטלפון עם הטקסט שתרצו",
        "es": "✍️ Responder al mensaje del número de teléfono con tu texto"
    },
    "number_invalid": {
        "en": "☎️ You can only replay on messages that contains phone number",
        "it": "☎️ Puoi rispondere solo a messaggi che contengono un numero di telefono",
        "he": "☎ ️ ניתן להגיב עם טקסט רק על הודעות שמכילות מספר טלפון",
        "es": "☎️ Solo se puede responder a mensajes que contengan número de teléfono"
    },
    "invalid_length": {
        "en": "❌ Please input correct number (International format, for example +97212345678)",
        "it": "❌ Inserisci un numero corretto (formato internazionale, ad esempio +39123456789)",
        "he": "❌ הזינו מספר טלפון תקין בפורמט בינלאומי",
        "es": "❌ Por favor ingresa un número correcto (Formato internacional, por ejemplo: +97212345678)"
    },
    "replay_url": {
        "en": "Click here to get/copy your link: {}",
        "it": "Clicca qui per ottenere/copiare il link: {}",
        "he": "לחץ כאן כדי לקבל/להעתיק את הקישור: {}",
        "es": "Haz clic para obtener/copiar tu enlace: {}"
    },
    "url_btn": {
        "en": "🔗 Url",
        "it": "🔗 Link",
        "he": "🔗 לינק",
        "es": "🔗 Enlace"
    },
    "share_btn": {
        "en": "♻ Share",
        "it": "♻️ Condividi",
        "he": "♻️ שיתוף",
        "es": "♻ Compartir"
    },
    "do_not_replay_to_ask": {
        "en": "💬 Please replay to message with phone number",
        "it": "💬 Rispondi al messaggio con il numero di teefono",
        "he": "💬 אנא הגב על הודעה שבה מופיע מספר טלפון",
        "es": "💬 Por favor responde al mensaje con número de teléfono"
    },
    "inline_btn": {
        "en": "🔁 Try inline!",
        "it": "🔁 Prova inline!",
        "he": "🔁 נסו באינליין!",
        "es": "🔁 Prueba el modo inline!"
    },
    "start_msg": {
        "en": "Hi {} 👋\n\n"
              "you can send me a phone number and text and I will return you a link that by clicking on it "
              "will "
              "be transferred to WhatsApp chat with the same number and with the text ready to send!\n"
              "You can also use me Inline! Type in the bot user followed by the phone number and text.\n"
              "\n- For help send /help"
              "\n- We need your help translating the bot! For more information send /translate"
              "\n\n- This bot made with ❤️ by [David Lev]({}) & [Yehuda By]({}) from [RobotTrick]({}) team.",
        "it": "Ciao {} 👋\n\n"
              "puoi inviarmi un numero di telefono e un messaggio e ti invierò un link che cliccandoci sopra "
              "verrai "
              "mandato su WhatsApp del numero e con il testo pronto per l'invio!\n"
              "Puoi anche usarmi Inline! Digita lo username del bot seguito dal numero di telefono e dal testo.\n "
              "\n- Per altro invia /help"
              "\n- Abbiamo bisogno del tuo aiuto per tradurre il bot! Per maggiori informazioni invia /traduci"
              "\n\n- Questo bot è realizzato con il ❤️ da [David Lev]({}) e [Yehuda By]({}) dal team [RobotTrick]({}).",
        "he": "היי {} 👋\n\n"
              "תוכל לשלוח לי מספר טלפון וטקסט ואני אחזיר קישור שבלחיצה עליו תועבר לצ'אט וואטסאפ עם "
              "אותו "
              "המספר ועם הטקסט מוכן לשליחה.\n"
              "ניתן להשתמש בי גם באינליין! הקלד את יוזר הבוט ולאחריו את מספר הטלפון והטקסט."
              "\n\n- לעזרה שלחו /help"
              "\n- אנו זקוקים לעזרתכם בתרגום הבוט! למידע נוסף שלחו /translate"
              "\n\n- הבוט נוצר על ידי [David Lev]({}) & [Yehuda By]({}) מצוות [רובוטריק]({}).",
        "es": "Hola {} 👋\n\n"
              "puedes enviarme un número de teléfono y un texto y te devolveré un enlace que al abrirlo "
              "te dirigirá "
              "a un chat de WhatsApp con ese número de teléfono y con el texto listo para enviar!\n"
              "Además puedes usarme Inline! Escribe el nombre de usuario del bot seguido del teléfono y el texto.\n"
              "\n- Por ayuda envía /help"
              "\n- Necesitamos tu ayuda para traducir el bot! Para más información envía /translate"
              "\n\n- Este bot fue hecho con ❤️ por [David Lev]({}) y [Yehuda By]({}) del equipo [RobotTrick]({})."
    },
    "repo": {
        "en": "🛠 GitHub",
        "it": "🛠 GitHub",
        "he": "🛠 גיטהאב",
        "es": "🛠 GitHub"
    },
    "url_repo": {
        "en": "https://github.com/RobotTrick/WhatsApp-API-Bot"
    },
    "support": {
        "en": "👤 Support",
        "it": "👤 Supporto",
        "he": "👤 תמיכה",
        "es": "👤 Soporte"
    },
    "input_sug": {
        "en": "Enter input like +97212345678 Hello from Telegram",
        "it": "Inserisci un input come +39123456789 Ciao da Telegram",
        "he": "הזינו טלפון וטקסט: 97212345678+ טקסט",
        "es": "Ingresa algo como: +97212345678 Hola desde Telegram"
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
        "it": "Questo bot ti consente di creare collegamenti diretti alle chat di WhatsApp con testo pronto per l'invio."
              "\n\necco due modi per usare questo bot:"
              "\n1. --Messaggi e risposte:--"
              "\n- Invia il numero di telefono."
              "\n- Rispondi al **messaggio numerico** con il testo da inviare."
              "\n- Ricevi un link da cliccare e copiare.\n"
              "\n\n2. --Uso Inline:--"
              "\n- Digita lo username del bot in qualsiasi chat."
              "\n- Dopodiché digita un numero di telefono e subito dopo un messaggio da inviare."
              "\n- Fai clic sul risultato che verrà visualizzato e otterrai il collegamento pronto per fare clic e copiare.",
        "he": "רובוט זה מאפשר יצירת קישורים ישירים לצ'אט וואטסאפ עם טקסט מוכן לשליחה.\n"
              "קיימות שתי צורות שימוש בבוט:\n\n"
              "1. --הודעות ותגובות:--\n"
              "- שלחו את מספר הטלפון.\n"
              "- הגיבו על **המספר** עם טקסט לשליחה.\n"
              "- קבלו קישור מוכן להקלקה ולהעתקה.\n\n"
              "2. --שימוש באינליין:--\n"
              "- הקלידו את יוזר הבוט בכל צ'אט שתרצו.\n"
              "- לאחריו הקלידו מספר טלפון ומיד לאחריו טקסט לשליחה.\n"
              "- הקליקו על התוצאה שתוצג ותקבלו את הקישור.",
        "es": "Este bot te permitirá crear links directos a chats de WhatsApp con texto listo para enviar."
              "\n\nhay dos formas de usar este bot:"
              "\n1. --Mensajes y Respuestas:--"
              "\n- Enviar el número de telefono (al que se desea enviar)."
              "\n- Responder al **mensaje con el número telefónico** con el texto a enviar."
              "\n- Obtener un enlace listo para tocar y copiar.\n"
              "\n\n2. --Usando Inline:--"
              "\n- Escribe el nombre de usuario del bot en cualquier chat (comenzando con @)."
              "\n- Después de eso escribir el número e inmediatamente después el texto a enviar."
              "\n- Toca en el resultado que se mostrará y ya tendrás el enlace listo para tocar y copiar."
    },
    "translate": {
        "en": "**🔡 We need your help translating the bot!**"
              "\n\nIf you are interested in translating the bot into your language or to another language, go to the "
              "strings file in GitHub, download it or edit it online and add the strings to the file according to the "
              "existing format. "
              "\n- Got tangled up, need help? Contact our support user.",
        "it": "**🔡 Abbiamo bisogno del tuo aiuto per tradurre il bot!**"
              "\n\nSe sei interessato a tradurre il bot nella tua lingua o in un'altra lingua, vai alle "
              "stringhe su GitHub, scaricalo o modificalo online e aggiungi le stringhe al file in base al "
              "formato esistente",
        "\n- Ti sei impasticciato, hai bisogno di aiuto? Contatta il nostro utente dell'assistenza."
        "he": "**🔡 אנו צריכים את עזרתכם בתרגום הבוט!**"
              "\n\nאם הנכם מעוניינים לתרגם את הבוט לשפתכם או לשפה אחרת, עברו לקובץ ההודעות בגיטהאב, הורידו אותו או "
              "ערכו "
              "באונליין והוסיפו את המחרוזות לקובץ על פי הפורמט הקיים. \n\n- הסתבכתם, זקוקים לעזרה? פנו למשתמש התמיכה "
              "שלנו. ",
        "es": "**🔡 Necesitamos tu ayuda con la traducción del bot!**"
              "\n\nSi estás interesado/a en traducir el bot a tu idioma u otro, ve al "
              "archivo strings.py en GitHub, descargalo o editalo online y agrega las cadenas de texto siguiendo el "
              "formato existente. "
              "\n- Te perdiste, necesitas ayuda? Contacta a nuestro soporte."
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
    
