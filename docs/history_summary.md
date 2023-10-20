# About MyDollarBot's history_summary.py file
The provided code in history_summary.py aims to generate a summary of a user's spending history, 
including a textual representation of their spending records and a corresponding histogram chart 
showing monthly spending trends. This code utilizes the helper module to access user data and history, 
and it interacts with the matplotlib library for data visualization.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/history_summary.py)

# Code Description
## Functions
1. run(message, bot):
   This main function is responsible for generating a spending history summary. It begins by reading user data from JSON and retrieving the user's spending history. It then calculates the total spending for each month and constructs a textual summary of spending records. Additionally, it creates a histogram chart to visualize monthly spending trends. The function returns the textual summary and the filename of the generated histogram image.

2. calculate_spendings(queryResult):
   This function takes a list of user spending history (queryResult) as input and calculates the total spending for each month. It processes each record, extracts the month from the date, and accumulates the expenses in a dictionary called Dict, where each key represents a month (e.g., 'Jan', 'Feb'). The function returns this dictionary containing the total spending for each month.

3. calculate_spendings_acs(queryResult):
   This function was defined but not used in the code. It appears to be intended for sorting spending data in ascending order but is not called in the code.

4. calculate_spendings_desc(queryResult):
   This function was defined but not used in the code. It seems to be intended for sorting spending data in descending order but is not utilized.

# How to run this feature?
After you've added sufficient input data, use the /summary command and you can see the output in a spending_history_beautified.pdf . 
