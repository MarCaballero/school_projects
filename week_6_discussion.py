#What program does?
    #1) Asks user for first name to take out initial of first name
    #2) Ask user for last name to take out initial of last name
    #3) asks user to create a username
    #4)checks username created doesn't contain spaces
    #5)checks username created doesn't contain numbers
    #6) counts the number of times the username letters contain the first and last name initials
    #7)Displays to the user
#Test Cases:
    #1) first name: Maria
        #last name: Caballero
        #username: mar123
        #second try username: ladyfresh

    #2) first name: Maria
        #last name: Caballero
        #username: mar caba
        #second try username: jonrat

    #3) first name: Maria
        #last name: Caballero
        #username: marmel

#Developer name: Maria Caballero
#CMIS-102 (6385)
#Date: 09/21/2022

from calendar import c


def main():

    firstName = input('Please, enter your first name: ')
    lastName = input('Please enter your last name: ')

    user_name = ask_user()
    initials_found = 0

    for letter in user_name:
        if letter.upper() == firstName[0].upper() or letter == lastName[0].upper():
           initials_found = initials_found + 1
        
    print('Your name initials were found ', initials_found, ' times')


def ask_user():
    user_name = input('Create a username (no numbers or spaces allowed): ')
    new_username = user_name.upper()
    if(username_has_spaces(new_username)):
        print("No spaces allowed")
        return ask_user()
    elif(username_has_numbers(new_username)):
        print("No numbers allowed.")
        return ask_user()
    else:
        return user_name
    

#We check it doesnt have any spaces
def username_has_spaces(userName):
    has_spaces = False
    for letter in userName:
        if letter.isspace()== True:
            has_spaces = True
    
    return has_spaces

#We check it doesnt have any numbers
def username_has_numbers(userName):
    has_numbers = False
    for letter in userName:
        if letter.isdigit() == True:
            has_numbers = True
    
    return has_numbers



            

main()
