# About MyDollarBot's /display_Asc Feature
This feature enables the users to view their spendings in a sorted order based on the spend amount.
Both Ascending and Descending Orders of user's spendings are displayed in the 
spending_history_beautified.pdf

# Location of Code for this Feature
The code that implements this feature can be found [here]https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/display_Asc.py

# Code Description
## Functions

1. run(message, bot):
   This is the main function used to implement the display_Asc feature. It Reads the user data from
   JSON and also stores the chat_id. Using getUserHistory the user spending is retrieved and stored in history.
   An if condition is implemented to chech whether the history is None or not. If the history is None bot sends a
   message to user saying that "Sorry, there are no records of the spending!" else it calls display_total(message, bot) function and returns a list called data.
   It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. display_total(message, bot)
   Calculates and displays total spending in ascending and descending order. It formats the results and appends them to a data list.
   Calls calculate_spendings_acs(query_acs) to calculate total spendings in ascending order.
   Calls calculate_spendings_desc(query_desc) to calculate total spendings in descending order.

3. calculate_spendings_acs(query_Result)
   Sort spending data in ascending order based on the amount and returns the sorted data.

4. calculate_spendings_desc(query_Result)
   Sorts spending data in descending order based on the amount and returns the sorted data.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /summary into the telegram bot.
