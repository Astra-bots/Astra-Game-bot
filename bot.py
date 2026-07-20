import os

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from games import games



load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")





def games_keyboard():

    keyboard = []


    for game in games:

        keyboard.append(

            [
                InlineKeyboardButton(

                    game["name"],

                    url=game["link"]

                )
            ]

        )


    return InlineKeyboardMarkup(keyboard)







async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):


    await update.message.reply_text(

        "🎮 به Astra Game خوش آمدی!\n\n"
        "بازی موردنظر خودت را انتخاب کن:",

        reply_markup=games_keyboard()

    )








async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):


    query = update.callback_query

    await query.answer()



async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):


    await update.message.reply_text(

        "از منوی بازی‌ها استفاده کن 🎮"

    )







def main():


    app = Application.builder().token(TOKEN).build()



    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )



    app.add_handler(

        CallbackQueryHandler(info)

    )



    print("Astra Game Started 🎮")



    app.run_polling()






if __name__ == "__main__":

    main()
