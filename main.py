# -*- coding: utf-8 -*-
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from app import render_quote
from dotenv import load_dotenv
import os

TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!, Please mention me to a message so i can quote it.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!, Please mention me to a message so i can quote it.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type in ['group', 'supergroup']:
        if BOT_USERNAME in text: 
            replied_message = update.message.reply_to_message
            if replied_message:
               
                replied_user_first_name = replied_message.from_user.first_name
                replied_user_last_name = replied_message.from_user.last_name or ""  

                full_name = f"{replied_user_first_name} {replied_user_last_name}".strip()

                replied_text = replied_message.text
    
                image_path = render_quote(replied_text, full_name)

                with open(image_path, 'rb') as photo:
                    await update.message.reply_photo(photo)

                os.remove(image_path)

            else:
                await update.message.reply_text('')
    else:
        await update.message.reply_text("Sorry, im only designed to work in groups.")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('quote', start_command))
    app.add_handler(CommandHandler('start', custom_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)