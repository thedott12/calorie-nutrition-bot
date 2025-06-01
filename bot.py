import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import text_handler, photo_handler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler("start", text_handler.start_command))
application.add_handler(CommandHandler("history", text_handler.history_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler.handle_text))
application.add_handler(MessageHandler(filters.PHOTO, photo_handler.handle_photo))