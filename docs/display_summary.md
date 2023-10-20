# About MyDollarBot's display_summary.py file
The display_summary.py is responsible for displaying total spending and generating corresponding plots
for both daily and monthly expenses. It interfaces with the helper, graphing_for_day, and 
graphing_for_month modules to retrieve data and create visual representations of user spending. 
The functions display_total, plot_total, calculate_spendings, and display_budget_by_text are central 
to this code, ensuring that users receive information on their spending habits and budgets.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/display_summary.py)

# Code Description
## Functions

1. display_total(message, bot):
   This main function initiates the process of displaying total spendings and generating plots.
   It reads user data from JSON, retrieves the user's spending history, and checks if any records exist.
   If available, it calls the display_total function to calculate spendings, display budget data,
   and create plots. It stores data and image filenames for future reference.

2. display_total(message, bot):
   This function calculates total spendings for both the current day and month based on the user's history and budget data.
   It also determines budget data and retrieves the user's history. The results are used to create
   spending text and are later used for plotting.

4. plot_total(message, bot):
   This function generates and sends plots for total spendings. It creates various visual
   representations of daily and monthly expenses, including bar charts and pie charts, using the
   graphing_for_day and graphing_for_month modules. The resulting images are stored for display to
   the user.

5. calculate_spendings(queryResult):
   This function calculates the total spendings from the provided query result, which is a list of
   user spending history data. It processes the data, categorizes expenses by type, and calculates
   the total amount spent in each category.

6. calculate_spendings_acs(queryResult):
   This function was defined but not used in the code. It appears to be intended for sorting
   spending data in ascending order but is not called in the code.

7. calculate_spendings_desc(queryResult):
   This function was defined but not used in the code. It seems to be intended for sorting
   spending data in descending order but is not utilized.

8. display_budget_by_text(history, budget_data):
   This function generates a text-based display of the user's budget information. It calculates the
   remaining budget for the user, considering both overall and category-specific budgets. The
   resulting budget display is returned as a formatted text string.

# How to run this feature?
After you've added sufficient input data, use the /summary command and you can see the output in a PDF file. 
