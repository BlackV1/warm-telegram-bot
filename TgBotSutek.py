import random
from datetime import date
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup

# === НАСТРОЙКИ ===
TOKEN = "8220445421:AAFj30coFLuk330NJ74KywUqPttW12wXPlc"
MEETING_DATE = date(2026, 6, 13)
DEPARTURE_DATE = date(2026, 2, 15)
MY_CHAT_ID = 1194574842
LIKA_CHAT_ID = 1289384192
HALF_SENT = False
MONTH_SENT = False
WEEK_SENT = False

unused_memories = []

MEMORY_PHOTOS = [
    ("AgACAgIAAxkBAAFC6JNpmZN2MBCFQwHInXjYkjSkJZsQQQACKhdrG1XdyEj5KU_zYpAmcgEAAwIAA3MAAzoE", "Ты себе на этом фото не очень нравишься, но я его так люблю💛"),
    ("AgACAgIAAxkBAAFC6J9pmZPwAxW7bW8rByAHqrxOoNN5hAACORdrG1XdyEhM6YLWInyOCwEAAwIAA3MAAzoE", "Ооо, смотри! А это мы в Астане💛"),
    ("AgACAgIAAxkBAAFC6KhpmZRgM8LZKTsVvaE24TDEJu8zPAACQRdrG1XdyEhsmLm4jcAWcAEAAwIAA3MAAzoE", "Теплый осенний день, когда мы с тобой пошли на терренкур и взяли поесть и термос💛"),
    ("AgACAgIAAxkBAAFC6LVpmZS3sjbe4B6Js1H61NNFl7SX-AACSRdrG1XdyEja-4HXLbtiVwEAAwIAA3MAAzoE", "Твоя любимая фотка💛 Новый год в Павлодаре :)"),
    ("AgACAgIAAxkBAAFC6L1pmZUI9r3Ndsxm7VphYQhwbrWakgACTRdrG1XdyEjcX_JRWjg6NwEAAwIAA3MAAzoE", "Моя умничка🥹🥹🥹"),
    ("AgACAgIAAxkBAAFC6MNpmZVxqCUylfDJ-tp86LCMF2ZycgACVRdrG1XdyEg2kGkEc-QBmQEAAwIAA3MAAzoE", "Оп, а это мой коллаж, помнишь его?))))"),
    ("AgACAgIAAxkBAAFC6NVpmZXEqDrKaZv0LTn83RIDaJrplwACVxdrG1XdyEgvkDVilRMtBAEAAwIAA3MAAzoE", "А это мы с тобой на фоне крутого Султана Сутека :) Интересно, мой постер там еще стоит?)"),
    ("AgACAgIAAxkBAAFC6N5pmZZG0BqKGzeq3oaVvrqHv6Eo2AACWhdrG1XdyEijFMzLz9fC4QEAAwIAA3MAAzoE", "АХХАХАХАХАХХАХА, ну это без комментариев"),
    ("AgACAgIAAxkBAAFC6OhpmZaWDLjpjqQul2Y2Shu5WjMargACXhdrG1XdyEhue1qQEyTEAQEAAwIAA3MAAzoE", "Повторим летом?)))))"),
    ("AgACAgIAAxkBAAFC6PZpmZbR4y64hRDwwLVnYXwdU7cf0wACXxdrG1XdyEjnDlbKl8lK0wEAAwIAA3MAAzoE", "Смотри!!! Они тогда еще не знали, что начнут встречаться🤭"),
    ("AgACAgIAAxkBAAFC6P5pmZc_-zxBMs2jlqKfNheW0vHoRAACYhdrG1XdyEgsG5K0JPLvAwEAAwIAA3MAAzoE", "А тут папа по твоим глазам понял, что ты в меня влюблена🤭"),
    ("AgACAgIAAxkBAAFC6QJpmZfR3ZT2ndNDvPnMwnrk40SIvgACaBdrG1XdyEiKhevahNPRFQEAAwIAA3MAAzoE", "Одна из моих любимых фотографий🥹💛"),
    ("AgACAgIAAxkBAAFC6RBpmZh13mfIFAGrSM6p7DYKa8RyKwACbxdrG1XdyEgyJnzA68dIBwEAAwIAA3MAAzoE", "Ооооу маааай"),
    ("AgACAgIAAxkBAAFC6RRpmZjYgt7WIgsc8eAnlhZCX3N2FQACdBdrG1XdyEgjFyVb-ur2JQEAAwIAA3MAAzoE", "СУППППППЕР КАЧКИИИИИИИ"),
    ("AgACAgIAAxkBAAFC6RhpmZkpfmwffTPM0d-I1vL71tsybQACdhdrG1XdyEginChQQlLQ-AEAAwIAA3MAAzoE", "💛💛💛"),
    ("AgACAgIAAxkBAAFC6RppmZlZz193t85HBtgNVwoinOafuQACeBdrG1XdyEgY-OnhhJtxJQEAAwIAA3MAAzoE", "Держимся за ручки🥹🥹🥹"),
    ("AgACAgIAAxkBAAFC6RxpmZmG2EbzZ4YS_Dcr9kUIZNkpjwACeRdrG1XdyEhTtsJ5pCPmKQEAAwIAA3MAAzoE", "ЛИКА позирует на фоне Астаны, лады и трактора, который еще не проехал на фоне"),
    ("AgACAgIAAxkBAAFC6SBpmZm-laje00vgVxumgbN46YJr7AACehdrG1XdyEiHH9IoXL3Q4gEAAwIAA3MAAzoE", "Еще один теплый день💛"),
    ("AgACAgIAAxkBAAFC6ShpmZnvrtH2tYTMpvBYfWHuGEdYTAACexdrG1XdyEgTCuMIJA1LygEAAwIAA3MAAzoE", "Дваа очкарика💛🥸"),
]

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
    "Прилечь бы сейчас с тобой в обнимку",
    "Мы друг у друга в приоритете, любимка :3",
    "Я всегда думаю о тебе, как Форрест думает о Дженни",
    "Представь, как мы будем обниматься в аэропорту🫂❤️‍🩹",
    "Люби меня люби, жарким огнем, ночью и днем, сердце сжигая.."
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

