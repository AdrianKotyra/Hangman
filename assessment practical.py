import csv

def readMyFile(filename):
    name = []
    surname = []
    score = []

    with open("assess.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            name.append(row[0])
            surname.append(row[1])
            score.append(row[2])
    return name, surname, score

name, surname, score = readMyFile('file.csv')



def create_dict(name, surname, score):
    your_dict = {}
    for name, surname, score in zip(name, surname, score):
        your_dict[name, surname] = int(score)
    return your_dict
  

def get_people_with_score_150_and_higher(dict, number):
    print("3. People with score above ",number,":")
    print("------------------------------")
    for key, value in dict.items():
        if value >=number:
            
            print(key, value)
    print("------------------------------")

def total_amount_rised(amount):
    
    sum = 0
    for i in amount:
        sum= sum+int(i)
    return sum



def highest_person_score(amount):
    highest_score = int(amount[0])
    i=0
    while i <= len(amount)-1:
        if int(amount[i])>highest_score:
            highest_score=int(amount[i])
        i = i+1  
    return highest_score


sum = total_amount_rised(score)     
dict = create_dict(name, surname, score)  


def name_of_highest_score_person():
    d3 = {v: k for k,v in dict.items()}
    
    return d3[max(d3)]

highest_person_name = name_of_highest_score_person()

def print_all_tasks():
    print("------------------------------")
    print("1. Total of all peoples score -", sum)
    print("------------------------------")
    print("2. This is the highest score from list -", highest_person_score(score), highest_person_name)
    print("------------------------------")
    get_people_with_score_150_and_higher(dict, 150)

print_all_tasks()

        




