# About MyDollarBot's /summary Feature
The summary.py file defines the main function that creates a comprehensive PDF report summarizing a user's financial data. The code imports functions from various other files, such as history_summary, display_summary, estimate_summary, and display_Asc, to gather data and generate different sections in the PDF report. These sections include a history summary, a daily and monthly spending summary, and ascending and descending order of spending summaries. The code sets up a custom PDF document class using FPDF to organize and format the report.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/summary.py)

## Code Description
## Functions
1. run(message, bot):
   This main function initiates the creation of the PDF report. It aggregates data by calling various functions from other files to populate different sections of the report. The sections include a history summary (from history_summary), daily and monthly spending summaries (from display_summary and estimate_summary), and ascending and descending order of spending summaries (from display_Asc). The code compiles all the sections into a single PDF document and sends it to the user via the Telegram bot.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /summary into the telegram bot.
