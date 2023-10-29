# Notes based on this video - https://www.youtube.com/watch?v=t8pPdKYpowI
#---------------------------------------------------

#print('HEllo World!')

#---------------------------------------------------
# String concatination

#print('20 days are ' + str(50) + ' minutes')

#---------------------------------------------------
# 'f' -> 'format' for string concatination

#print(f'20 days are {50} minutes')
#print(f'20 days are {20 * 24 * 60} minutes')

#---------------------------------------------------
# Variables -> python is dynamicalyl typed

# to_seconds = 20 * 24 * 60
# name_of_unit = 'seconds'
# print(f'20 days are {to_seconds} {name_of_unit}')

#---------------------------------------------------
# Functions

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units():
#     print(f'20 days are {20 * calculation_to_units} {name_of_unit}')

# days_to_units()

#---------------------------------------------------
# Function Parameters
# Variable Scopes -> global if defined outside of functions, local if defined inside of function

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days, customer_message):
#     print(f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}')
#     print(customer_message)

# days_to_units(20, 'Hello Python')

#---------------------------------------------------
# User Input

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
    
#     return (f'{number_of_days} days are {int(number_of_days) * calculation_to_units} {name_of_unit}')

# user_input = input('Hey user, enter a number of days and I will conver it to hours!\n')
# my_var = days_to_units(user_input)
# print(my_var)

#---------------------------------------------------
# Conditinals (if / else) & Boolean Data Types, Netsted If / else

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
#     if number_of_days > 0:
#         return (f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}')
#     elif number_of_days == 0:
#         return 'You entered ZERO! No go!'
#     else:
#         return 'You entered a negative value, so no conversion fo you!'   

# def validate_and_execute():  
#     if user_input.isdigit():
#         calculated_value = days_to_units(int(user_input))
#         print(calculated_value)
#     else:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = input('Hey user, enter a number of days and I will conver it to hours!\n')

# validate_and_execute()

#---------------------------------------------------
# Netsted If / else

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
#     return (f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}') 

# def validate_and_execute():  
#     if user_input.isdigit():
#         user_input_number = int(user_input)   
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print('You entered ZERO! No go!')
#     else:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = input('Hey user, enter a number of days and I will conver it to hours!\n')

# validate_and_execute()

#---------------------------------------------------
# Try/Except(Catch)

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
#     return (f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}') 

# def validate_and_execute():  
#     try:

#         user_input_number = int(user_input)   
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print('You entered ZERO! No go!')
#         else:
#             print('You entered a negative number! No go!')
#     except ValueError:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = input('Hey user, enter a number of days and I will conver it to hours!\n')

# validate_and_execute()

#---------------------------------------------------
# While Loops

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
#     return (f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}') 

# def validate_and_execute():  
#     try:

#         user_input_number = int(user_input)   
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print('You entered ZERO! No go!')
#         else:
#             print('You entered a negative number! No go!')
#     except ValueError:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = ''
# while user_input != 'exit':
#     user_input = input('Hey user, enter a number of days and I will conver it to hours!\n')
#     validate_and_execute()

#---------------------------------------------------
# List and For Loops

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days):
#     return (f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}') 

# def validate_and_execute():  
#     try:

#         user_input_number = int(number_of_days_element)   
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print('You entered ZERO! No go!')
#         else:
#             print('You entered a negative number! No go!')
#     except ValueError:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = ''
# while user_input != 'exit':
#     user_input = input('Hey user, enter a number of days as a comma seperated list and I will conver it to hours!\n')
#     for number_of_days_element in user_input.split(', '):
#         validate_and_execute()

#---------------------------------------------------
# List Operations []

# months = ['January', 'Febraury', 'March']
# print(months[0])
# months.append('April')
# print(months)

#---------------------------------------------------
# Comments

# Single Comment line

""" Multi Line Comments
"""

#---------------------------------------------------
# Set {} Data type -> does not allow duplicate values

# months = ['January', 'Febraury', 'March', 'March']
# print(months)
# print(type(months))
# months_set = set(months)
# print(months_set)
# print(type(months_set))

# for element in months_set:
#     print(element)

# months_set.add('April')
# print(months_set)
# months_set.remove('January')
# print(months_set)

#---------------------------------------------------
# Dictionary Datatype - Key Value Pairs {'days': 20, 'unit': 'hours'}

# calculation_to_units = 24
# name_of_unit = 'hours'

# def days_to_units(number_of_days, conversion_unit):
#     if conversion_unit == 'hours':
#         return (f'{number_of_days} days are {number_of_days * 24} {conversion_unit}') 
#     elif conversion_unit == 'minutes':
#         return (f'{number_of_days} days are {number_of_days * 24 *60} {conversion_unit}')
#     else:
#         return 'Unsupported Unit!'

# def validate_and_execute():  
#     try:

#         user_input_number = int(days_and_unit_dictionary['days'])   
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number, days_and_unit_dictionary['unit'])
#             print(calculated_value)
#         elif user_input_number == 0:
#             print('You entered ZERO! No go!')
#         else:
#             print('You entered a negative number! No go!')
#     except ValueError:
#         print('Your input is not a number. Don\'t ruin my program!')

# user_input = ''

# while user_input != 'exit':
#     user_input = input('Hey user, enter a number of days and conversion unit!\n')
#     days_and_unit = user_input.split(':')
#     days_and_unit_dictionary = {'days': days_and_unit[0], 'unit': days_and_unit[1]}
#     validate_and_execute()

#---------------------------------------------------
# Modules/Import, Build In Modules
# import helper - imports all functions
# from helper import validate_and_execute - imports only required function
# from helper import * vs. import helper -> how you reference modules
# import helper as hoot -> you cna rename the module

# from helper import validate_and_execute, user_input_message

# user_input = ''

# while user_input != 'exit':
#     user_input = input(user_input_message)
#     days_and_unit = user_input.split(':')
#     days_and_unit_dictionary = {'days': days_and_unit[0], 'unit': days_and_unit[1]}
#     validate_and_execute(days_and_unit_dictionary)

#---------------------------------------------------
# Build In Modules

# import os
# import logging

# print(os.name)

# logger = logging.getLogger('MAIN')
# logger.error('Error happend in the app')

#---------------------------------------------------
# Module vs Package vs Library
# Module is 1 file, package is a collection of modules, Library is a collection of packages
# Import packages from pypi

# pip install packagename
# pip uninstall packagename