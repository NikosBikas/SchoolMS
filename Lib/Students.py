from datetime import date
from Lib.StudentsPerCourse import Person

class Students(Person):
    studentsList = []
    studentsMultipleCoursesList = []
    # Constructor
    def __init__(self, fname, lname, subject, tuitionfees, dateOfBirth):
       super().__init__(fname, lname, subject)
       self.tuitionfees = tuitionfees
       self.dateOfBirth = dateOfBirth
    
    def __str__(self):
        return f"Student's name is:{self.fname} {self.lname},learns{self.subject} Date of birth is: {self.dateOfBirth} and tuition fees are: {self.tuitionfees}"    
    
    def studentsPerCourse(self, dictionaryPerCourse):
        self.full_name = f"{self.fname} {self.lname}"

        for subj in self.subject:
        #iterating through the set that contains the languages
            if subj == 'C#':
                dictionaryPerCourse['C#'].append(self.full_name)
            elif subj == 'Java':
                dictionaryPerCourse['Java'].append(self.full_name)
            elif subj == 'JavaScript':
                dictionaryPerCourse['JavaScript'].append(self.full_name)
            else:
                dictionaryPerCourse['Python'].append(self.full_name)
        return dictionaryPerCourse    


# Function to create and append new student   
def addNewStudent():
    print("\n","Students information section".upper().center(100, '-'), "\n")
    while True:
        while True:
            try:
                fname = input("Enter student's first name: ")
            except ValueError:
                print('Invalid Input')
            if fname == "":
                print("This field cant be empty!")
                continue
            break 
        while True:
            try:
                lname = input("Enter student's last name: ")
                break
            except ValueError:
                print('Invalid Input')
            if lname == "":
                print("This field cant be empty!")
                continue
            break
        while True:
            try:
                tuitionfees = float(input("Enter student's fees (numeric): "))
                break
            except ValueError:
                print(" Your input has to be a number!")
        while True:
            try:
                date_Input = input("Enter Student's date_Input of Birth (YYYY-MM-DD): ")
                y, m, d = map(int, date_Input.split('-'))
                dateOfBirth = date(y, m, d)
                break
            except ValueError:
                print("Date is not in correct format (YYYY-MM-DD). Try again ")
                continue
        new_obj = Students(fname, lname, None, tuitionfees, dateOfBirth)
        Students.studentsList.append(new_obj)
        print("\n", ">New student: ", new_obj, "\n")
        if len(new_obj.subject) > 1:
            #checks if the student learns multiple languages, if true it appends it's name to the corresponding list
            Students.studentsMultipleCoursesList.append(f"{new_obj.fname} {new_obj.lname}")
        q = input("\nTo continue adding students press any key. To quit press 'q' ".center(100, '>'))
        if q == 'q':
            break
    return Students.studentsList

    

def dummyStudents():
    Students.studentsList.append(Students('Name1','Last_Name1',{'Python','C#'},2000,'1994-06-10'))
    Students.studentsList.append(Students('Name2','Last_Name2',{'Java','Python'},2000,'1987-08-15'))
    Students.studentsList.append(Students('Name3','Last_Name3',{'JavaScript'},2000,'1990-12-23'))
    Students.studentsList.append(Students('Name4','Last_Name4',{'C#'},2000,'1997-10-10'))
    Students.studentsList.append(Students('Name5','Last_Name5',{'Python'},2000,'1999-01-21'))
    Students.studentsList.append(Students('Name6','Last_Name6',{'Java'},2000,'1975-05-18'))
    Students.studentsList.append(Students('Name7','Last_Name7',{'Python'},2000,'1979-02-01'))
    Students.studentsList.append(Students('Name8','Last_Name8',{'Python','C#'},2000,"1993-10-03"))

    for std in Students.studentsList:
        #iterating through the list that contains dummy students
        if len(std.subject) > 1:
            #checks if the student learns multiple languages, if true it appends it's name to the corresponding list
            Students.studentsMultipleCoursesList.append(f"{std.fname} {std.lname}")
            
    return Students.studentsList  
 

def studentsToString(entity,studentsList):
    print("\nStudents are the following:")
    print("==========================")
    for item in range(len(studentsList)):
        print(f"{item + 1}. {studentsList[item]}") 

def stdsMultipleCoursesToString(itemsList):
    print("\nStudents are the following:")
    print("==========================")
    for item in range(len(itemsList)):
        print(f"{item + 1}. {itemsList[item]}") 

def stdsPerCourseToString(itemsList, case = True):
    dictionaryCourses = {'C#' : [], 'Java' : [], 'JavaScript' : [], 'Python' : []}
    print("Students Per Course:")
    print("==========================")
    for item in itemsList:
        item.studentsPerCourse(dictionaryCourses)
        #executed only for printing
    if case:
        for k, v in dictionaryCourses.items():
            print("\n", '---', k, '---')
            for v in range(len(dictionaryCourses[k])):
                print(f"{v+1}. {dictionaryCourses[k][v]}")
        return dictionaryCourses


    






        