def format_remaining_days(days):
    weeks = days // 7
    remaining_days = days % 7

    if weeks > 0:
        return f"{weeks} недель и {remaining_days} дней"
    else:
        return f"{remaining_days} дней"

def persistent_keyboard():
    keyboard = [
        ["Мне тебя не хватает...💛", "⏳ Сколько осталось", "📞 Хочу, чтобы ты позвонил"]
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

def schedule_weekly_messages(job_queue):

    SECONDS_IN_WEEK = 7 * 24 * 60 * 60

    for _ in range(3):  # 3 сообщения в неделю
        day_offset = random.randint(0, 6)
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)

        first_time = (
            day_offset * 24 * 60 * 60 +
            hour * 60 * 60 +
            minute * 60
        )

        job_queue.run_repeating(
            auto_message,
            interval=SECONDS_IN_WEEK,
            first=first_time
        )

# === КОМАНДЫ ===
async def auto_message(context: ContextTypes.DEFAULT_TYPE):
    sticker = random.choice(STICKERS)
    message = random.choice(SOFT_MESSAGES)

    await context.bot.send_sticker(chat_id=LIKA_CHAT_ID, sticker=sticker)
    await context.bot.send_message(chat_id=LIKA_CHAT_ID, text=message)

async def days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = date.today()
    remaining = (MEETING_DATE - today).days

    # если дата уже прошла — показываем 0
    if remaining < 0:
        remaining = 0

    time_text = format_remaining_days(remaining)

    text = (
        f"До нашей встречи осталось:{time_text}🤍\n"
        "Мы на шаг ближе к нашей встрече🥹"
    )

    await update.message.reply_text(text)

