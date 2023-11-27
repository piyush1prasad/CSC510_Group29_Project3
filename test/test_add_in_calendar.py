import pyautogui
import time

# Function to switch to Telegram Desktop
def switch_to_telegram():
    pyautogui.hotkey('ctrl', 'tab')
    pyautogui.click(721, 896)
    time.sleep(1)

# Function to type a message in Telegram
def type_message(message):
    pyautogui.typewrite(message)
    pyautogui.press('enter')

# Function to select a date on the calendar
def select_date(date):
    # Example logic to calculate the position based on date
    # This is a placeholder and needs to be adjusted based on the actual UI
    x_base, y_base = 100, 200  # Base position for the calendar
    x_offset, y_offset = 50, 50  # Offset for each day and row
    day, month, year = map(int, date.split('.'))
    x_pos = x_base + (day * x_offset)
    y_pos = y_base + (month * y_offset)  # Simplified assumption
    pyautogui.click(x_pos, y_pos)

# Function to test add_to_calendar
def test_add_in_calendar(test_cases):
    for test in test_cases:
        
        type_message('/add_in_calendar')
        time.sleep(2)  # Wait for calendar to appear
        select_date(test['date'])
        type_message(test['category'])
        type_message(str(test['amount']))

# Function to test change_currency
def test_change_currency():
    #switch_to_telegram()
    type_message('/change_currency')
    type_message('INR')

# Test cases for add_in_calendar
test_cases = [
    {'date': '01.12.2023', 'category': 'Transport', 'amount': 100},
    {'date': '05.12.2023', 'category': 'Food', 'amount': 200},
    # Add more test cases as needed
]

# Run the tests
switch_to_telegram()
test_add_in_calendar(test_cases)
test_change_currency()
