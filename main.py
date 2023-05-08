import requests
import telebot
from telebot import apihelper
Token = ""
bot = telebot.TeleBot(Token)


# Replace <CHAT_ID> with the chat ID you want to send the number to
#
#


# Define a dictionary to store the chat ID and message for each user
user_data = {}


@bot.message_handler(commands=['heyyyy'])
def send_message_to_user(message):
    # Save the user's chat ID for later use
    user_chat_id = message.chat.id

    # Send a message asking the user for the chat ID and message text
    bot.send_message(
        user_chat_id, "Please enter the chat ID of the user you want to send a message to:")

    # Set the next message handler to listen for the user's chat ID input
    bot.register_next_step_handler(message, get_chat_id, user_chat_id)


def get_chat_id(message, user_chat_id):
    # Save the user's chat ID input
    chat_id = message.text

    # Save the chat ID for later use
    user_data[user_chat_id] = {'chat_id': chat_id}

    # Send a message asking the user for the message text
    bot.send_message(
        user_chat_id, "Please enter the message you want to send:")

    # Set the next message handler to listen for the user's message input
    bot.register_next_step_handler(message, get_message_text, user_chat_id)


def get_message_text(message, user_chat_id):
    # Save the user's message input
    message_text = message.text

    # Save the message for later use
    user_data[user_chat_id]['message'] = message_text
    try:
        # Send a confirmation message to the user
        bot.send_message(
            user_chat_id, f"Sending message '{message_text}' to chat ID {user_data[user_chat_id]['chat_id']}")

        # Send the message to the specified chat ID
        bot.send_message(user_data[user_chat_id]['chat_id'], message_text)

    except apihelper.ApiTelegramException as e:

        # Handle the case when the chat ID is not valid
        bot.send_message(
            user_chat_id, f"Error: Invalid chat ID. Please enter a valid chat ID.")


#
#
#
#
CHAT_ID = 962498311


@bot.message_handler(commands=['send_UTR'])
def ask_for_number(message):

    user_chat_id = message.chat.id
    user_first_name = message.from_user.first_name

    try:

        bot.send_message(
            user_chat_id, "Please enter the number you want to send:")

        bot.register_next_step_handler(
            message, send_number, user_chat_id, user_first_name)
    except apihelper.ApiTelegramException as e:
        # Handle the case when the bot sends messages too quickly
        bot.send_message(
            user_chat_id, "Error: Please wait a moment before sending another command.")


def send_number(message, user_chat_id, user_first_name):
    try:

        number = int(message.text)

        # Send the number and user's name to the specified chat ID
        bot.send_message(
            CHAT_ID, f"{user_chat_id},{user_first_name} sent: {number}")

        bot.send_message(
            user_chat_id, f"Number: {number} if this UTR number is right then you wifi is activated")
    except ValueError:

        bot.send_message(user_chat_id, "Invalid input. Please enter a number.")


@bot.message_handler(commands=['k'])
def send_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your chat ID is {chat_id}")


@bot.message_handler(['start', 'new', 'name'])
def start(message):
    bot.reply_to(message, """ 
    /abhay -> My name
    /golu -> My name
    /madhu -> My name
    /ansil -> My name
    /tanishka -> My name
    /other -> My name
    """)


@bot.message_handler(['abhay'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_month
    /3_month
    """)


@bot.message_handler(['golu'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_month
    /3_month
    """)


@bot.message_handler(['ansil'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_month
    /3_month
    """)


@bot.message_handler(['madhu'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_month
    /3_month
    """)


@bot.message_handler(['pay'])
def start(message):
    bot.reply_to(message, """
    pay to this UPI
    """)
    bot.reply_to(message, """
    paytmqr2810050501011xniujoadq6d@paytm
    """)
    bot.reply_to(message, """
    name - milkii


    you can pay by PhonePay ,Google Pay , Paytm

    after payment send your last 4 digit URT number

    /send_UTR

    """)


@bot.message_handler(['tanishka'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_month
    /3_month
    """)


@bot.message_handler(['other'])
def start(message):
    bot.reply_to(message, """
    Choose a plan for recharge
    /1_day
    /1_week
    /new_connection
    """)


@bot.message_handler(['1_day'])
def start(message):
    bot.reply_to(message, """
    your 1 day pack is 25 rs (this is valid till night 12:01 am)
    /pay
    """)


@bot.message_handler(['1_week'])
def start(message):
    bot.reply_to(message, """
    your 1 week pack is 99rs
    /pay
    """)


@bot.message_handler(['new_connection'])
def start(message):
    bot.reply_to(message, """
    if you have personal router then pay only 800rs

    if you don't have personal router then pay 1500 rs

    /pay
    """)


@bot.message_handler(commands=['help'])
def handle_1_month(message):
    if message.from_user.first_name.lower() == 'kumar':
        bot.reply_to(message, """
        /heyyyy -> When I want to send message to any chat-ID
        /k -> know my chat-ID
        all person username is-
        ansil abhay madhu tanishka vijay

        all person command name is-
        ansil abhay madhu tanishka golu

        /akk -> when ansil click then he can recharge anyones
        """)


@bot.message_handler(commands=['akk'])
def handle_1_month(message):
    if message.from_user.first_name.lower() == 'ansil':
        bot.reply_to(message, """
        you can recharge anyone's ,you just /pay and send the UTR number and this activated
        
        """)


@bot.message_handler(commands=['1_month'])
def handle_1_month(message):
    if message.from_user.first_name.lower() == 'ansil':
        bot.reply_to(message, """
        Ansil your 1month plan is 200 rs
        /pay

        pay this and activate your plan
         see /3_month plan""")

    elif message.from_user.first_name.lower() == 'abhay':
        bot.reply_to(message, """
        Abhay your 1month plan is 200 rs
        /pay
        pay this and activate your plan
        see /3_month plan""")

    elif message.from_user.first_name.lower() == 'madhu':
        bot.reply_to(message, """
        Madhu your 1month plan is 200 rs
        /pay
        pay this and activate your plan
        see /3_month plan""")

    elif message.from_user.first_name.lower() == 'tanishka':
        bot.reply_to(message, """
        Tanishka your 1month plan is 200 rs
        /pay
        pay this and activate your plan
        see /3_month plan""")

    elif message.from_user.first_name.lower() == 'vijay':
        bot.reply_to(message, """
        Golu your 1month plan is 90 rs
        /pay
        pay this and activate your plan
        see /3_month plan""")
    else:
        bot.reply_to(message, """you cannot see other's plan""")


@bot.message_handler(commands=['3_month'])
def handle_1_month(message):
    if message.from_user.first_name.lower() == 'ansil':
        bot.reply_to(message, """
        Ansil your 3 month plan is 600 rs
        /pay
        pay this and activate your plan
        see /1_month plan""")

    elif message.from_user.first_name.lower() == 'abhay':
        bot.reply_to(message, """
        Abhay your 3 month plan is 600 rs
        /pay
        pay this and activate your plan
        see /1_month plan""")

    elif message.from_user.first_name.lower() == 'madhu':
        bot.reply_to(message, """
        Madhu your 3 month plan is 600 rs
        /pay
        pay this and activate your plan
        see /1_month plan""")

    elif message.from_user.first_name.lower() == 'tanishka':
        bot.reply_to(message, """
        Tanishka your 3 month plan is 600 rs
        /pay
        pay this and activate your plan
        see /1_month plan""")

    elif message.from_user.first_name.lower() == 'vijay':
        bot.reply_to(message, """
        Golu your 3 month plan is 270 rs
        /pay
        pay this and activate your plan
        see /1_month plan""")


bot.polling()
