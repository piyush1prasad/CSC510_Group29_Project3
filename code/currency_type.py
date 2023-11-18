import helper
import logging
from telebot import types
from datetime import datetime


option = {}  # A dictionary for storing temporary user options


def run(message, bot):
    # Read spending data from a JSON file
    helper.read_json()
    chat_id = message.chat.id

    # Remove any previous temporary choices
    option.pop(chat_id, None)  # remove temp choice

    # Create a keyboard markup with spending categories for user selection
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    
    # Add spending categories to the keyboard
    for c in helper.getCurrencyType():
        markup.add(c)
    
    # Ask the user to select a category or cancel the operation
    msg = bot.reply_to(message, 'Select Category or Select Cancel to cancel the operation', reply_markup=markup)
    
    # Register the next step handler to process user's choice
    bot.register_next_step_handler(msg, post_category_selection, bot)


def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        
        # Check if the selected category is valid
        if selected_category not in helper.getCurrencyType():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))
        print(selected_category)
        if selected_category != "Cancel":
            user_list = helper.read_json()
            fromCurrency = user_list[str(chat_id)]['curr_type']
            if selected_category != fromCurrency:
                user_list[str(chat_id)]['curr_type'] = selected_category
                if user_list[str(chat_id)]['data']:
                    updatedData = list()
                    for expense in user_list[str(chat_id)]['data']:
                        amount = expense.split(",")[-1]
                        updatedAmount = helper.convertCurrency(fromCurrency, selected_category, amount)
                        # print(amount, updatedAmount)
                        # expense.replace(amount, updatedAmount)
                        updatedData.append(','.join(expense.split(',')[:-1])+','+updatedAmount)
                        print(updatedData)
                    user_list[str(chat_id)]['data'] = updatedData
                if user_list[str(chat_id)]['income']:
                    user_list[str(chat_id)]['income'] = helper.convertCurrency(fromCurrency, selected_category, user_list[str(chat_id)]['income'])
                if user_list[str(chat_id)]['budget']['overall']:
                    user_list[str(chat_id)]['budget']['overall'] = helper.convertCurrency(fromCurrency, selected_category, user_list[str(chat_id)]['budget']['overall'])
                if user_list[str(chat_id)]['budget']['category']:
                    for key in user_list[str(chat_id)]['budget']['category']:
                        user_list[str(chat_id)]['budget']['category'][key] = helper.convertCurrency(fromCurrency, selected_category, user_list[str(chat_id)]['budget']['category'][key])
                helper.write_json(user_list)
                bot.send_message(chat_id, 'Currency Type Updated to '+selected_category+' from '+fromCurrency)
            else:
                bot.send_message(chat_id, 'Currency Type select is same as before: '+selected_category)
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