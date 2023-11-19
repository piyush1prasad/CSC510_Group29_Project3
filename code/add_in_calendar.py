##Copyright (c) 2021 Dev Kumar
import helper
import logging
from telebot import types
from datetime import datetime
from telebot_calendar import Calendar, CallbackData
from telebot.types import ReplyKeyboardRemove, CallbackQuery
from datetime import datetime
from code import bot
import json

option = {} # A dictionary for storing temporary user options
dates = {}
messages = {}
# Initialize the calendar with English language
calendar = Calendar()
callback_data = CallbackData("calendar", "action", "year", "month", "day")

def run(message, bot):
    # Read spending data from a JSON file
    
    chat_id = message.chat.id
    messages[chat_id] = {'original_message': message}
    print("The original message stored for chat_id", messages[chat_id])


    # Check if a date has already been selected
    if chat_id in dates and 'date' in dates[chat_id]:
        # If a date is selected, move to category selection
        display_categories(message, bot)
        print("date already stored")
    else:
        # If no date is selected, show the calendar
        helper.read_json()
        
        # Remove any previous temporary choices
        option.pop(chat_id, None)  # remove temp choice

        # Send calendar to user
        now = datetime.now()  # Current date
        
        bot.send_message(chat_id, "Please select a date", reply_markup=calendar.create_calendar(
            name=callback_data.prefix,
            year=now.year,
            month=now.month,
        ),)
        print("date selected")
        



def display_categories(message, bot):
    # Logic to display categories
    print("Inside display categories")
    # Create a keyboard markup with spending categories for user selection
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2

    # Add spending categories to the keyboard
    for c in helper.getSpendCategories():
        markup.add(c)

    # Ask the user to select a category or cancel the operation
    msg = bot.reply_to(message, 'Select Category or Select Cancel to cancel the operation', reply_markup=markup)
    
    # Register the next step handler to process user's choice
    bot.register_next_step_handler(msg, post_category_selection, bot)

# @bot.callback_query_handler(func=lambda call: call.data.startswith(callback_data.prefix))
@bot.callback_query_handler(func=lambda call: True)
def calendar_handler(call: CallbackQuery):
    print("inside calendar handler")
    chat_id = call.message.chat.id
    
    # We Retrieve the original message
    print("retrieving the original message")
    original_message = messages.get(chat_id, {}).get('original_message')

    if not original_message:
        print("Original message not found for chat_id:", chat_id)
        #Handle the case where original_message is not found
        return

    name, action, year, month, day = call.data.split(callback_data.sep)
    #Processing the calendar. Get either the date or None if the buttons are of a different type
    date = calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )
    
    if action == "DAY":
        dates[chat_id] = {'date': date}

        bot.send_message(
            chat_id=call.from_user.id,
            text=f"You have chosen {date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{callback_data}: Day: {date.strftime('%d.%m.%Y')}")
        call.message.text = '/run'  # Or any relevant text
        display_categories(original_message, bot)
    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Cancellation",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{callback_data}: Cancellation")
    


def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        
        # Check if the selected category is valid
        if selected_category not in helper.getSpendCategories():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))
        print(selected_category)
        if selected_category != "Cancel":
            # Store the selected category in the user's options
            option[chat_id] = selected_category

            # Ask the user to enter the amount or cancel the operation
            message = bot.send_message(chat_id, 'How much did you spend on {}? \n(Enter numeric values only) or enter Cancel to cancel the operation'.format(str(option[chat_id])))
            
            # Register the next step handler to process the amount input
            bot.register_next_step_handler(message, post_amount_input, bot, selected_category)
        else :
            text_intro = "Cancelled the operation.\nSelect "
            commands = helper.getExitCommands()
            for c in commands:  # generate help text out of the commands dictionary defined at the top
                text_intro += "/" + c + " to "
                text_intro += commands[c] + "\n\n"
            bot.send_message(chat_id, text_intro)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no! ' + str(e))
        
         # Display available menu options to the user
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, 'Please select a menu option from below:')
        bot.send_message(chat_id, display_text)


def post_amount_input(message, bot, selected_category):
    try:
        chat_id = message.chat.id
        amount_entered = message.text
        print("post_amount_input date recived", option[chat_id])
        # Check if the user canceled the operation
        if amount_entered != "Cancel":
            # Validate and convert the entered amount to a numeric value
            amount_value = helper.validate_entered_amount(amount_entered)  # validate
            
            # Ensure that the amount is not zero
            if amount_value == 0:  # cannot be $0 spending
                raise Exception("Spent amount has to be a non-zero number.")

            # Get the current date and time for the entry
            date_of_entry = dates[chat_id]['date'].strftime(helper.getDateFormat() + ' ' + helper.getTimeFormat())
            date_str, category_str, amount_str = str(date_of_entry), str(option[chat_id]), str(amount_value)
            
            # Add the user's expenditure record to the JSON data
            helper.write_json(add_user_record(chat_id, "{},{},{}".format(date_str, category_str, amount_str)))
            
            # Inform the user that the expenditure has been recorded
            bot.send_message(chat_id, 'The following expenditure has been recorded: You have spent ${} for {} on {}'.format(amount_str, category_str, date_str))
            
            # Display the remaining budget for the selected category
            helper.display_remaining_budget(message, bot, selected_category)
            dates.pop(chat_id, None)
            messages.pop(chat_id, None)
        else :

            # Inform the user that the operation has been canceled
            text_intro = "Cancelled the operation.\nSelect "
            commands = helper.getExitCommands()
            for c in commands:  # generate help text out of the commands dictionary defined at the top
                text_intro += "/" + c + " to "
                text_intro += commands[c] + "\n\n"
            bot.send_message(chat_id, text_intro)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))


def add_user_record(chat_id, record_to_be_added):
    # Read the existing user data from the JSON file
    user_list = helper.read_json()
    
    # Check if the user's data exists, and create a new record if not
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    # Append the new record to the user's data
    user_list[str(chat_id)]['data'].append(record_to_be_added)
    return user_list
bot.polling(none_stop=True)