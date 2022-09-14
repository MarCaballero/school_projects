#What does the program do? It computes the weighted average grade for each student
#in a group of 4 student. Additionally, it determines which student has
#the highest average
#Major Design Steps:


#Developer Name: Maria Caballero
#CMIS-102 (6385)
#Date: 09/13/2022

#Include list of 4 student. Decide on the names.
def main():
    studentList = ["Michael", "Nicholas", "Maria", "Emerson"]
    for student in studentList:
        print(student)
        average = totalAveGrade(student)
        print("Your total average is = ", "%.2f" % average)

        compare = comparison(average)
        print("The max Average is ", compare)
            
            
def comparison(ave):
    maxAve = 0
    if ave > maxAverage:
        maxAverage = ave
        return maxAverage
        
          
def totalAveGrade(studentS):
    quiz_Weight = .40
    discussion_Weight = .25
    assignment_Weight = .35

    try:
        quiz_Grade = eval(input("Enter the given grade for quiz (0-10): "))
        if(quiz_Grade > 10 or quiz_Grade < 0):
            raise Exception("What the hell dude")
        if(discussion_Grade > 10 or discussion_Grade < 0):
            discussion_Grade = eval(input("Enter the given grade for discussion (0-10): "))
        if(assignment_Grade > 10 or assignment_Grade < 0):
            assignment_Grade = eval(input("Enter the given grade for assignment (0-10): "))
        total_Average = (quiz_Grade * quiz_Weight) + (discussion_Grade * discussion_Weight) + (assignment_Grade * assignment_Weight)
        return total_Average
    except Exception as e:
        if(e.__class__.__name__ == "NameError"):
            print("Input an actual number, not a string")
        else:
            print(e)
        
        totalAveGrade(studentS)
        



#Execution
main()


