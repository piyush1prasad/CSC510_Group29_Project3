# About MyDollarBot's /category Feature
This feature enables the user to manage their categories.
Currently we have the following expense categories set by default and Cancel option:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

The user can choose to add/delete/show categories, and after that, add the cost with custom category to the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/category.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the category feature. It pop ups a menu on the bot asking the user to choose their operation, after which operation is given to post_operation_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_operation_selection(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the category.py file. It requests the user to choose an operation from Add/Delete/Show categories and then passes control to category_add(message, bot), category_delete(message, bot), category_view(message, bot) for further processing depends on user's choose if the user doesnot Cancel the operation.

3. category_add(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_operation_selection(message, bot): function in the category.py file. It takes the new category name entered by the user, and then write it in the file categories.txt.

4. category_delete(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_operation_selection(message, bot): function in the category.py file. It takes the category name entered by the user, read the file categories.txt and check whether the inputed category is in the file. Write  the categories back to the file categories.txt.
 
5. category_view(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_operation_selection(message, bot): function in the category.py file. It read the file categories.txt and output the text in chat room.
 
# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /category into the telegram bot.


https://github.com/21Tulasi/MyDollarBot-newPhase/assets/68286340/0a5f6b0a-7bc1-4fd4-889f-89903e89e239