async def milestone_message(context: ContextTypes.DEFAULT_TYPE):
    today = date.today()
    remaining = (MEETING_DATE - today).days

    if remaining > 0 and remaining % 10 == 0:

        message_text = (
            "💛 СООООЛНЫШКООООО, Ещё один рубеж пройден\n"
            f"До нашей встречи осталось {remaining} дней 🤍"
        )

        # ей
        await context.bot.send_message(chat_id=LIKA_CHAT_ID, text=message_text)

        # тебе
        await context.bot.send_message(chat_id=MY_CHAT_ID, text=message_text)

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

async def special_milestones(context: ContextTypes.DEFAULT_TYPE):
    global HALF_SENT, MONTH_SENT, WEEK_SENT

    today = date.today()
    remaining = (MEETING_DATE - today).days

    if remaining <= 0:
        return

    total_days = (MEETING_DATE - DEPARTURE_DATE).days

    # 💛 Половина пути
    if not HALF_SENT and remaining <= total_days // 2:
        HALF_SENT = True

        text = (
            "💛УРАААААААААААААААААААА Мы прошли половину путиииииии\n"
            "Теперь мы еще ближе🤍 Просто вспомни как это ощущалось в самом начале. Я, например, думал, что это ну просто невозможно"
        )

        await context.bot.send_message(chat_id=LIKA_CHAT_ID, text=text)
        await context.bot.send_message(chat_id=MY_CHAT_ID, text=text)

    # 🌙 Последний месяц
    if not MONTH_SENT and remaining <= 30:
        MONTH_SENT = True

        text = (
            "🌙 УРААААААААААААААААААА Начался последний месяц до нашей встречи 🤍\n"
            "Скоро мы будем рядом"
        )

        await context.bot.send_message(chat_id=LIKA_CHAT_ID, text=text)
        await context.bot.send_message(chat_id=MY_CHAT_ID, text=text)

    # ✨ Последняя неделя
    if not WEEK_SENT and remaining <= 7:
        WEEK_SENT = True

        text = (
            "✨СООООЛНЫШКООООООООООООО, Финальная неделя\n"
            "Скоро мы будем рядом🤍"
        )

        await context.bot.send_message(chat_id=LIKA_CHAT_ID, text=text)
        await context.bot.send_message(chat_id=MY_CHAT_ID, text=text)

async def weekly_memory(context):
    global unused_memories

    # Если список закончился — начинаем заново
    if not unused_memories:
        unused_memories = MEMORY_PHOTOS.copy()
        random.shuffle(unused_memories)

    photo_id, caption = unused_memories.pop()

    # 📩 Ей
    await context.bot.send_photo(
        chat_id=LIKA_CHAT_ID,
        photo=photo_id,
        caption=caption
    )

    # 📩 Тебе
    await context.bot.send_photo(
        chat_id=MY_CHAT_ID,
        photo=photo_id,
        caption=caption
    )

async def text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Мне тебя не хватает...💛":
        sticker = random.choice(STICKERS)
        message = random.choice(SOFT_MESSAGES)
        await update.message.reply_sticker(sticker)
        await update.message.reply_text(message)

    elif text == "⏳ Сколько осталось":
        await update.message.chat.send_action("typing")
        await days(update, context)

        await update.message.reply_text(reply)

    elif text == "📞 Хочу, чтобы ты позвонил":

        # Ответ ей
        await update.message.reply_text(
            "Я получил сигнал, моя малышка Лика💛\n"
            "Постараюсь позвонить, как только смогу :)"
        )

        # Уведомление тебе
        await context.bot.send_message(
            chat_id=MY_CHAT_ID,
            text="Сутек, Лика хочет, чтобы ты позвонил 🤍"
        )

# === ЗАПУСК ===
from telegram.ext import MessageHandler, filters
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("days", days))
app.add_handler(CommandHandler("missyou", missyou))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_buttons))

schedule_weekly_messages(app.job_queue)

app.job_queue.run_repeating(
    milestone_message,
    interval=24 * 60 * 60,  # раз в сутки
    first=10
)

app.job_queue.run_repeating(
    weekly_memory,
    interval=7 * 24 * 60 * 60,
    first=10
)

app.job_queue.run_repeating(
    special_milestones,
    interval=24 * 60 * 60,
    first=20
)

app.run_polling()












