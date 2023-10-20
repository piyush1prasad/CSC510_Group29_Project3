# About MyDollarBot's /estimate_summary Feature
It reads user spending data from a JSON file and calculates estimations of spendings for a specified day or 
month. It handles errors, provides clear responses, and tracks data availability for daily average spending. 
Overall, it enhances the chatbot's functionality by allowing users to estimate spending.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/estimate_summary.py)

# Code Description
## Functions

1. run(message, bot):
   Reads user spending data from a JSON file using helper.read_json().
   Retrieves the user's spending history.
   If the user has no spending history, it informs them; otherwise, it calls the estimate_total function to calculate and return estimated spending.

2. estimate_total(message, bot):
   Initializes two lists to store estimated spending for the day and month.
   Retrieves the user's spending history, ensuring that data is available.
   Calculates estimated spending for the selected day and month based on a specified number of days.
   Prepares well-formatted text messages with spending estimates.
   Populates the data_estimate_day and data_estimate_month lists with the estimated spending data.
   Returns the estimated spending data or logs and informs the user of any errors.

3. calculate_estimate(queryResult, days_to_estimate):
   Processes the user's spending data, including date, category, and amount, to calculate estimated spending.
   Uses a dictionary to store the total spending per spending category.
   Tracks data availability days for daily average spending calculations.
   Estimates total spending for the specified period and returns the results in a well-structured text format.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /summary into the telegram bot.
