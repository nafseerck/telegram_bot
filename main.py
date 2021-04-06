import Constants as keys
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import  Responses as R
import json

updater = Updater(token="1541105950:AAGrzH31WqDwXIK7cr4ejT8mDYr39oOTseY")
dispatcher = updater.dispatcher

print("Bot Started....")

def start_command(update, context):
    update.message.reply_text('Type something random to get started !')

def help_command(update, context):
    update.message.reply_text('If you need help, please let us know  !')

def villa_command(update, context):
    update.message.reply_text('What kind of villas are you looking for ?')

def townhouses_command(update, context):
    update.message.reply_text('What kind of townhouses are you looking for ?')

def apartment_command(update, context):
    update.message.reply_text('What kind of apartments are you looking for ?')

def flats_command(update, context):
    update.message.reply_text('What kind of flats are you looking for ?')

def opt(update, context):
    button1 = [
        [InlineKeyboardButton("Villas", callback_data="Villas", url=""),],
         [InlineKeyboardButton("Flats", callback_data="Flats", url="")],
         [InlineKeyboardButton("Apartments", callback_data="Apartments", url="")]
        ]

    # print(button1[0])
    reply_markup = InlineKeyboardMarkup(button1)

    # print(reply_markup['update_id'])

    update.message.reply_text(text="What Kind of Property are you looking for ?", reply_markup=reply_markup)



def villas_budget(update, context):



    button3 = [
        [InlineKeyboardButton("100k-500k", callback_data="100k-500k", url="indusre.com"),
         InlineKeyboardButton("500k-1M", callback_data="500k-1M", url=""),],
         [InlineKeyboardButton("1M-1.5M", callback_data="1M-1.5M", url="")]
        ]

    selection1 = button3[1]
    print(selection1)
    reply_markup = InlineKeyboardMarkup(button3)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)



def apartments_budget(update, context):
    button4 = [
        [InlineKeyboardButton("100k-500k", callback_data="100k-500k", url="indusre.com"),
         InlineKeyboardButton("500k-1M", callback_data="500k-1M", url=""), ],
        [InlineKeyboardButton("1M-1.5M", callback_data="1M-1.5M", url="")]
    ]

    reply_markup = InlineKeyboardMarkup(button4)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)

def townhouses_budget(update, context):
    button5 = [
        [InlineKeyboardButton("100k-500k", callback_data="100k-500k", url="indusre.com"),
         InlineKeyboardButton("500k-1M", callback_data="500k-1M", url=""), ],
        [InlineKeyboardButton("1M-1.5M", callback_data="1M-1.5M", url="")]
    ]

    reply_markup = InlineKeyboardMarkup(button5)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)

def townhouses_location(update, context):
    button6 = [
        [InlineKeyboardButton("Bur Dubai", callback_data="Bur Dubai", url="indusre.com"),
         InlineKeyboardButton("Deira", callback_data="Deira", url=""), ],
        [InlineKeyboardButton("Jumeirah Lake Towers", callback_data="Jumeirah Lake Towers", url="")]
        [InlineKeyboardButton("Abu Dhabi Island", callback_data="Abu Dhabi Island", url="")]
        [InlineKeyboardButton("Al Bustan", callback_data="Al Bustan", url="")]
        [InlineKeyboardButton("Burj Khalifa", callback_data="Burj Khalifa", url="")]
        [InlineKeyboardButton("Dubai Marina", callback_data="Dubai Marina", url="")]

    ]

    reply_markup = InlineKeyboardMarkup(button6)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)

def apartment_location(update, context):
    button7 = [
        [InlineKeyboardButton("Bur Dubai", callback_data="Bur Dubai", url="indusre.com"),
         InlineKeyboardButton("Deira", callback_data="Deira", url=""), ],
        [InlineKeyboardButton("Jumeirah Lake Towers", callback_data="Jumeirah Lake Towers", url="")]
        [InlineKeyboardButton("Abu Dhabi Island", callback_data="Abu Dhabi Island", url="")]
        [InlineKeyboardButton("Al Bustan", callback_data="Al Bustan", url="")]
        [InlineKeyboardButton("Burj Khalifa", callback_data="Burj Khalifa", url="")]
        [InlineKeyboardButton("Dubai Marina", callback_data="Dubai Marina", url="")]

    ]

    reply_markup = InlineKeyboardMarkup(button7)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)

def villas_location(update, context):
    button8 = [
        [InlineKeyboardButton("Bur Dubai", callback_data="Bur Dubai", url="indusre.com"),
         InlineKeyboardButton("Deira", callback_data="Deira", url=""), ],
        [InlineKeyboardButton("Jumeirah Lake Towers", callback_data="Jumeirah Lake Towers", url="")]
        [InlineKeyboardButton("Abu Dhabi Island", callback_data="Abu Dhabi Island", url="")]
        [InlineKeyboardButton("Al Bustan", callback_data="Al Bustan", url="")]
        [InlineKeyboardButton("Burj Khalifa", callback_data="Burj Khalifa", url="")]
        [InlineKeyboardButton("Dubai Marina", callback_data="Dubai Marina", url="")]

    ]

    reply_markup = InlineKeyboardMarkup(button8)
    update.message.reply_text(text="What is the budget you are looking for ?", reply_markup=reply_markup)



def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused erro {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("Services", opt))
    dp.add_handler(CommandHandler("Villas", villas_budget))
    dp.add_handler(CommandHandler("Apartments", apartments_budget))
    dp.add_handler(CommandHandler("Townhouses", townhouses_budget))
    dp.add_handler(CommandHandler("townhouseslocation", townhouses_location))
    dp.add_handler(CommandHandler("villaslocation", villas_location))
    dp.add_handler(CommandHandler("apartmentlocation", apartment_location))





    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()