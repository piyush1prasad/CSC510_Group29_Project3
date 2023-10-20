# About MyDollarBot's graphing_for_month.py file
This code, primarily responsible for data visualization for monthly expenditure and is designed to generate graphical 
representations of user spending data. It uses the Matplotlib library to create bar charts 
and pie charts, allowing users to visualize their expenses. The code includes three main 
functions: visualize, vis, and viz, each producing different types of charts. These charts 
illustrate expense categories and amounts, with the option to include budget lines for comparison. 
The resulting charts are saved as image files.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/graphing_for_month.py)

# Code Description
## Functions
1. visualize(total_text, budgetData):
   This function creates a bar chart to visualize user spending data. It processes the spending
   data to obtain categories and amounts, then plots the categories on the x-axis and corresponding
   expenses on the y-axis. Budget lines can also be included for reference. The resulting chart is
   saved as 'expenditure_month.png'. This function facilitates a comprehensive view of expenses
   against budgets.

2. vis(total_text): This function generates a pie chart to visualize user spending data. It extracts
   categories and amounts from the spending data, then plots them in a pie chart format,
   showing the proportion of each category's expenditure. The resulting pie chart is saved as
   'pie_month.png'. This chart offers a quick, visually appealing overview of spending distribution.

3. viz(total_text): Similar to visualize, this function creates a bar chart to visualize user
   spending data. It processes the data and plots categories on the x-axis and expenses on the
   y-axis. Unlike visualize, it applies custom colors to the bars for a different visual
   representation. The resulting chart is saved as 'expend_month.png'. This function provides
   an alternative way to view expenses, emphasizing the use of custom colors for differentiation.


# How to run this feature?
After you've added sufficient input data, use the /summary command and you can see the output in a spending_history_beautified.pdf . 
