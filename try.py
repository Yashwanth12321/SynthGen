
from faker import Faker
import pandas as pd
# from datetime import datetime

import random
import string
import datetime
fake = Faker('en_IN')
def all3():
    # dop = fake.date(pattern="%d-%m-%Y")
    # x = datetime.datetime.strptime(dop, "%d-%m-%Y")
    # days = fake.random_int(1,20)
    # dod = x + datetime.timedelta(days=days)
    # dod = dod.strftime("%d-%m-%Y")
    
    # # dop = fake.date_between_dates(date_start = '2023-09-12', date_end = '2023-09-25')
    # # dod = fake.date_between_dates(date_start = '2023-09-25', date_end = '2023-10-12')
    # # new_
    # print(dop)
    # print(dod)
    departments_and_courses = {
    "Computer Science": ["Introduction to Programming", "Data Structures", "Algorithms", "Database Management", "Web Development"],
    "Mathematics": ["Calculus", "Linear Algebra", "Probability and Statistics", "Number Theory", "Differential Equations"],
    "Physics": ["Classical Mechanics", "Electromagnetism", "Quantum Mechanics", "Thermodynamics", "Astrophysics"],
    "Biology": ["Cell Biology", "Genetics", "Ecology", "Microbiology", "Human Anatomy"],
    "Psychology": ["Introduction to Psychology", "Abnormal Psychology", "Cognitive Psychology", "Social Psychology", "Developmental Psychology"],
    "History": ["World History", "American History", "European History", "Ancient History", "Medieval History"]
    }
    h = random.choice(list(departments_and_courses))
    print(h)

all3()