import random
from datetime import date
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === НАСТРОЙКИ ===
TOKEN = "8220445421:AAFj30coFLuk330NJ74KywUqPttW12wXPlc"
MEETING_DATE = date(2026, 6, 14)

SOFT_MESSAGES = [
    "Если ты это читаешь — я думаю о тебе именно сейчас",
    "Я не рядом физически, но я очень рядом внутри",
    "Ты можешь просто быть. Этого достаточно",
    "Я здесь. Даже если молчу",
    "Этот день — ещё один шаг к нам",
    "Ты не одна. Никогда",
    "Пусть тебе сейчас будет немного теплее",
    "Я верю в тебя так же спокойно, как дышу",
    "Я скучаю по тебе тихо и бережно",
    "Ты — мой дом, даже на расстоянии",
    "14 июня станет нашим днём",
    "Я рядом. Просто знай это"
]

# === КОМАНДЫ ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я здесь 🤍\nИногда буду писать тебе, чтобы напомнить — ты не одна."
    )

async def days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = date.today()
    remaining = (MEETING_DATE - today).days
    if remaining >= 0:
        text = (
            f"До нашей встречи осталось {remaining} дней 🤍\n"
            f"Это на один день меньше, чем вчера.\n"
            f"14.06.2026"
        )
    else:
        text = "Мы уже вместе 🤍"
    await update.message.reply_text(text)

async def missyou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(SOFT_MESSAGES))

# === ЗАПУСК ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("days", days))
app.add_handler(CommandHandler("missyou", missyou))

app.run_polling()

