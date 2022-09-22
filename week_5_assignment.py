def quiz_Ave(student):
    quiz_weight = .40
    try:
        quiz_grade = eval(input('Please enter your quiz grade (0-10): '))
        if(quiz_grade < 0 or quiz_grade > 10):
            raise Exception('Please, enter a number from 0 to 10\n')
        else:
            total_quiz_ave = quiz_weight * quiz_grade
            return total_quiz_ave
    
    except Exception as e:
        print(e)
    quiz_grade = eval(input('Quiz grade (0-10): '))
    total_quiz_ave = quiz_weight * quiz_grade
    return total_quiz_ave
    
    
def discussion_Ave(student):
    discussion_weight = .25
    try:
        discussion_grade = eval(input('Please enter your discussion grade (0-10): '))
        if(discussion_grade > 10 or discussion_grade <0):
            raise Exception("Please, enter a number from 0 to 10\n")
        else:
            total_discussion_ave = discussion_weight * discussion_grade
            return total_discussion_ave

    except Exception as e:
        print(e)
    discussion_grade = eval(input('Discussion grade (0-10): '))
    total_discussion_ave = discussion_weight * discussion_grade
    return total_discussion_ave


def assignment_Ave(student):
    assignment_weight = .35
    try:
        assignment_grade = eval(input('Please enter your assignment grade (0-10): '))
        if(assignment_grade < 0 or assignment_grade > 10):
            raise Exception('Please, enter a number from 0 to 10\n')
        else:
            total_assignment_ave = assignment_weight * assignment_grade
            return total_assignment_ave

    except Exception as e:
        print(e)
    assignment_grade = eval(input('Please enter your assignment grade (0-10): '))
    total_assignment_ave = assignment_weight * assignment_grade
    return total_assignment_ave
    


def total_Ave(quiz_ave, discussion_ave, assignment_ave):
    total = 0.0 
    total = quiz_ave + discussion_ave + assignment_ave
    return total
    

def main():
    studentList = ['Nick', 'Micke', 'Maria', 'Alex']
    maxAverage = 0
    maxAveStudent = None
    for student in studentList:
        print(student)
        quizzes = quiz_Ave(student)
        forum = discussion_Ave(student)
        homework = assignment_Ave(student)
        
        try:
            averages = total_Ave(quizzes, forum, homework)
            print('Your total average is ', '%.2f'%averages, '\n')
        except:
            print('Error ocurred!')
        averages= total_Ave(quizzes, forum, homework)

        if averages > maxAverage:
            maxAverage = averages
            maxAveStudent = student
                
            
    print(maxAveStudent, ' is the student who has the highest average of ', '%.2f'%maxAverage)
    
main()
    
    
