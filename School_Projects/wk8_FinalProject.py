#What does the program do? 
    #1)My program displays the service we offer and prices to the user
    #2)It asks the user to enter the preferable service
        #a)House Cleaning
        #b)Yard Service
        #c)House Cleaning and Yard Service (both)
    #3)It displays the discount we offer to the user, depending the age
    #4)Asks user to enter age
    #5)It displays either the user's age is valid or not for the offered discount
    #6)It then asks for the type of service required
        #If Yard:
            #Type1 = Mowing
                #Asks for length and width
            #Type2 = Edging
                #Asks for length
            #Type3 = Shrub pruning
                #Asks for the No. of shrubs to prune
        #If House Cleaning: 
            #House Size1 = Small (1 to 3 rooms)
                #Dusting OR Floors OR both
            #House Size2 = Medium (4 to 6 rooms)
                #Dusting OR Floors OR both
            #House Size3 = Large (7 to 9 rooms)
                #Dusting OR Floors OR both
        #If both:
            #Yard:
                #Type1 = Mowing
                    #Asks for length and width
                #Type2 = Edging
                    #Asks for length
                #Type3 = Shrub pruning
                    #Asks for the No. of shrubs to prune
            #House Cleaning:
                #House Size1 = Small (1 to 3 rooms)
                #Dusting OR Floors OR both
            #House Size2 = Medium (4 to 6 rooms)
                #Dusting OR Floors OR both
            #House Size3 = Large (7 to 9 rooms)
                #Dusting OR Floors OR both
    
    #7)It then calculates and displays the total cost of the given service(s)
        #If Senior the discount is applied
        #If not a Senior then discount is not applied 
    
#Major Design Steps:
    #Yard:
        #1.Yard services offered:
            #a.Mowing
            #b.Edging
            #c.Shrub prune
        #2.Price of each type:
            #a.$25 per square footage
                #Length * Width * 25
            #b.$30 per linear footage
                #Length * 30
            #c. $50 per number of shrub to prune(n)
                #n * 50

    #House Cleaning:
        #1.Cleaning types offered:
            #a.Dusting
            #b.Floors
        #2.Price of each type:
            #a. $75 dollars
            #b. $50 dollars
        #3.Cost based on house size:
            #Small size = 1-3 rooms
            #Medium size = 4-6 rooms
            #Large size = 7-9 rooms
        #4.Calculations depending on number of rooms and type of cleaning chosen
            #1a. roomsNum * type1
            #2b. roomsNum * type2
            #3ab. (roomsNum * type1) + (roomsNum * type2)
    #Discount:
        #1.Age = 60+
        #2.Yard Discount = 25%
        #3.House Cleaning Discount = 15%
#Developer name: Maria Caballero
#CMIS-102 (6385)
#Date: 09/02/2022


#print_sizes(): function without arguments prints the sizes of the house
def print_sizes():
    print("\tSmall = 1 to 3 rooms.")
    print("\tMedium = 4 to 6 rooms.")
    print("\tLarge = 7 to 9 rooms.")

#print_yardServies(): function without arguments prints the yard services and price of each
def print_yardServices():
    print("\tMowing = $25 per square foot")
    print("\tEdging = $30 per linear footage")
    print("\tShrub Pruning = $50 per shrub")
    
#size_comparison(x): function with one argument compares the sizes and asks for the number of rooms
def size_comparison(size):
    SM = "SMALL"
    MED = "MEDIUM"
    LG = "LARGE"
    #comparison for small
    if size.upper() == SM:
        roomsNum = int(input("How many rooms?(please, enter a number) "))
    #comparison for medium
    elif size.upper() == MED:
        roomsNum = int(input("How many rooms?(please, enter a number) "))
    #comparison for large
    elif size.upper() == LG:
        roomsNum = int(input("How many rooms?(please, enter a number) "))
        
    #returns the number of rooms to clean
    return roomsNum

