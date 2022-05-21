from sys import exit
import math
from tabulate import tabulate
#create class grade_find
def grade_find(mark):
  
  
  #if marks is greater or equal to 90
  if mark >= 90:
      #output results
      return ('S', 'Pass')
      #if marks is greater or equal to 80
  if mark >= 80:
      #output results
      return ('A', 'Pass')
      #if marks is greater or equal to 70
  if mark >= 70:
      #output results
      return ('B', 'Pass')
      #if marks is greater or equal to 60
  if mark >= 60:
      #display
      return ('C', 'Pass')
      #if marks is greater or equal to 50
  if mark >= 50:
      return ('D', 'Pass')
      ##if marks is  E show fail
  return ('E', 'Fail')
   
def main():
  while True:
    answer = input('Do you want to continue?:')
    if answer.lower().startswith("y"):
      
   
      #display student to eneter name
      #try catch to check is user inputs student name
      try:
        name = input("Enter the name of student: ")
        if not name:
          raise ValueError('empty student name')
      except ValueError as e:
        print(e)
        exit(0)
      
      #show subjects 
      subjects = ["English", "Science",
                  "Mathematics","Computer",  "Social Science"]
                  #display the calculated grade
      print("Subjects which grade is calculated:\nEnglish\nMathematics\nComputer\nScience\nSocial Science")
      #validate the list and results
     
      try:
        test_one = list(map(int, input(
          "Enter marks for test I (space separated values in order as above): ").split(' ')))
      except IndexError as e:
        print (e)
        
      except ValueError as e:
        print ('error type: ', type (e))
          #promt student to enter marks they got in results 2
      try:
        test_two = list(map(int, input(
          "Enter  test II Marks (space separated values in order as above): ").split(' ')))
      except IndexError as e:
        print (e)
        
      except ValueError as e:
        print ('error type: ', type (e))
          #display results
      try:
        test_three = list(map(int, input(
          "Enter  test III marks(space separated values ): ").split(' ')))
      except IndexError as e:
        print (e)
        
      except ValueError as e:
        print ('error type: ', type (e))
      #calculate the final results
      final_result = []
      #for in range loop
      for i in range(5):
          #to accept data
          data = []
          #calculate avaerage marks for all test
          try:
            avg_mark = (test_one[i]+test_two[i]+test_three[i])/3
          except ValueError as e:
            print ('error type: ', type (e))
          except IndexError as e:
            print (e)
          #show the grades and status
          grade, status = grade_find(avg_mark)
          #append data for the subjects
          data.append(subjects[i])
          #append data for average marks
          data.append(round(avg_mark, 2))
          #append grade
          data.append(grade)
          #append the status for grades
          data.append(status)
          #calculate for the final results
          final_result.append(data)
      # calculate the final marks
      final_mark = 0
      for i in range(5):
          #claculate the final marks and results
          final_mark += final_result[i][1]
          #calculate for average and round the results


       
      try: 
        avg_final_mark = round((final_mark/len(subjects)), 2)
        
      except(ArithmeticError, IOError): 
        print('Arrithmetic error')
        exit(0)
      #final step for calcuaton
      final_grade = grade_find(avg_final_mark)
      #display the name for the student
      print(f"Name of Student: {name}\n")
      #print the final subject, marks grade and status
      print(tabulate(final_result, headers=["Subject", "Mark", "Grade", "Status"]))
      #print the final average marks for the student
      print(f"Final Average Mark: {avg_final_mark}")
      #display the final grade
      print(f"Final Grade: {final_grade}")

    elif answer.lower().startswith("n"):
      print("ok, bye")
      exit(0)
    
if __name__ == '__main__':
  main()

   
