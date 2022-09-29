#What program does?
    #It asks user to enter a list of numbers
    #Calculates the sum all numbers in the list
    #It calculates the square of each number on the list
#Test Cases:
    #1) 2, 4, 6, 8, 10
        #sum output =
        #square output =

    #2) 1, 2, 3, 4, 5
        #sum output =
        #square output =

    #3) 9, 14, 18, 7, 12
        #sum output =
        #square output =
#Developer Name: Maria Caballero
#CMIS-102 (6385): Wk7Discussion
#Date: 09/27/2022

def main():
    print('This program calculates the sum of numbers in a list and calculates the square of those numbers')
    #We initialize our list
    numList = list()
    #our counter for "while" loop
    count = 5
    #our counter for "for" loop
    count2 = 1

#asks user for 5 items/numbers to be inputted by user
    while count != 0:
        value = eval(input('Enter a number: '))
        numList.append(value)
        count = count - 1
        

#prints out each item/number in the inputted list by the user
    while count2 != 6:
        for i in range(len(numList)):
            print('\tItem ', count2, 'in your list is: ', numList[i])
            count2 = count2 + 1

#Calculates the sum of all the items/numbers in the list
    addition = sum(numList)
    print('The sum of all the items in your list is: ', addition)

#Calculates square of each item/number in the list
    for i in range(len(numList)):
        numList[i] = numList[i] * numList[i]
    print('The square of each number in your list is: ', numList)

    print('Thank you for participating')

main()
    
