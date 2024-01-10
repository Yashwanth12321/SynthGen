from faker import Faker
import pandas as pd
import datetime
import random
import string
fake = Faker('en_IN')

def replace_newlines_with_comma_space(input_string):
    # Use the replace method to replace "\n" with ", "
    modified_string = input_string.replace("\n", ", ")
    return modified_string

def phonenumber():
    for _ in range(1):
        a =  "+91 " + str(fake.random_int(10000000, 9999999999))
    return a

def all2(new_row: dict):
    state = fake.state()
    address = fake.street_address().replace("\n","").replace(",","")+","+fake.city().replace("\n","")+","+state.replace("\n","")
    h=random.randrange(10,99)
    hr=random.randrange(1000,9999)
    indian_states = {
    'Andaman and Nicobar Islands': 'AN',
    'Andhra Pradesh': 'AP',
    'Arunachal Pradesh': 'AR',
    'Assam': 'AS',
    'Bihar': 'BR',
    'Chandigarh': 'CH',
    'Chhattisgarh': 'CG',
    'Dadra and Nagar Haveli and Daman and Diu': 'DN',
    'Delhi': 'DL',
    'Goa': 'GA',
    'Gujarat': 'GJ',
    'Haryana': 'HR',
    'Himachal Pradesh': 'HP',
    'Jammu and Kashmir': 'JK',
    'Jharkhand': 'JH',
    'Karnataka': 'KA',
    'Kerala': 'KL',
    'Lakshadweep': 'LD',
    'Madhya Pradesh': 'MP',
    'Maharashtra': 'MH',
    'Manipur': 'MN',
    'Meghalaya': 'ML',
    'Mizoram': 'MZ',
    'Nagaland': 'NL',
    'Odisha': 'OD',
    'Puducherry': 'PY',
    'Punjab': 'PB',
    'Rajasthan': 'RJ',
    'Sikkim': 'SK',
    'Tamil Nadu': 'TN',
    'Telangana': 'TS',
    'Tripura': 'TR',
    'Uttar Pradesh': 'UP',
    'Uttarakhand': 'UK',
    'West Bengal': 'WB'
    }

    cpf = indian_states[state]+str(h)+random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters).upper()+str(hr)
    new_row["address"].append(address)
    new_row["carplate"].append(cpf)
    return new_row


def all3(new_row:dict,min_salary: int, max_salary:int):
    profession_hierarchy = {
    'Management': {
        'General Manager': [80000, 150000],
        'Project Manager': [60000,120000],
        'HR Manager': [65000, 130000],
        'Sales Manager':  [70000, 140000],
    },
    'Information Technology': {
        'Software Engineer': [50000, 110000],
        'Data Scientist': [60000, 130000],
        'Network Administrator':  [55000, 120000],
        'Database Administrator': [60000, 125000],
    },
    'Healthcare': {
        'Doctor': [250000, 800000],
        'Nurse': [35000, 75000],
        'Pharmacist': [60000, 120000],
        'Dentist': [90000, 180000],
    },
    'Education': {
        'Teacher': [40000, 80000],
        'Professor': [60000, 140000],
        'School Principal': [70000, 150000],
        'Librarian': [45000, 90000],
    },
    }
    professions = list(profession_hierarchy.keys())
    # print(professions)
    gen = fake.random_int(0, len(professions) - 1)
    role = list(profession_hierarchy[professions[gen]].keys())
    gen_role = fake.random_int(0, len(role) - 1)
    # min_salary = profession_hierarchy[professions[gen]][role[gen_role]][0]
    # max_salary = profession_hierarchy[professions[gen]][role[gen_role]][1]
    salary = str(fake.random_int(min_salary, max_salary))
    salary = "Rs. " + salary

    new_row["profession"].append(professions[gen])

    new_row["salary"].append(salary)
    new_row["role"].append(role[gen_role])
    return new_row

def dob(new_row:dict, start_date: str, end_date:str):
    for i in range(1):
        birthdate = fake.date_of_birth(tzinfo=None, minimum_age=int(start_date), maximum_age=int(end_date))
        birthdate = birthdate.strftime("%d-%m-%Y")

    new_row["dob"].append(birthdate)
    return new_row

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



def helloworld(n: int, params:list, names: list, min_salary:list, max_salary:list, min_date: list, max_date: list):
    
    functions = {
        # "dob" : dob,
        "phonenumber": phonenumber,
    }

    df = pd.DataFrame(columns=names)
    
    relation1 = ["gender", "name", "firstname", "lastname", "email"]
    relation2 = ["address", "carplate"]
    relation3 = ["profession", "role", "salary"]
    relation4 = ["dob"]
    # curr_row = {"gender": [], "firstname": [], "lastname": [], "email": [], "name": []}
    # curr_row2 = {"address": [], "carplate":[]}
    # curr_row3 = {"profession": [], "role": [], "salary": []}
    for i in range(n):
        row = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        cnt = 0
        cnt2 = 0
        for j in range(len(params)):
            
            # print(len(min_salary))
            # print(len(max_salary))
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
                    curr_row2 = {"address": [], "carplate":[]}
                    new = all2(curr_row2)
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
                    curr_row3 = {"profession": [], "role": [], "salary": []}
                    new = all3(curr_row3, int(min_salary[cnt]), int(max_salary[cnt]))
                    cnt+=1
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l3.append(new)
                else:
                    cnt+=1
                    row.append(l3[check][params[j]][0])
                    l3[check][params[j]].clear()
            elif params[j] in relation4:
                check = -1
                for x in range(len(l4)):
                    if(len(l4[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    curr_row4 = {"dob": []}
                    new = dob(curr_row4, int(min_date[cnt2]), int(max_date[cnt2]))
                    cnt2+=1
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l4.append(new)
                else:
                    row.append(l4[check][params[j]][0])
                    l4[check][params[j]].clear()
                    cnt2+=1
            else:
                row.append(functions[params[j]]())
             
        df.loc[len(df.index)] = row



    with open("try.csv", "w") as file: 
        df.to_csv(file, index=False)