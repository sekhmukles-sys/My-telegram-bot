import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
TOKEN = '8067725589:AAHaOtDiBu8uwk9emqmxrprG0lyXJGiTWOM' 
async def start(update, context):
    await update.message.reply_text('Hello. This is a webhook bot.')
async def main():
app_builder = Application.builder().token(TOKEN).build()
app_builder.add_handler(CommandHandler('start', start))
await app_builder.initialize()
await app_builder.start()
webhook_url = 'YOUR_RENDER_URL' + '/' + TOKEN
await app_builder.bot.set_webhook(webhook_url)
return app_builder
import asyncio
loop = asyncio.get_event_loop()
app_builder = loop.run_until_complete(main())
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
json_update = request.get_json()
update = Update.de_json(json_update, app_builder.bot)
loop.create_task(app_builder.update_queue.put(update))
return 'ok', 200
if name == 'main':
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
