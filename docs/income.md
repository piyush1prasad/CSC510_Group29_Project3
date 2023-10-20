# About MyDollarBot's /income Feature
This feature enables the user to add, remove, edit or display a income in their expense tracker.

The user can choose a category and add the amount for the income to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/income.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the budget feature. It pop ups a menu on the bot asking the user to choose to add, remove or display a income, or Cancel after which control is given to post_operation_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_operation_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the budget.py file. Depending on the action chosen by the user, it passes on control to the corresponding functions which are all located in different files if the action selected is not Cancel.

3. post_overall_amount_input(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_operation_selection(message, bot): function in the income.py file. This function takes over from the update_overall_income, and asks the user to enter the new/updated income amount. As long as the user doesnot Cancel the action and this amount is not zero(in which case it throws an exception), it continues processing. It reads the current user data through helper module's read_json function adds the new income information onto it, writing back with the helper module's write_json function.

4.display_income(message, bot):
It takes 2 arguments for processing - message which is the message from the user, and bot which is the telegram bot object from the run(message, bot): in the same file. income for the user based on their chat ID using the helper module.It then processes it into a string format suitable for display, and returns the same through the bot to the Telegram UI.

5.delete_income(message, bot):
It takes 2 arguments for processing - message which is the message from the user, and bot which is the telegram bot object from the run(message, bot): in the same file. It gets the user's chat ID from the message object, and reads all user data through the read_json method from the helper module. It then proceeds to empty the budget data for the particular user based on the user ID provided from the UI. It returns a simple message indicating that this operation has been done to the UI.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.


https://github.com/21Tulasi/MyDollarBot-newPhase/assets/68286340/ee26fdc8-2e80-4bdb-a106-23d2e37bb74b



