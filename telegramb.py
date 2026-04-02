from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    translated = GoogleTranslator(source='en', target='kn').translate(text)

    await update.message.reply_text(translated)

app = ApplicationBuilder().token("hi hi hided").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

app.run_polling()