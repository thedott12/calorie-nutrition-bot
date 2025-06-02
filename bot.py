import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import text_handler, photo_handler
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# ВРЕМЕННАЯ ОТЛАДКА — покажет токен в логах Render
print(f"TOKEN = {TOKEN}")

# Проверка, что токен получен
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set. Check your .env file.")

# Создание приложения Telegram
application = ApplicationBuilder().token(TOKEN).build()

# Регистрация обработчиков
application.add_handler(CommandHandler("start", text_handler.start_command))
application.add_handler(CommandHandler("history", text_handler.history_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler.handle_text))
application.add_handler(MessageHandler(filters.PHOTO, photo_handler.handle_photo))
