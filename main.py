import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/баксик", "/кубик"]]
    await update.message.reply_text(
        "Выбери команду 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def baksik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dogs = [
        "https://images.unsplash.com/photo-1558788353-f76d92427f16",
        "https://images.unsplash.com/photo-1591768575198-88dac53fbd0a",
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e"
    ]
    await update.message.reply_photo(random.choice(dogs))

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_dice()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("баксик", baksik))
app.add_handler(CommandHandler("кубик", dice))

app.run_polling()
