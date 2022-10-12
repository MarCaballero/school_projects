#What program does? Determines whether a password meets the following requirements for a secure password:
    #length of password required has to be min. 6 characters and max. 12 characters
    #It must NOT include any spaces
    #It must contain at least one digit
    #It must contain at least one aphabetic character
#Major Design Steps:
    #1. We checked the length of password was within the requirements
        #password = MarMel1234Caballero --> exceeds number of characters
        #password = Mar --> It is short on number of characters

    #2. We checked password didn't contain any spaces, else we asked for password again
        #password = Mar Mel 123 --> contain spaces, then we ask again
        #password = MarMel123 --> correct password because it does not contain any spaces

    #3. We checked password contained at least one alphabetic character
        #password = 1234568 --> doesn't contain any alphabetic characters, then we ask again
        #password = MarMel123 --> contains alphabetic characters, therefore password is correct

    #4. We checked password contained at least one numeric character
        #password = MarMel --> doesn't contain any numeric characters, then we ask again
        #password = MarMel123 -->contains numeric characters, therefore password is correct

    #5. If password passed all the requirements for a safe password, we display to the user the newly created password
        #password = MarMel123 --> meets all the required items for a secure password

    #6. We exit gratefully

#Developer Name: Maria Caballero
#CMIS-102 (6385)
#Date: 09/23/2022



#main() function executes the whole program by properly using each function 
def main():
    #prints out the specific requirements for a secure password
    print("Requirements to create a password.")
    print("\t1) It needs to be min 6 characters, maximum 12")
    print("\t2) It requires to have at least one number and/or alphabetic character")
    print("\t3) No spaces are allowed")
    #newly_created_password varible stores the correct secure password after using all functions
    newly_created_password = ask_password()
    print('Your new password is ', newly_created_password)
    #We exit gratefully
    print("Thank you for participating, see you next time!")



#The ask_password() function asks user to create a password and starts using the results of each function to check if is a secure password
def ask_password():
    #Asks user to create a password
    password = input("Please, create your password: ")
    #Checks for length to be correct if not asks again to create a password
    checked_password = check_length(password)
    #If length is correct, we create an if statement to check the password doesn't include any spaces
    if(has_spaces(checked_password) == True):
        print("You are not allowed to have spaces in the password, please try again.")
        #if it does include spaces then we print the above statements and ask again until no spaces are found
        return ask_password()
    #If the newly created password doesn't include any spaces, we check it has at least one alphabetic character
    if(has_alpha(checked_password) == False):
        print("You need at least one alphabetic character. Try again.")
        #if it doesn't include at least one alphabetic character then we print the above statement and ask again until password contains one alphabetic character
        return ask_password()
    #if password contains alphabetic characters, we then check for numbers to be included
    if(has_numbers(checked_password) == False):
        print("You need at least one numeric character. Try again.")
        #if the password doesn't include any numbers then we print the above statement and ask again until password contains at least one numeric character
        return ask_password()
    #finally if the password meets all the requirements and it's correct, we return the password
    else:
        return checked_password

#check_length(password) checks the length of password is within 6 and 12 characters 
def check_length(password):
    #count is a variable were we will store the count of each letter contained in passwordto be able to check for length requirements
    count = 0
    for letter in password:
        count = count + 1
    if count < 6:
        print("password has less characters than required, try again.")
        return ask_password()
    elif count > 12:
        print("password has too many characters than required, try again.")
        return ask_password()
    else:
        return password

#has_alpha(password) is a function that will check the password contains at least one alphabetic character
def has_alpha(password):
    #we set contain_alpha to False 
    contains_alpha = False
    #for each character in password we check there is at least one alphabetic character, if so, then we set contains_alpha to True
    for letter in password:
        if letter.isalpha() == True:
            contains_alpha = True
    #we return contains_alpha to be able to check later on ask_password() function
    return contains_alpha

#has_numbers(password) is a function that will check the password contains at least one numeric character
def has_numbers(password):
    #we set contain_numbers to False 
    contains_numbers = False
    #for each character in password we check there is at least one numeric character, if so, then we set contains_numbers to True
    for letter in password:
        if letter.isdigit() == True:
            contains_numbers = True
    #we return contains_numbers to be able to check later on ask_password() function
    return contains_numbers

#has_spaces(password) is a function that will check the password does not contain any spaces
def has_spaces(password):
    #we set contains_spaces to False 
    contains_spaces = False
    #for each character in password we check there is no spaces, if so, then we set contain_spaces to True
    for letter in password:
        if letter.isspace() == True:
            contains_spaces = True
    #we return contains_spaces to be able to check later on ask_password() function
    return contains_spaces
    
        
main()
