# About MyDollarBot's /currency_type Feature  
This feature enables the user to add a new expense by changing the currency type.



# Location of Code for this Feature
The code that implements this feature can be found [here] [https://github.com/piyush1prasad/CSC510_Group29_Project3/blob/main/code/add_in_calendar.py](https://github.com/piyush1prasad/CSC510_Group29_Project3/blob/main/code/currency_type.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the add feature. It pop ups a menu on the bot asking the user to choose their expense category, after which control is given to post_category_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_category_selection(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add.py file. It requests the user to enter the amount they have spent on the expense category chosen and then passes control to post_amount_input(message, bot): for further processing only if the user doesnot Cancel the operation.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /currency_type into the telegram bot.
