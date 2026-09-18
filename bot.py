import os from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
TOKEN = '8067725589:AAHaOtDiBu8uwk9emqmxrprGOlyXJGItWOM'
app = Flask(name)
async def start(update, context):
    await update.message.reply_text('Hello. This is a webhook bot.')
    app_builder = Application.builder().token(TOKEN).build()
    app_builder.add_handler(CommandHandler('start', start))
    async def main():
        await app_builder.initialize()
        await app_builder.start()
        webhook_url = 'YOUR_RENDER_URL' + '/' + TOKEN
        await app_builder.bot.set_webhook(webhook_url)
        import asyncio loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        @app.route('/' + TOKEN, methods=['POST'])def webhook():
            json_update = request.get_json()
            update = Update.de_json(json_update, app_builder.bot)
            loop.create_task(app_builder.update_queue.put(update))
            return 'ok', 200 if name == 'main':
            app.run(host='0.0.0.0', port=5000)
            
port=int(os.environ.get('PORT', 5000))
