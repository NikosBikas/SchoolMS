from datetime import date
from random import randint

class Assignments:
    assignmentsList = []
    # Constructor
    def __init__(self, subject, title, description, subDatetime,oralMark=None,totalMark=None):
        self.subject = subject
        self.title = title
        self.description = description
        self.subDatetime = subDatetime
        self.oralMark = oralMark
        self.totalMark = totalMark

    def __str__(self):
            return f"Title: {self.title} Description: {self.description} Submission date is: {self.subDatetime}"

    def assPerCourse(self, dictionaryAssPerCourse):
        self.full_string = f"Title: {self.title} Description: {self.description} Submission date is: {self.subDatetime}"
        for subj in self.subject:
        #iterating through the set that contains the languages
            if subj == 'C#':
                dictionaryAssPerCourse['C#'].append(self.full_string)
            elif subj == 'Java':
                dictionaryAssPerCourse['Java'].append(self.full_string)
            elif subj == 'JavaScript':
                dictionaryAssPerCourse['JavaScript'].append(self.full_string)
            else:
                dictionaryAssPerCourse['Python'].append(self.full_string)
        return dictionaryAssPerCourse 

    def stdsPerCourse(self, dictionaryStdsPerCourse):
        self.full_name = f"{self.fname} {self.lname}"

        for subj in self.subject:
        #iterating through the set that contains the languages
            if subj == 'C#':
                dictionaryStdsPerCourse['C#'].append(self.full_name)
            elif subj == 'Java':
                dictionaryStdsPerCourse['Java'].append(self.full_name)
            elif subj == 'JavaScript':
                dictionaryStdsPerCourse['JavaScript'].append(self.full_name)
            else:
                dictionaryStdsPerCourse['Python'].append(self.full_name)
        return dictionaryStdsPerCourse    

    
def addNewAssignment():
    print("\n", "Assignment information section".upper().center(100,'-'), "\n")
    availableSubjects = ('C#', 'Java', 'JavaScript', 'Python')
    while True:
        subject = input(f"Select the language {availableSubjects} that this assignment refers to or press 'stop' to quit: ")
        if subject in availableSubjects:
            print("\nFor the assignment enter the following: Title, Description, Date of Submission.")
            title = input("Title: ")
            description = input("Description: ")
            while True:
                try:
                    date_entry = input("Deadline date of assignment submission (YYYY-MM-DD): ")
                    y, m, d = map(int, date_entry.split('-'))
                    subDatetime = date(y, m, d)
                    break
                except ValueError:
                    print("Date is not in correct format (YYYY-MM-DD). Try again ".center(85,'*'), "\n")
                    continue
            newObj = Assignments({subject},title,description,subDatetime)
            Assignments.assignmentsList.append(newObj)
            print("\n", ">New assignment: ", newObj, "\n")
        elif subject == 'stop':
            break
        else:
            print("\n", " Enter one of the available languages or check for typos ".center(85,'*'), "\n")
    return Assignments.assignmentsList



def dummyAssignments():
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 1','Individual Project 1','2021-11-29'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 2','Individual Project - Part A','2021-12-21'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 3','Individual Project - Part B','2022-02-02'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 4','Second Assignment','2022-02-24'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 5','Third Assignment','2022-03-09'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 6','Fourth Assignment','2022-03-15'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 7','Fifth Assignment','2022-03-21'))
    Assignments.assignmentsList.append(Assignments({'JavaScript','Python','C#','Java'},'Assignment 8','Group Project','2022-04-26'))

    return Assignments.assignmentsList



def assignmentsToString(entity, assignmentsList):
    print("\nAssignmets are the following:")
    print("=============================")
    for item in range(len(assignmentsList)):
        print(f"{item + 1} .{assignmentsList[item]}")


def assignmentsPerCourseToString(itemsList,case=True):
    dictionaryCourses = {'C#' : [], 'Java' : [], 'JavaScript' : [], 'Python' : [],}
    print("Assignments Per Course:")
    print("==========================")
    for item in itemsList:
        item.assPerCourse(dictionaryCourses)
        #executed only for printing
    if case:
        for k, v in dictionaryCourses.items():
            print("\n", '---', k, '---')
            for v in range(len(dictionaryCourses[k])):
                print(f"{v+1}. {dictionaryCourses[k][v]}")
        return dictionaryCourses



