import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.environ.get("TOKEN")

quotes = {
    "💪 Discipline": [
        "Discipline is the bridge between goals and accomplishment.",
        "Strength is not about never falling, but getting up every time.",
        "Discomfort today is growth tomorrow.",
        "One small step every day is a big distance over a year.",
        "Don't wait for the right moment. Create it.",
    ],
    "📈 Marketing": [
        "Data without action is just numbers.",
        "The best marketing is the one you don't notice.",
        "Test everything. Trust only the numbers.",
        "If CAC is growing — you're losing focus somewhere.",
        "A great offer beats a perfect creative every time.",
    ],
    "🧠 Mindset": [
        "Your actions today are your life tomorrow.",
        "Focus on the process — results will follow.",
        "Success is the sum of small efforts repeated day after day.",
        "Don't compare yourself to others. Compare yourself to who you were yesterday.",
        "A problem is just a task without a solution. Find the solution.",
    ],
    "🔥 Success": [
        "Success favors the prepared.",
        "Big results start with small decisions.",
        "Do today what others won't — live tomorrow how others can't.",
        "Every day is a new chance to be better.",
        "Results are a reflection of your habits.",
    ],
}

main_keyboard = [["💪 Discipline", "📈 Marketing"], ["🧠 Mindset", "🔥 Success"], ["🔙 Main menu"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
    await update.message.reply_text("Hey! Choose a category 👇", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in quotes:
        quote = random.choice(quotes[text])
        await update.message.reply_text(f"💬 {quote}")
    elif text == "🔙 Main menu":
        reply_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
        await update.message.reply_text("Choose a category 👇", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Please choose a category from the menu 👇")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()