#yard_service_cost(x, y): function with two arguments calculates the total cost for the given service, according to age and returns total cost
def yard_service_cost(service, age):
    #Replacing (if any) spaces with no spaces to be able to compare
    yardService = service.replace(" ", "").upper()
    #Initializing variables for costs and discount if applicable
    mowing_cost = 25
    edging_cost = 30
    shrub_cost = 50
    senior_discount = .25
    #Initializing the variable where we will store the total cost
    total_cost = 0

    #If the yard service required is 'mowing' and age is between senior range then calculate total cost with discount and return
    if yardService == "MOWING":
        if age >= 60 and age < 106:
            length = eval(input("Please enter the length in feet: "))
            width = eval(input("Please enter the width in feet: "))
            total_cost = length * width * mowing_cost
            total_discount_cost = length * width * mowing_cost * senior_discount
            total_cost = total_cost - total_discount_cost
            return total_cost
        #Else if the age is not between senior range then calculate total cost without the discount
        else:
            length = eval(input("Please enter the length in feet: "))
            width = eval(input("Please enter the width in feet: "))
            total_cost = length * width * mowing_cost
            return total_cost
    #If the yard service required is 'edging' and age is between senior range then calculate total cost with discount and return
    elif yardService == "EDGING": 
        if age >= 60 and age < 106:
            length = eval(input("Please enter the length in feet: "))
            total_cost = length * edging_cost 
            total_discount_cost = length * edging_cost * senior_discount
            total_cost = total_cost - total_discount_cost
            return total_cost
        #Else if the age is not between senior range then calculate total cost without the discount
        else: 
            length = eval(input("Please enter the length in feet: "))
            total_cost = length * edging_cost
            return total_cost
    #If the yard service required is 'shrub pruning' and age is between senior range then calculate total cost with discount and return
    elif yardService == "SHRUBPRUNING":
        if age >= 60 and age < 106:
            shrub_number = eval(input("Please enter the number of shrubs to prune: "))
            total_cost = shrub_number * shrub_cost
            total_discount_cost = shrub_number * shrub_cost * senior_discount
            total_cost = total_cost - total_discount_cost
            return total_cost
        #Else if the age is not between senior range then calculate total cost without the discount
        else:
            shrub_number = eval(input("Please enter the number of shrubs to prune: "))
            total_cost = shrub_number * shrub_cost
            return total_cost
    #Else if the inputted service is not a service we offer, make user to try again
    else:
        service = input("Please enter the correct service (mowing, edging, shrub pruning): ")
        new_age = age
        return yard_service_cost(service, new_age)

        
#house_cleaning_cost(x, y): function with two arguments compares the type of cleaning needed and returns the calculated cost
def house_cleaning_cost(roomsNum, typeOfCleaning):
    tp1 = "DUSTING"
    type1 = 75
    tp2 = "FLOORS"
    type2 = 50

    #if type of cleaning is dusting then the cost is the number of rooms to clean times the price of the type of cleaning
    if typeOfCleaning.upper() == tp1:
            cost = roomsNum * type1
            #we return cost
            return cost
    #if type of cleaning is floors then the cost is the number of rooms to clean times the price of the type of cleaning       
    elif typeOfCleaning.upper() == tp2:
            cost = roomsNum * type2
            #we return cost
            return cost
    #if type of cleaning is dusting and floors then the cost is the number of rooms to clean times the price of the type of cleaning       
    else:
            cost = (roomsNum * type1)+(roomsNum * type2)
            #we return cost
            return cost

#def check_option_service(x): function with one argument validates either the service entered is correct or not and returns  
def check_option_service(service):
    service1 = service.replace(" ", "").upper()
    if service1 == "YARDSERVICE" or service1 == "YARD":
        return service1
    elif service1 == "HOUSECLEANING" or service1 == "HOUSE":
        return service1
    elif service1 == "YARDSERVICEANDHOUSECLEANING" or service1 == "HOUSECLEANINGANDYARDSERVICE" or service1 == "YARDANDHOUSE" or service1 =="HOUSEANDYARD" or service1 == "BOTH":
        return service1
    else:
        service = input("Please enter the correct service you would like: ")
        return check_option_service(service)

#def check_validAge(x): function with one argument validates if the age applies for senior discount or not and then returns
def check_validAge(age):
    if age >= 60 and age < 106:
        return age
    elif age > 0 and age < 60:
        return age
    else:
        age = int(input("Your age was an invalid number, please try again: "))
        return check_validAge(age)

