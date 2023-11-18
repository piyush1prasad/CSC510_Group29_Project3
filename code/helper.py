#Copyright (c) 2021 Dev Kumar
import re
import json
import os
import requests
from datetime import datetime

choices = ['Date', 'Category', 'Cost']
plot = ['Bar with budget', 'Pie','Bar without budget', 'Cancel']
spend_display_option = ['Day', 'Month','Cancel']
spend_estimate_option = ['Next day', 'Next month', 'Cancel']
update_options = {
    'continue': 'Continue',
    'exit': 'Exit'
}

yes_or_no = {
    'yes': 'Yes',
    'no': 'No'
}

options = {
    'update': 'Add/Update',
    'view': 'View',
    'delete': 'Delete',
    'cancel': 'Cancel'
}

budget_types = {
    'overall': 'Overall Budget',
    'category': 'Category-Wise Budget',
    'cancel' : 'Cancel'
}

data_format = {
    'curr_type': 'USD',
    'data': [],
    'income': None,
    'budget': {
        'overall': None,
        'category': None
    }
}

category_options = {
    'add': 'Add',
    'delete': 'Delete',
    'view': 'Show Categories',
    'cancel' : 'Cancel'
}

# set of implemented commands and their description
commands = {
    'menu': 'Display this menu',
    'curr_type': 'Chnage currency type',
    'income': 'Add/Update/View/Delete income',
    'add': 'Record/Add a new spending',
    'add_recurring': 'Add a new recurring expense for future months',
    'display': 'Show sum of expenditure for the current day/month',
    'estimate': 'Show an estimate of expenditure for the next day/month',
    'history': 'Display spending history',
    'delete': 'Clear/Erase all your records',
    'edit': 'Edit/Change spending details',
    'budget': 'Add/Update/View/Delete budget',
    'category': 'Add/Delete/Show custom categories',
    'summary': 'show summary of spending',
    'exit' : 'Exit from MyDollarBot'
}
exit_commands = {
    'menu': 'Display the menu'
}


dateFormat = '%d-%b-%Y'
timeFormat = '%H:%M'
monthFormat = '%b-%Y'

# Currency rates
user_currency_type = dict()
currency_rates = dict()
currency_types = [
    'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
    'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
    'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF',
    'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF',
    'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP',
    'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
    'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
    'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
    'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
    'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR',
    'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
    'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR',
    'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD',
    'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SYP', 'SZL', 'THB', 'TJS',
    'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD',
    'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU',
    'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']


# function to load .json expense record data
def read_json():
    try:
        if not os.path.exists('expense_record.json'):
            with open('expense_record.json', 'w') as json_file:
                json_file.write('{}')
            return json.dumps('{}')
        elif os.stat('expense_record.json').st_size != 0:
            with open('expense_record.json') as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")


