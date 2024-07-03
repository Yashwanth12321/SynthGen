from faker import Faker
import pandas as pd
import datetime
import random
import string
import datetime
import os

a=2
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
    car_insurance_companies = [
        "ICICI Lombard General Insurance Company Ltd.",
        "HDFC ERGO General Insurance Company Ltd.",
        "Bajaj Allianz General Insurance Company Ltd.",
        "Reliance General Insurance",
        "TATA AIG General Insurance Company Ltd.",
        "New India Assurance Company Ltd.",
        "National Insurance Company Ltd.",
        "United India Insurance Company Ltd.",
        "Bharti AXA General Insurance",
        "IFFCO Tokio General Insurance Company Ltd.",
        "Go Digit General Insurance",
        "Royal Sundaram General Insurance",
        "Future Generali India Insurance",
        "Liberty General Insurance",
        "Shriram General Insurance",
        "Edelweiss General Insurance",
        "SBI General Insurance",
        "Universal Sompo General Insurance",
        "Kotak Mahindra General Insurance"
    ]

    comp = random.choice(car_insurance_companies)
    numb = (comp.split(" "))[0].upper()
    for i in range(10):
        numb += str(random.randint(0,9))
    
    premam = str(random.randint(2000,25000))
    premam = "Rs. " + premam
    new_row["company"].append(comp)
    new_row["premiumamount"].append(premam)
    new_row["insurancenumber"].append(numb)
    return new_row

def all5(new_row:dict):
    # dop=fake.date_between(start_date=datetime.datetime.strptime('01-01-2000', '%d-%m-%Y').date(),end_date='now')
    dop = datetime.datetime(2015, 5, 17)
    dop = fake.date_between(start_date=dop)
    # x = datetime.datetime.strptime(dop, "%d-%m-%Y")
    # x = dop.strftime("%d-%m-%Y")
    days = fake.random_int(1,30)
    ss = dop + datetime.timedelta(days=-100)
    dod = dop + datetime.timedelta(days=days)
    dol = dod + datetime.timedelta(days=365)
    dod = dod.strftime("%d-%m-%Y")
    dop = dop.strftime("%d-%m-%Y")
    dol = dol.strftime("%d-%m-%Y")
    ss = ss.strftime("%Y")
    # ss = ss.year()
    new_row["dateofpurchase"].append(dop)
    new_row["dateofinsurance"].append(dod)
    new_row["nextpremiumdate"].append(dol)
    new_row["manufactureyear"].append(ss)
    return new_row


def all3(new_row:dict):
    df = pd.read_csv("Cars_India_dataset.csv")
    n = len(df)
    ch = random.randint(0,n-1)
    comp = df.at[ch, "Maker"]
    model = df.at[ch, "Model"]
    type = df.at[ch, "Type"]
    new_row["carbrand"].append(comp)
    new_row["carmodel"].append(model)
    new_row["cartype"].append(type)
    return new_row

def all4(new_row: dict):
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


def grade():
    l = ['A+', 'A', 'B', 'B+', 'C', 'C+', 'D', 'E', 'F']
    return random.choice(l)

def rollnumber():
    s = "MU"
    for i in range(0,4):
        s += str(random.randint(0,9))

    return s

def price():
    return random.randint(1000000, 3500000)

def coverage():
    l = ["Liability Coverage", "Colission Coverage", "Personal Injury Coverage", "Uninsured Motorist Protection", "Comprehensive Coverage"]
    return random.choice(l)


def helloworld4(n: int, params:list, names: list):
    
    functions = {
        # "dob" : dob,
        "price": price,
        "phonenumber": phonenumber,
        "coverage": coverage,
    }

    df = pd.DataFrame(columns=names)
    
    relation1 = ["gender", "name", "firstname", "lastname", "email"]
    relation2 = ["company", "premiumamount", "insurancenumber"]
    relation3 = ["carbrand", "carmodel", "cartype"]
    relation4 = ["address", "carplate"]
    relation5 = ["dateofpurchase", "dateofinsurance", "nextpremiumdate", "manufactureyear"]


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
                    curr_row2 = {"company": [], "premiumamount": [], "insurancenumber": []}
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
                    curr_row3 = {"carbrand": [], "carmodel": [], "cartype": []}
                    new = all3(curr_row3)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l3.append(new)
                else:
                    row.append(l3[check][params[j]][0])
                    l3[check][params[j]].clear()
            elif params[j] in relation4:
                check = -1
                for x in range(len(l4)):
                    if(len(l4[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    # relation3 = ["dateofpurchase", "dateofdelivery"]
                    curr_row4 = {"address": [], "carplate": []}
                    new = all4(curr_row4)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l4.append(new)
                else:
                    row.append(l4[check][params[j]][0])
                    l4[check][params[j]].clear()

            elif params[j] in relation5:
                check = -1
                for x in range(len(l5)):
                    if(len(l5[x][params[j]])):
                        check = x
                        break
                if(check == -1):
                    # relation3 = ["dateofpurchase", "dateofdelivery"]
                    curr_row5 = {"dateofpurchase": [], "dateofinsurance": [], "nextpremiumdate": [], "manufactureyear": []}
                    new = all5(curr_row5)
                    row.append(new[params[j]][0])
                    new[params[j]].clear()
                    l5.append(new)
                else:
                    row.append(l5[check][params[j]][0])
                    l5[check][params[j]].clear()
            else:
                row.append(functions[params[j]]())
             
        df.loc[len(df.index)] = row



    with open("try.csv", "w") as file: 
        df.to_csv(file, index=False)