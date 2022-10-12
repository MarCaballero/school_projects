#What program does? Python program collects data of a road trip and calculate each person's share of the costs.
#Major Design Steps:
    #1) It prompts the user to input:
        #Number of People in the Trip
        #Number of Days of the trip
    #2) We initialize counter variables that will be used to iterate in while loops
    #3) We initialize arrays that will be used to store the values inputted by user and the calculations we will perform.
    #4) We will iterate through our first while loop to be able to prompt the user to enter costs of Food and Gas of each day.
    #5) We will iterate through our second while loop to be able to display the total cost of each day of the trip.
    #6) We will store values as the calculation of the total sum of each day total costs and the share of cost of each person.
    #7) We will display the total cost in general for all days in the trip and the share of cost of each person.
#Test Cases:
    #1)
        #Input:
            #Num of people on the trip = 10
            #Num of Days of the trip = 5
            #Food Cost = [50, 35, 98, 73, 100]
            #Gas Cost = [45, 15, 20, 37, 117]
        #Output:
            #Total Cost of each day = [95, 50, 118, 110, 217]
            #Total Cost of all days = 590
            #Total share costs of each person = 59

    #2)
        #Input:
            #Num of people on the trip = 7
            #Num of Days of the trip = 4
            #Food Cost = [35, 47, 88, 36]
            #Gas Cost = [55, 21, 34, 16]
        #Output:
            #Total Cost of each day = [90, 68, 122, 52]
            #Total Cost of all days = 332
            #Total share costs of each person = 47.43

    #3)
        #Input:
            #Num of people on the trip = 4
            #Num of Days of the trip = 7
            #Food Cost = [25, 29, 56, 71, 64, 18, 123]
            #Gas Cost = [10, 19, 24, 17, 34, 98, 14]
        #Output:
            #Total Cost of each day = [35, 48, 80, 88, 98, 116, 137]
            #Total Cost of all days = 602
            #Total share costs of each person = 150.50

#Developer Name: Maria Caballero
#CMIS-102 (6385) : Wk7_Assignment
#Date: 09/29/2022

def main():
#Prompt User for:
    #1) The number of people on the trip
    numOfPeople = int(input('Enter the number of people on the trip: '))
    #2) The number of days of the trip
    numOfDays = int(input('Enter the number of days for the trip: '))

#Counter variables for next loops
    #counter for while loop one
    Days = 0
    #counter for while loop two
    Days2 = 0
    
#Arrays that I will initialize as empty
    #Cost of Food initialization array
    costOfFood = []
    
    #Cost of Gas initialization array
    costOfGas = []
    
    #Calculation of total Cost it will be stored in an array
    totalCost = []

#The first while loop to enter costs of the trip (Food and Gas)
    #For each day of the trip, store in an array:
    while Days != numOfDays:
        #Add 1 to Days until it reaches the number of days of the trip
        Days = Days + 1
        print('\nEnter day ', Days, ' costs of trip.')
        #1) Cost of food
        foodCost = eval(input('\tFood cost = '))
        costOfFood.append(foodCost)
        #2) Cost of gas
        gasCost = eval(input('\tGas cost = '))
        costOfGas.append(gasCost)
    
    #print a new line
    print()

#The second while loop to display total cost of the trip for each day
    #displaying the total cost of food plus gas for each day of the trip
    while Days2 != numOfDays:
        for i in range(len(costOfFood)) and range(len(costOfFood)):
            totalCost.append(costOfFood[i] + costOfGas[i])
            Days2 = Days2 + 1
            print('\tTotal Cost of day ',Days2, ' is ', totalCost[i])

    #variables storing the sum of all total cost in general and the share of total costs for each person
    totalCostInGeneral = sum(totalCost)
    eachPersonShareOfTotalCost = totalCostInGeneral/numOfPeople

    #Displaying sum and share of total costs
    print('\nThe total cost of the whole trip is ', totalCostInGeneral)
    print('\tEach person share of cost = ', '%.2f' %eachPersonShareOfTotalCost)

#Execution   
main()
