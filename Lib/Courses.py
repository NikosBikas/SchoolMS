import time

class Courses:
    coursesList = []
    # Constructor
    def __init__(self, title, stream, type, startDate, endDate):
        self.title = title
        self.stream = stream
        self.type = type
        self.startDate = startDate
        self.endDate = endDate
    
    def __str__(self):
        return f"Course Title: {self.title} {self.stream} {self.type} Starts on: {self.startDate} and ends on: {self.endDate}"  
    

def addNewCourse():
    print("")
    while True:
        try:
            title = input('Enter Coure Title:')
        except ValueError:
            print("Invalid Input!")
            continue    
        if title == "":
            print("This field cant be empty!")
            continue
        break
    while True:    
        try:
            stream = input('Enter Course Stream:')
        except ValueError:
            print("Invalid Input!")
            continue               
        if stream == "":
            print("This field cant be empty!")
            continue
        elif stream != ("C#" or "Python" or "JavaScript" or "Java"):
            print("Wrong Input! Available options: C# , Python, JavaScript, Java")
            continue
        break
    while True:
        try:
            type = input('Enter Course Type:')
        except ValueError:
            print("Invalid Input!")
            continue               
        if type == "":
            print("This field cant be empty!")
            continue 
        elif type != ("Part_Time" or "Full_Time"):
            print("Wrong Input! Available options: Part_Time,Full_Time")
            continue
        break      
    while True:
        try:
            startDate = input('Enter Course Starting Date:')
        except ValueError:
            print("Invalid Input!")
            continue         
        if startDate == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try:                
            endDate = input('Enter Course End Date: ')
        except ValueError:
            print("This field cant be empty!")
            continue            
        if endDate == "":
            print("This field cant be empty!")
            continue
        #elif endDate != endDateObj:
        #   print("Incorect date string format! It should be YYYY-MM-DD")
        #    continue
        obj = Courses(title, stream, type, startDate, endDate)
        Courses.coursesList.append(obj)
        print("")
        print("New Course was added!")
        time.sleep(2)
        break
             



def dummyCourses():
    Courses.coursesList.append(Courses('CB13FTCS','C#','Full_Time','2021-18-10','2022-20-04'))
    Courses.coursesList.append(Courses('CB13FTJA','Java','Full_Time','2021-18-10','2022-20-04'))
    Courses.coursesList.append(Courses('CB13PTJS','Javascript','Part_Time','2021-18-10','2022-20-01'))
    Courses.coursesList.append(Courses('CB13FTPY','Python','Full_Time','2021-18-10','2022-20-04'))
    Courses.coursesList.append(Courses('CB13PTPY','Python','Part_Time','2021-18-10','2022-20-01'))

    return Courses.coursesList


def coursesToString(entity, coursesList):
    print("\nCourses are the following:")
    print("==========================")
    for item in range(len(coursesList)):
        print(f"{item + 1}. {coursesList[item]}")

#dummyCourses()
#coursesToString("Language courses", Courses.coursesList)
#addNewCourse()
#coursesToString("Language courses", Courses.coursesList)
