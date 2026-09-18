const TelegramBot = require('node-telegram-bot-api');
const token = '8067725589:AAHaOtDiBu8uwk9emqmxrprGOlyXJGItWOM';
const bot = new TelegramBot(token, {polling: true});
bot.on('message', (msg) => {
const chatId = msg.chat.id;
bot.sendMessage(chatId, 'Hello! I am your bot.');
});
