'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object using the information provided below
2) Create an instance of the Register object for EACH student in the 'students' list using a For loop.
3) Students can only register if the course is still 'open'. If the seats are filled, the course should be 'closed'.
4) Print out the student name, course name, CRN and number of seats left for each iteration using
   only GET methods.
5) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the file - Output.png.
'''

# Import the class to be used
import CourseClass as cc

def main():

   name = 'MIS 4322 - Advanced Python'
   crn = '250309'
   seats = 4
   status = 'open'
   students = ['John','James','Jill','Jack','Joanne']


   #create an instance of the course and name the instance 'python'
   python = cc.Course(name, crn, seats, status)

   #using a for loop register each student in the student list for the python course
   for student in students:
      if python.get_status() == 'open':
         register_Student = cc.Register(student, crn)
         python.update_seat_count()
         print(f"Student Name: {register_Student.get_name()}")
         print(f"Course Name: {python.get_name()}")
         print(f"CRN: {register_Student.get_crn()}")
         print(f"Seats left: {python.get_seats()}")
         print()
      else:
         print(f"Sorry {register_Student.get_name()}, registration is closed for {python.get_name()}")

#check if course is open
#create a register instance
#update seat count
#print out student details
#if course is not open, print appropriate message
    
main()



        
    
    
