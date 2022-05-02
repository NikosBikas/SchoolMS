from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, fname, lname, subject):
        self.fname = fname
        self.lname = lname
        if subject == None:
            self.subject = self.addSubject()
        else:
            self.subject = subject

    def addSubject(self):
        availableSubjects = ('C#', 'Java', 'JavaScript', 'Python')
        self.subject = set()
        while True:
            new_subject = input(f"Enter subjects {availableSubjects} for this person or type 'stop' to stop entering: ")
            if new_subject in availableSubjects and new_subject != 'stop':
                self.subject.add(new_subject)
                continue
            elif new_subject == 'stop' and len(self.subject) == 0:
                print("Enter at least one of the available subjects before quiting!")
                continue                
            elif new_subject == 'stop':
                break
            else:
                print("Enter one of the supported subjects!")
                continue  
        return self.subject

    def perCourse(self, dictionaryPerCourse):
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




    



