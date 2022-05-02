import time
from Lib.TrainersPerCourse import Person

# Create class "Trainers"
class Trainers(Person):
    trainersList = []
    # Constructor
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname, subject)

    def __str__(self):
            return f"Trainer name: {self.fname} {self.lname} and teaches: {self.subject}"

    def trainersPerCourse(self, dictionaryPerCourse):
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

def addNewTrainer():
    print("")    
    while True:
        try:
            fname = input("Enter trainer's first name: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if fname == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try:
            lname = input("Enter trainer's last name: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if lname == "":
            print("This field cant be empty!")
            continue
        new_obj = Trainers(fname, lname, None)
        Trainers.trainersList.append(new_obj)        
        print("")
        print("New Trainer was added!")
        time.sleep(2)
        break 

def dummyTrainers():
    Trainers.trainersList.append(Trainers('Sarantia','Tyrovola',{'Python','JavaScript'}))
    Trainers.trainersList.append(Trainers('George','Pasparakis',{'C#','JavaScript','Python','Java'}))
    Trainers.trainersList.append(Trainers('Antonios','Thodos',{'JavaScript'}))
    Trainers.trainersList.append(Trainers('Lena','Kapetanaki',{'JavaScript'}))
    Trainers.trainersList.append(Trainers('Danae','Tzoumba',{'Python'}))

    return Trainers.trainersList    

def trainersToString(entity, trainersList):
    print("\nTrainers are the following:")
    print("==========================")
    for item in range(len(trainersList)):
        print(f"{item + 1}. {trainersList[item]}")

def trainersPerCourseToString(itemsList, case = True):
    dictionaryCourses = {'C#' : [], 'Java' : [], 'JavaScript' : [], 'Python' : []}
    for item in itemsList:
        item.trainersPerCourse(dictionaryCourses)
        #executed only for printing
    if case:
        for k, v in dictionaryCourses.items():
            print("\n", '---', k, '---')
            for v in range(len(dictionaryCourses[k])):
                print(f"{v+1}. {dictionaryCourses[k][v]}")
        return dictionaryCourses
#dummyTrainers()
#trainersToString("Trainers", Trainers.trainersList)
#addNewTrainer()
#trainersToString("Trainers", Trainers.trainersList)
