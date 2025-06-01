
from telegram import Update
from telegram.ext import ContextTypes

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Фото получено. Анализ пока не реализован.")
