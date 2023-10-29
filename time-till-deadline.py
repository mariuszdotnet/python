from datetime import datetime

user_input = input('Enter your goal with a dealine seperated by a colan:\n')
input_list = user_input.split(':')
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.now()
# Calculate how many days from no till deadline
time_till = deadline_date-today_date


print(f'Dear user! Time remaining for your goal: {goal} is {time_till.days} days')