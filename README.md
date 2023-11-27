# 💰 TrackMyDollar V3.0 - Budget On The Go(BOTGo) 💰


<hr>
<p align="center">
<a><img  height=420 width=550 
  src="https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/docs/trackmydollar.png" alt="Tracking expenses made easy!"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/21Tulasi/MyDollarBot-newPhase)](https://github.com/21Tulasi/MyDollarBot-newPhase/graphs/contributors)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10023243.svg)]((https://zenodo.org/doi/10.5281/zenodo.10023242))
[![Build Status](https://app.travis-ci.com/sak007/MyDollarBot-BOTGo.svg?branch=main)](https://app.travis-ci.com/github/sak007/MyDollarBot-BOTGo)
[![CI](https://github.com/21Tulasi/MyDollarBot-newPhase/actions/workflows/main.yml/badge.svg)](https://github.com/21Tulasi/MyDollarBot-newPhase/actions/workflows/main.yml)
[![Lint Python](https://github.com/21Tulasi/MyDollarBot-newPhase/actions/workflows/black.yml/badge.svg)](https://github.com/21Tulasi/MyDollarBot-newPhase/actions/workflows/black.yml)
[![codecov](https://codecov.io/gh/sak007/MyDollarBot-BOTGo/branch/main/graph/badge.svg?token=5AYMR8MNMP)](https://codecov.io/gh/sak007/MyDollarBot-BOTGo)
[![GitHub issues](https://img.shields.io/github/issues/prithvish-doshi-17/MyDollarBot-BOTGo)](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues?q=is%3Aopen+is%3Aissue)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/prithvish-doshi-17/MyDollarBot-BOTGo)](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues?q=is%3Aissue+is%3Aclosed)

![Fork](https://img.shields.io/github/forks/deekay2310/MyDollarBot?style=social)
<hr>

## About TrackMyDollar

TrackMyDollar is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle 
With simple commands, this bot allows you to:
- Add/Update/View/Delete Income
- Add/Record a new spending
- Add/Update/View/Delete Budget
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Summary report of all expenses done till date
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- Add expense to any date on the calendar
- Add expense in any currency 


## What's new? (From Phase 3 to Phase 4)

-Add to Calendar:
This functionality lets uusers add an expense to any date from the Calendar.
In the older version of this software, the expense would get added by default to the current date.

-Currency Type:
This feature lets user record their expenses in a variety of currencies. 
In the older version, the expense could only be recorded in USD.

## What more can be done?
Please refer to the issue list available [here](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues) to see what more can be done to make MyDollarBot better. Please refer to the MyDollarBot project present [here](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/projects) to have a look at the tasks to be done, tasks currently in progress and tasks already done.


## Demo

[![Watch the video](https://img.youtube.com/vi/O44Spomhkbs/maxresdefault.jpg)](https://youtu.be/O44Spomhkbs)


## Installation guide

The below instructions can be followed in order to set-up this bot at your end in a span of few minutes! Let's get started:

1. Clone this repository to your local system.

2. Start a terminal session in the directory where the project has been cloned. Run the following command to install the required dependencies:
```
  python3 -m pip install fpdf
  pip install -r requirements.txt
```

3. In Telegram, search for "BotFather". Click on "Start", and enter the following command:
```
  /newbot
```
Follow the instructions on screen and choose a name for your bot. After this, select a username for your bot that ends with "bot".

4. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use.

5. In the directory where this repo has been cloned, please run the below command to execute a bash script to run the Telegram Bot:
```
   ./run.sh
```
(OR)
```
   bash run.sh
```
Please note that it will ask you to paste the API token you received from Telegram in step 4.
A successful run will generate a message on your terminal that says "TeleBot: Started polling." 

6. In the Telegram app, search for your newly created bot by entering the username and open the same. Now, on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!


## Walktrough 
Add in Calendar: 
Steps: 1. Enter /menu
       2. Enter /add_in_calendar OR Press on /add_in_calendar in the menu
       3. Click on the date of your choice
       4.Select from the Category of expenses
       5.Enter the ammount and click enter! You will get a confirmation message

Changing Currency Type:
Steps: 1. Enter /menu 
       2. Select /curr_type from the menu or type /curr_type
       3. Select from the variety of options available
       4. You will get a confirmation message.

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:
```
python run -m pytest test/
```

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

## Troubleshoot:

1. While running the project an error may arise stating fpdf  Module not found eventhough it is installed in such case uninstall fpdf using pip uninstall fpdf upgrade pip and install using the provided command pip.
2. While running the test cases if an error arrises then run pytest command to run the testcases.
   

## Notes:
You can download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/


<hr>
<p>Title:'Track My Dollar'</p>
<p>Version: '4.1'</p>
<p>Description: 'An easy to use Telegram Bot to track everyday expenses'</p>
<p>Authors(Iteration 5):'Piyush, Raaj, Ameaza'</p>
<p>Authors(Iteration 4):'Tulasi, Siddartha, Yogitha, Deepika'</p>
<p>Authors(Iteration 3):'Vraj, Alex, Leo, Prithvish, Seeya'</p>
<p>Authors(Iteration 2):'Athithya, Subramanian, Ashok, Zunaid, Rithik'</p>
<p>Authors(Iteration 1):'Dev, Prakruthi, Radhika, Rohan, Sunidhi'</p>
