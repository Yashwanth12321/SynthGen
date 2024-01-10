from faker import Faker
import pandas as pd
import datetime
import random
import string
import datetime
# from datetime import time
fake = Faker('en_IN')

def replace_newlines_with_comma_space(input_string):
    # Use the replace method to replace "\n" with ", "
    modified_string = input_string.replace("\n", ", ")
    return modified_string

def phonenumber():
    for _ in range(1):
        a =  "+91 " + str(fake.random_int(10000000, 9999999999))
    return a


def dob():
    for i in range(1):
        birthdate = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65)
        birthdate = birthdate.strftime("%d-%m-%Y")
    return birthdate



def all2(new_row: dict):
    state = fake.state()
    address = fake.street_address().replace("\n","").replace(",","")+","+fake.city().replace("\n","")+","+state.replace("\n","")
    new_row["address"].append(address)
    return new_row

def residential():

    res=["Day Scholar","Hosteller","Suspended"]
    
    return random.choice(res)





def all(new_row: dict):
    gender = fake.random_int(0, 1)
    if gender == 0:
        new_row["gender"].append('M')
        fname = fake.first_name_male()
        lname = fake.last_name_male()
    else:
        new_row["gender"].append('F')
        fname = fake.first_name_female()
        lname = fake.last_name_female()
    domain  = fake.free_email_domain()
    email = lname + '.' + fname + '@' + domain
    name = fname + " "+ lname
    new_row["firstname"].append(fname)
    new_row["lastname"].append(lname)
    new_row["email"].append(email)
    new_row["name"].append(name)
    return new_row

def all4(new_row: dict):
    departments_and_courses = {
    "Computer Science": ["Introduction to Programming", "Data Structures", "Algorithms", "Database Management", "Web Development"],
    "Mathematics": ["Calculus", "Linear Algebra", "Probability and Statistics", "Number Theory", "Differential Equations"],
    "Physics": ["Classical Mechanics", "Electromagnetism", "Quantum Mechanics", "Thermodynamics", "Astrophysics"],
    "Biology": ["Cell Biology", "Genetics", "Ecology", "Microbiology", "Human Anatomy"],
    "Psychology": ["Introduction to Psychology", "Abnormal Psychology", "Cognitive Psychology", "Social Psychology", "Developmental Psychology"],
    "History": ["World History", "American History", "European History", "Ancient History", "Medieval History"],
    "Chemistry": ["Inorganic Chemistry", "Organic Chemistry", "Physical Chemistry", "Analytical Chemistry", "Biochemistry"],
    "English": ["Literature", "Creative Writing", "Linguistics", "Shakespearean Studies", "Poetry"],
    "Economics": ["Microeconomics", "Macroeconomics", "International Economics", "Econometrics", "Development Economics"],
    "Art and Design": ["Drawing", "Painting", "Sculpture", "Graphic Design", "Art History"],
    "Mechanical Engineering": ["Thermodynamics", "Mechanics of Materials", "Fluid Mechanics", "Control Systems", "CAD/CAM"],
    "Environmental Science": ["Environmental Biology", "Climate Change Studies", "Environmental Policy", "Conservation Ecology", "Geospatial Analysis"]
}

    h = random.choice(list(departments_and_courses))
    courses = ""
    for i in departments_and_courses[h]:
        courses += (i + ", ")
        
    courses = courses[:len(courses)-2]
    new_row["department"].append(h)
    new_row["courses"].append(courses)
    return new_row


def all3(new_row:dict):
    # # dop=fake.date_between(start_date=datetime.datetime.strptime('01-01-2000', '%d-%m-%Y').date(),end_date='now')
    # dop = datetime.datetime(2020, 5, 17)
    # dop = fake.date_between(start_date=dop)
    # # x = datetime.datetime.strptime(dop, "%d-%m-%Y")
    # # x = dop.strftime("%d-%m-%Y")
    # days = fake.random_int(1,20)
    # dod = dop + datetime.timedelta(days=days)
    # dod = dod.strftime("%d-%m-%Y")
    # dop = dop.strftime("%d-%m-%Y")
    # new_row["dateofpurchase"].append(dop)
    # new_row["dateofdelivery"].append(dod)
    # return new_row
    start_date = datetime.datetime(2020, 5, 17)
    date = fake.date_between(start_date=start_date)
    date = date.strftime("%d-%m-%Y")
    year = ["1st year", "2nd year", "3rd year", "4th year"]
    yr = random.choice(year)
    new_row["admissiondate"].append(date)
    new_row["year"].append(yr)
    return new_row



def grade():
    l = ['A+', 'A', 'B', 'B+', 'C', 'C+', 'D', 'E', 'F']
    return random.choice(l)

def rollnumber():
    s = "MU"
    for i in range(0,4):
        s += str(random.randint(0,9))

    return s



def helloworld3(n: int, params:list, names: list):
    
    functions = {
        # "dob" : dob,
        "grade": grade,
        "rollnumber": rollnumber,
        "residential": residential,
    }

    df = pd.DataFrame(columns=names)
    
    relation1 = ["gender", "name", "firstname", "lastname", "email"]
    relation2 = ["department", "courses"]
    relation3 = ["admissiondate", "year"]

    # relation3 = ["profession", "role", "salary"]
    # curr_row = {"gender": [], "firstname": [], "lastname": [], "email": [], "name": []}
    # curr_row2 = {"address": [], "carplate":[]}
    # curr_row3 = {"profession": [], "role": [], "salary": []}
    for i in range(n):
        row = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        for j in range(len(params)):
            if params[j] in relation1:
                check = -1
                for x in range(0, len(l1)):
                    if(len(l1[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    curr_row = {"gender": [], "firstname": [], "lastname": [], "email": [], "name": []}
                    new = all(curr_row)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l1.append(new)
                else:
                    row.append(l1[check][params[j]][0])
                    l1[check][params[j]].clear()

            elif params[j] in relation2:
                check = -1
                for x in range(len(l2)):
                    if(len(l2[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    curr_row2 = {"department": [], "courses": []}
                    new = all4(curr_row2)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l2.append(new)
                else:
                    row.append(l2[check][params[j]][0])
                    l2[check][params[j]].clear()
                
            elif params[j] in relation3:
                check = -1
                for x in range(len(l3)):
                    if(len(l3[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    # relation3 = ["dateofpurchase", "dateofdelivery"]
                    curr_row3 = {"admissiondate": [], "year": []}
                    new = all3(curr_row3)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l3.append(new)
                else:
                    row.append(l3[check][params[j]][0])
                    l3[check][params[j]].clear()
            else:
                row.append(functions[params[j]]())
             
        df.loc[len(df.index)] = row



    with open("try.csv", "w") as file: 
        df.to_csv(file, index=False)