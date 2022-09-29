def main():
    #Identify variables
    Fname = input("Please enter your First name: ")
    Lname = input("Please enter your Last name: ")
    name = (Fname + Lname)

    #Identify their initials
    print("Your initials are:",Fname[0],"and",Lname[0])

    #Calculate the total length

    length1 = len(Fname)
    print("Your first name has ",length1, "characters")
    length2 = len(Lname)
    print("Your last name has ",length2, "characters")
    total_length = len(Fname) + len(Lname)
    print("Your name has a total of ",total_length,"characters!\n")

    #Create a username
    username = input("Now, create a username: ")
    upper_username = username.upper()
    upper_Fname = Fname[0].upper()
    upper_Lname = Lname[0].upper()
    foundFirstInitials = False
    foundLastInitials = False
    

    for char in upper_username:
        if char == upper_Fname:
            foundFirstInitials = True
       
        elif char == upper_Lname:
            foundLastInitials = True
            
        elif char == upper_Fname and char == upper_Lname:
            foundFirstInitials = True
            foundLastInitials = True


    if foundFirstInitials == True and foundLastInitials == True:
        print('Both, first and last name initials were found in username')
    elif foundFirstInitials == True:
        print('Your first name initials were found in username')
    elif foundLastInitials == True:
        print('Your last name initials were found in username')
    else:
        print('Initials were not found in username')      
        

    print('Thank you for participating!')
    

    
main()    
