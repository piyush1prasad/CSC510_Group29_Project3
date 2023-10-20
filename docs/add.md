# About MyDollarBot's /add Feature
This feature enables the user to add a new expense to their expense tracker.
Currently we have the following expense categories set by default and Cancel option:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

The user can choose a category and add the amount they have spent to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/add.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the add feature. It pop ups a menu on the bot asking the user to choose their expense category, after which control is given to post_category_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_category_selection(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add.py file. It requests the user to enter the amount they have spent on the expense category chosen and then passes control to post_amount_input(message, bot): for further processing only if the user doesnot Cancel the operation.

3. post_amount_input(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_category_selection(message, bot): function in the add.py file. If the operation is not cancelled it takes the amount entered by the user, validates it with helper.validate() and then calls add_user_record to store it .

4. add_user_record(chat_id, record_to_be_added):
 Takes 2 arguments - **chat_id** or the chat_id of the user's chat, and **record_to_be_added** which is the expense record to be added to the store. It then stores this expense record in the store.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

https://github.com/21Tulasi/MyDollarBot-newPhase/assets/68286340/c39d0ab0-8801-41fa-bdb1-959e86635cfc
