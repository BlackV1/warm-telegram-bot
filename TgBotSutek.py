import random
from datetime import date
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup

# === НАСТРОЙКИ ===
TOKEN = "8220445421:AAFj30coFLuk330NJ74KywUqPttW12wXPlc"
MEETING_DATE = date(2026, 6, 14)
DEPARTURE_DATE = date(2026, 2, 15)
MY_CHAT_ID = 1194574842

SOFT_MESSAGES = [
    "А я тебя люблю, прелесть!",
    "Скучаю по теплу твоего тела...",
    "Я тону в твоих глазах, а ты в моих...",
    "Шр-х-кк-вц-уп, ой простите, в Европе связь барахлит, я перезвоню",
    "-Привет, я сейчас в Европе, не могу говорить \n"
    "-Но ты же сам написал...\n"
    "-Всёёё, не могу говорить, тут слишком красиво",
    "Ты милаааааааааашечка💛",
    "Я слышу хруст твоих суставов и огонь в твоих глазааааах",
    "Я верю в тебя!",
    "Я скучаю по тебе... Очень...",
    "Ты — мой дом",
    "Я ЛЮБЛЮЮЮЮ ТЕБЯ ДО СЛЛЕЕЕЕЕЕЗ",
    "Я рядом, Лид💛",
    "Ты - нафталин моих мехов, конъюнктивит моих очей🦈",
    "СООООЛНЫШКООООООООО🥹",
    "Что, милое сообщение ожидала увидеть? Лох! \n"
    "Ну лааааааааааааадно, так уж и быть)) Нажми еще раз))",
    "Ну фто, малыфка, к тебе или ко мне?",
    "Где твои губы, когда они мне так нужны..",
    "Желаю всем годовой запас кофе!!!",
    "Обожаю тебя🫂",
    "Ты лучшая!💛",
    "Думаю о тебе...💛",
    "Расцеловать тебя хочется!!!",
    "Прилечь бы сейчас с тобой в обнимку"
]

STICKERS = [
    "CAACAgIAAxkBAAFA3sxpbPdIrFWG3W8CltSe9rYiYjoxKgACjQEAAiteUwvXatazNkylHDgE",
    "CAACAgQAAxkBAAFA3tRpbPgcppxpM90emOsxcR2jFekCMQAC2BQAAuiWMFKeUXzNBIgNGzgE",
    "CAACAgQAAxkBAAFA3thpbPg7bxPkaUzYrAqdQQm33VSNsAACXxIAAlnsCFLWYwMTNjjlYTgE",
    "CAACAgQAAxkBAAFA3uBpbPheNedk9o4YdtbRsvtilNtCSwACgRMAAt_I2VOKmTHOdbqtTTgE",
    "CAACAgIAAxkBAAFBCihpcdPeCq48U9S3ypuPuqi7CgABHbAAAm8_AAKEGbBKjh9-eEJZaZo4BA",
    "CAACAgIAAxkBAAFBCippcdPooK4_hp0vUvuFXlOs1U-mHgACHCUAAm3FyUl96nT8kts0zzgE",
    "CAACAgIAAxkBAAFBCixpcdPyyV9S3s3qVbJnBTfJSbYnOQACpBsAAtsS0EkLKsSm2aNDqTgE",
    "CAACAgIAAxkBAAFBCi5pcdP2Cn39MN1o26T9PahHaNW4TgACdx4AApRuyEkjwf63ds1DyTgE",
    "CAACAgIAAxkBAAFBCjBpcdP5YO_2yyzZbcSCsPJVzD6ZwQACGyMAAl5J0UmN4pHGYMho6DgE",
    "CAACAgIAAxkBAAFBCjNpcdQOCq3UJadrV_S70z7Nr5aJdgAC0yAAAkAtyElSD1F7REosZDgE",
    "CAACAgIAAxkBAAFBCjVpcdQYeYavITK5NOlMpsPVkkBC6AACViMAAsB10ElzoZn_OXdpijgE"
]

def persistent_keyboard():
    keyboard = [
        ["Мне тебя не хватает...💛", "⏳ Сколько осталось", "📞 Хочу, чтобы ты позвонил"]
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

# === КОМАНДЫ ===
async def days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = date.today()

    if today < DEPARTURE_DATE:
        remaining = (MEETING_DATE - today).days
        text = (
            "Хээээй! Я ещё никуда не улетел, солнце :)🤍\n"
            "Мы всё ещё рядом💛"
        )
    else:
        remaining = (MEETING_DATE - today).days
        if remaining >= 0:
            text = (
                f"До нашей встречи осталось дней: {remaining} 🤍\n"
                "Это на один день меньше, чем вчера, солнышко :)\n"
                "14.06.2026"
            )
        else:
            text = "Мы уже вместе💛"

    await update.message.reply_text(text)

async def missyou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker = random.choice(STICKERS)
    message = random.choice(SOFT_MESSAGES)

    await update.message.reply_sticker(sticker)
    await update.message.reply_text(message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я здесь, солнышко, и я тебя люблю💛",
        reply_markup=persistent_keyboard()
    )


async def text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Мне тебя не хватает...💛":
        sticker = random.choice(STICKERS)
        message = random.choice(SOFT_MESSAGES)
        await update.message.reply_sticker(sticker)
        await update.message.reply_text(message)

    elif text == "📞 Хочу, чтобы ты позвонил":

    # Ответ ей
    await update.message.reply_text(
        "Я получил сигнал, моя малышка Лика💛\n"
        "Постараюсь позвонить, как только смогу :)"
    )

    # Уведомление тебе
    await context.bot.send_message(
        chat_id=MY_CHAT_ID,
        text="Она хочет, чтобы ты позвонил 🤍"
    )


    elif text == "⏳ Сколько осталось":
        today = date.today()

        if today < DEPARTURE_DATE:
            remaining = (MEETING_DATE - today).days
            reply = (
                "Хээээй! Я ещё никуда не улетел, солнце :)🤍\n"
                "Мы всё ещё рядом💛"
            )
        else:
            remaining = (MEETING_DATE - today).days
            reply = (
                f"До нашей встречи осталось дней: {remaining} 🤍\n"
                "Это на один день меньше, чем вчера, солнышко :)\n"
                "14.06.2026"
            )

        await update.message.reply_text(reply)



# === ЗАПУСК ===
from telegram.ext import MessageHandler, filters
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("days", days))
app.add_handler(CommandHandler("missyou", missyou))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_buttons))

app.run_polling()