def write_json(user_list):
    try:
        with open('expense_record.json', 'w') as json_file:
            json.dump(user_list, json_file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Sorry, the data file could not be found.')


def setUserCurr(chat_id):
    user_list = read_json()
    user_currency_type[str(chat_id)]['curr_type'] = user_list[str(chat_id)]['curr_type']


def getUserCurr(chat_id):
    if not user_currency_type[str(chat_id)]:
        user_list = read_json()
        user_currency_type[str(chat_id)]['curr_type'] = user_list[str(chat_id)]['curr_type']
    return user_currency_type[str(chat_id)]['curr_type']


def getCurrencyType():
    return currency_types


def setCurrencyRates():
    API_KEY = '1932e67af6cdd38f9a1df48dbed973e1'
    url = 'http://data.fixer.io/api/latest?access_key=' + API_KEY
    global currency_rates
    data = requests.get(url).json()
    # Extracting only the rates from the json data
    currency_rates = data["rates"]


def convertCurrency(fromCurrency, toCurrency, amount):
    amount = float(amount)
    if fromCurrency != 'EUR':
        amount = amount / currency_rates[fromCurrency]
    amount = round(amount * currency_rates[toCurrency], 2)
    return str(amount)


def validate_entered_amount(amount_entered):
    if amount_entered is None:
        return 0
    if re.match("^[1-9][0-9]{0,14}\\.[0-9]*$", amount_entered) or re.match("^[1-9][0-9]{0,14}$", amount_entered):
        amount = round(float(amount_entered), 2)
        if amount > 0:
            return str(amount)
    return 0


def validate_entered_duration(duration_entered):
    if duration_entered is None:
        return 0
    if re.match("^[1-9][0-9]{0,14}", duration_entered):
        duration = int(duration_entered)
        if duration > 0:
            return str(duration)
    return 0


def getUserHistory(chat_id):
    data = getUserData(chat_id)
    if data is not None:
        return data['data']
    return None


def getUserData(chat_id):
    user_list = read_json()
    if user_list is None:
        return None
    if (str(chat_id) in user_list):
        return user_list[str(chat_id)]
    return None


def throw_exception(e, message, bot, logging):
    logging.exception(str(e))
    bot.reply_to(message, 'Oh no! ' + str(e))


def createNewUserRecord():
    return data_format


def getOverallBudget(chatId):
    data = getUserData(chatId)
    if data is None:
        return None
    return data['budget']['overall']


def getTotalIncome(chatId):
    data = getUserData(chatId)
    if data is None:
        return None
    return data['income']


def getCategoryBudget(chatId):
    data = getUserData(chatId)
    if data is None:
        return None
    return data['budget']['category']


def getCategoryBudgetByCategory(chatId, cat):
    if not isCategoryBudgetByCategoryAvailable(chatId, cat):
        return None
    data = getCategoryBudget(chatId)
    return data[cat]


def canAddBudget(chatId):
    return (getOverallBudget(chatId) is None) and (getCategoryBudget(chatId) is None)


def isOverallBudgetAvailable(chatId):
    return getOverallBudget(chatId) is not None


def isTotalIncomeAvailable(chatId):
    return getTotalIncome(chatId) is not None 


def isCategoryBudgetAvailable(chatId):
    return getCategoryBudget(chatId) is not None


def isCategoryBudgetByCategoryAvailable(chatId, cat):
    data = getCategoryBudget(chatId)
    if data is None:
        return False
    return cat in data.keys()


def display_remaining_budget(message, bot, cat):
    chat_id = message.chat.id
    if isOverallBudgetAvailable(chat_id):
        display_remaining_overall_budget(message, bot)
    elif isCategoryBudgetByCategoryAvailable(chat_id, cat):
        display_remaining_category_budget(message, bot, cat)


def display_remaining_overall_budget(message, bot):
    print('here')
    chat_id = message.chat.id
    remaining_budget = calculateRemainingOverallBudget(chat_id)
    print("here", remaining_budget)
    if remaining_budget >= 0:
        msg = '\nRemaining Overall Budget is $' + str(remaining_budget)
    else:
        msg = '\nBudget Exceded!\nExpenditure exceeds the budget by $' + str(remaining_budget)[1:]
    bot.send_message(chat_id, msg)


def calculateRemainingOverallBudget(chat_id):
    budget = getOverallBudget(chat_id)
    history = getUserHistory(chat_id)
    query = datetime.now().today().strftime(getMonthFormat())
    queryResult = [value for index, value in enumerate(history) if str(query) in value]

    return float(budget) - calculate_total_spendings(queryResult)


def calculate_total_spendings(queryResult):
    total = 0

    for row in queryResult:
        s = row.split(',')
        total = total + float(s[2])
    return total


def display_remaining_category_budget(message, bot, cat):
    chat_id = message.chat.id
    remaining_budget = calculateRemainingCategoryBudget(chat_id, cat)
    if remaining_budget >= 0:
        msg = '\nRemaining Budget for ' + cat + ' is $' + str(remaining_budget)
    else:
        msg = '\nBudget for ' + cat + ' Exceded!\nExpenditure exceeds the budget by $' + str(abs(remaining_budget))
    bot.send_message(chat_id, msg)


def calculateRemainingCategoryBudget(chat_id, cat):
    budget = getCategoryBudgetByCategory(chat_id, cat)
    history = getUserHistory(chat_id)
    query = datetime.now().today().strftime(getMonthFormat())
    queryResult = [value for index, value in enumerate(history) if str(query) in value]

    return float(budget) - calculate_total_spendings_for_category(queryResult, cat)


def calculate_total_spendings_for_category(queryResult, cat):
    total = 0

    for row in queryResult:
        s = row.split(',')
        if cat == s[1]:
            total = total + float(s[2])
    return total


def getSpendCategories():
    with open("categories.txt", "r") as tf:
        spend_categories = tf.read().split(',')
    return spend_categories


def getplot():
    return plot


def getSpendDisplayOptions():
    return spend_display_option


def getSpendEstimateOptions():
    return spend_estimate_option


def getCommands():
    return commands


def getDateFormat():
    return dateFormat


def getTimeFormat():
    return timeFormat


def getMonthFormat():
    return monthFormat


def getChoices():
    return choices


def getOptions():
    return options


def getBudgetTypes():
    return budget_types


def getUpdateOptions():
    return update_options


def getYesNoOptions():
    return yes_or_no


def getCategoryOptions():
    return category_options


def getExitCommands():
    return exit_commands
