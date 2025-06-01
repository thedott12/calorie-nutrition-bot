
from telegram import Update
from telegram.ext import ContextTypes
from services.db import save_to_history, get_history

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь текст или фото еды.")

async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    history = get_history(update.effective_user.id)
    if history:
        await update.message.reply_text("\n".join(history))
    else:
        await update.message.reply_text("История пуста.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    result = f"Обработка текста: {text}"
    save_to_history(user_id, result)
    await update.message.reply_text(result)
