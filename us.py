from telebot import types

def check_subscription():
    channel_url = "https://t.me/+5morJrd_bukwZDJl"

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="Bot channel",
            url=channel_url
        )
    )

    return markup
