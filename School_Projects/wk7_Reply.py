#What program does?
    #1)Ask user to enter 5 elements/numbers
    #2)Adds 2 to each element/number the user inputted
    #3)Squares each element/number the user inputted
    #4)Displays the new element/number after the addition and square calculation
#Test Cases:
    #1) User Input: [2,4,6,8,10]
        #After addition calculation: [4,6,8,10,12]
        #After square calculation: [4,16,36,64,100]

    #2) User Input: [1,2,3,4,5]
        #After addition calculation: [3,4,5,6,7]
        #After square calculation: [1,4,9,16,25]

    #3) User Input: [14,27,9,81,42]
        #After addition calculation: [16,29,11,83,44]
        #After square calculation: [196,729,81,6561,1764]
#Developer Name: Maria Caballero
#CMIS-102 (6385): Wk7_Reply
#Date: 10/03/2022

def main():
    array1=[]
    array2=[]

    print("Enter 5 elements : ")
    for i in range(5):
        user_input = int(input())
        array1.append(user_input)
        array2.append(user_input)
    print()
    print("Addition array: ", addition(array1))
    print("Square array: ", square(array2))


def addition(array):
    addition_array = []
    #add 2 to each element
    for i in range(5):
        array[i]=array[i]+2
        addition_array.append(array[i])
    return addition_array


def square(array):
    square_array = []
    #square each element
    for i in range(5):
        array[i] = array[i]*array[i]
        square_array.append(array[i])
    return square_array

main()
