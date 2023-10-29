user_input_message = 'Hey user, enter a number of days and conversion unit!\n'

def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return (f'{number_of_days} days are {number_of_days * 24} {conversion_unit}') 
    elif conversion_unit == 'minutes':
        return (f'{number_of_days} days are {number_of_days * 24 *60} {conversion_unit}')
    else:
        return 'Unsupported Unit!'

def validate_and_execute(days_and_unit_dictionary):  
    try:

        user_input_number = int(days_and_unit_dictionary['days'])   
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary['unit'])
            print(calculated_value)
        elif user_input_number == 0:
            print('You entered ZERO! No go!')
        else:
            print('You entered a negative number! No go!')
    except ValueError:
        print('Your input is not a number. Don\'t ruin my program!')