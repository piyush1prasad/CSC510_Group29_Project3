# About MyDollarBot's /add in Calendar Feature 
This feature enables the user to add a new expense any date in the tracker.
Currently we have the /add option that adds the expense to only the current date.


# Location of Code for this Feature
The code that implements this feature can be found [here] https://github.com/piyush1prasad/CSC510_Group29_Project3/blob/main/code/add_in_calendar.py

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

5. def display_categories(message, bot):
   Takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the aadd_in_calendar.py file. It requests the user to select the date from the calendar and then passes control to post_amount_input(message, bot): for further processing only if the user doesnot Cancel the operation.
# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add_in_calendar into the telegram bot.

