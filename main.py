import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "6001568141:AAHFXdQS2ZRSGOwwNdMnQFmAMFnaoHZEeeo"
PROXY_URL = "socks5://127.0.0.1:10808"

query_count = 25
reset_time = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Used a query', callback_data='used_query')]]
    return InlineKeyboardMarkup(keyboard)

async def used_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global query_count
    query_count -= 1
    await query(update, context)

async def query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global query_count
    await context.bot.answer_inline_query(update.inline_query.id, text=f"You have {query_count} queries left.")

if __name__ == '__main__':

    application = ApplicationBuilder().proxy_url("socks5://127.0.0.1:10808").token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(used_query, pattern='used_query'))

    application.run_polling()