#main(): is the main function without arguments where our program will be executed and displayed to the user      
def main():
    #Print statements
    print("Houses Cleaning Sizes: ")
    print_sizes()
    print("Types of Cleaning: ")
    print("\tDusting = $75")
    print("\tFloors = $50")
    print()
    print("Yard Services: ")
    print_yardServices()

    #Input
    option_service = input("\nPlease enter the type of service you would like to have today (yard service, house cleaning, or both): ")
    #Applying function
    checked_option = check_option_service(option_service)
    #Print statements
    print("\nNote - If you are a senior (60+) there is a discount of... ")
    print("\tYard service discount = 25% off over the total price.")
    print("\tHouse service discount = 15% off over the total price.\n")
    #Input
    age = int(input("Please, enter your age: "))
    #Call function
    checked_age = check_validAge(age)
    #Initializing senior discount for house cleaning service
    senior_discount_for_house_cleaning = .15

    #if yard service entered:
    if checked_option =="YARDSERVICE" or checked_option == "YARD":
        #If age is valid for senior discount
        if checked_age >= 60 and checked_age < 106:
            #Print statement
            print("Congratulations, you qualify for the senior discount.")
            #Input = yard type of service
            yard_service = input("\nPlease, enter what service for yard - mowing, edging or shrub pruning:\n")
            #Call function
            total_cost_of_service = yard_service_cost(yard_service, checked_age)
            #Print statement = total cost 
            print("\nYour total yard service cost will be = ", total_cost_of_service)
        #If age is Not valid for senior discount
        else:
            #Print statement
            print("Sorry, you do not qualify for senior discount.")
            #Input = yard type of service
            yard_service = input("\nPlease, enter what service for yard - mowing, edging or shrub pruning:\n")
            #Call function
            total_cost_of_service = yard_service_cost(yard_service, checked_age) 
            #Print statement = total cost
            print("\nYour total yard service cost will be = ", total_cost_of_service)
    
    #if House cleaning entered:
    if checked_option == "HOUSECLEANING" or checked_option == "HOUSE":
        #If age is valid for senior discount
        if checked_age >= 60 and checked_age < 106:
            #Print statement
            print("Congratulations, you qualify for the senior discount.")
            #Input = size of house
            size = input("\nPlease enter the size of your house: ")
            #Call function
            size = size_comparison(size)
            #Input = type of cleaning service
            typeOfCleaning = input("Please, enter what type of cleaning - dusting, floors or both:\n")
            #Call function
            total_house_cost = house_cleaning_cost(size, typeOfCleaning)
            #Calculate total cost with senior discount
            house_cost = total_house_cost * senior_discount_for_house_cleaning
            total_house_cost = total_house_cost - house_cost
            #Print statement = total cost
            print("\nYour total house cleaning service cost will be = ", total_house_cost)
        #If age is not valid for senior discount
        else:
            #Print statement
            print("Sorry, you do not qualify for senior discount.")
            #Input = size of house
            size = input("\nPlease enter the size of your house: ")
            #Call function
            size = size_comparison(size)
            #Input = type of cleaning service
            typeOfCleaning = input("Please, enter what type of cleaning - dusting, floors or both:\n")
            #Call function
            total_house_cost = house_cleaning_cost(size, typeOfCleaning)
            #Print statement = total cost
            print("\nYour total house cleaning service cost will be = ", total_house_cost)

    #If both services entered (yard and house cleaning):
    if checked_option == "YARDSERVICEANDHOUSECLEANING" or checked_option == "HOUSECLEANINGANDYARDSERVICE" or checked_option == "YARDANDHOUSE" or checked_option =="HOUSEANDYARD" or checked_option == "BOTH":
        #If age is valid for senior discount
        if checked_age >= 60 and checked_age < 106:
            #Print statement
            print("Congratulations, you qualify for the senior discount.")
            #Input = yard type of service
            yard_service = input("\nPlease, enter what service for yard - mowing, edging or shrub pruning:\n")
            #Call function
            total_cost_of_service = yard_service_cost(yard_service, checked_age)
            #Input = size of house 
            size = input("\nPlease enter the size of your house: ")
            #Call function
            size = size_comparison(size)
            #Input = type of cleaning service
            typeOfCleaning = input("Please, enter what type of cleaning - dusting, floors or both:\n")
            #Call function
            total_house_cost = house_cleaning_cost(size, typeOfCleaning)
            #Calculate total cost with senior discount
            total_discount = total_house_cost * senior_discount_for_house_cleaning
            total_cost_after_discount = total_house_cost - total_discount
            #Print statement = total cost
            print("\nYour total yard and house cleaning service cost will be = ", total_cost_of_service + total_cost_after_discount)
        #if age is not valid for senior discount
        else:
            #Print statement
            print("Sorry, you do not qualify for senior discount.")
             #Input = yard type of service
            yard_service = input("\nPlease, enter what service for yard - mowing, edging or shrub pruning:\n")
            #Call function
            total_cost_of_service = yard_service_cost(yard_service, checked_age) 
            #Input = size of house
            size = input("\nPlease enter the size of your house: ")
            #Call function
            size = size_comparison(size)
            #Input = type of cleaning service
            typeOfCleaning = input("Please, enter what type of cleaning - dusting, floors or both:\n")
            #Call function
            total_house_cost = house_cleaning_cost(size, typeOfCleaning)
            #Print statement = total cost
            print("\nYour total yard and house cleaning service cost will be = ", total_cost_of_service + total_house_cost)

    #Exit gratefully
    print("\nThank you for choosing us")


#execution of main()
main()


