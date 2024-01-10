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

def ordernumber():
    ans = ""
    for i in range(10):
        if i == 0:
            ans += str(random.randint(1,9))
        else:
            ans += str(random.randint(0,9))

    return ans



def customernumber():
    ans = ""
    for i in range(15):
        if i == 0:
            ans += str(random.randint(1,9))
        else:
            ans += str(random.randint(0,9))

    return ans



def itemnumber():
    ans = ""
    for i in range(8):
        if i == 0:
            ans += str(random.randint(1,9))
        else:
            ans += str(random.randint(0,9))

    return ans

def all2(new_row: dict):
    state = fake.state()
    address = fake.street_address().replace("\n","").replace(",","")+","+fake.city().replace("\n","")+","+state.replace("\n","")
    new_row["address"].append(address)
    return new_row



def all4(new_row: dict):
    payment_modes = [
        "Cash",
        "Credit Card",
        "Debit Card",
        "Bank Transfer",
        "Cheque",
        "Mobile Wallet",
        "UPI (Unified Payments Interface)",
        "Digital Payment Apps",
        "Net Banking",
        "PayPal",
        "Prepaid Cards",
        "Contactless Payments",
        "Gift Cards",
        "Money Orders",
        "Direct Debit",
        "Online Payment Gateways",
        "Invoice Payment",
        "Cash on Delivery (COD)",
        "Installment Plans",
        "Electronic Funds Transfer (EFT)"
    ]
    ch = random.choice(payment_modes)
    id = ""
    for i in range(10):
        id += str(random.randint(0,9))

    id = ch[:3].upper() + id
    new_row["paymentmethod"].append(ch)
    new_row["paymentid"].append(id)
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

def all3(new_row:dict):
    # dop=fake.date_between(start_date=datetime.datetime.strptime('01-01-2000', '%d-%m-%Y').date(),end_date='now')
    dop = datetime.datetime(2020, 5, 17)
    dop = fake.date_between(start_date=dop)
    # x = datetime.datetime.strptime(dop, "%d-%m-%Y")
    # x = dop.strftime("%d-%m-%Y")
    days = fake.random_int(1,20)
    dod = dop + datetime.timedelta(days=days)
    dod = dod.strftime("%d-%m-%Y")
    dop = dop.strftime("%d-%m-%Y")
    new_row["dateofpurchase"].append(dop)
    new_row["dateofdelivery"].append(dod)
    return new_row

def all5(new_row:dict):
    df = pd.read_csv("description.csv")
    n = len(df)
    randi = random.randint(0,n-1)
    price_euro = df.at[randi, "price"].split(",")
    price_euro = int(price_euro[0])
    price_ind = price_euro * 85
    price_ind  = str(price_ind)
    price_ind = "Rs. " + price_ind
    new_row["description"].append(df.at[randi,"description"])
    new_row["price"].append(price_ind)
    return new_row

def orderstatus():
    order_statuses = [
        "Pending",
        "Processing",
        "Shipped",
        "Delivered",
        "Partially Shipped",
        "Cancelled",
        "On Hold",
        "Refunded",
        "Backordered",
        "Payment Pending",
        "Completed",
        "In Progress",
        "Ready for Pickup",
        "Awaiting Payment",
        "Disputed",
        "On Backorder",
        "Hold for Review",
        "Preparation in Progress",
        "Customization in Progress",
        "Delayed"
        ]
    return random.choice(order_statuses)

def helloworld2(n: int, params:list, names: list):
    
    functions = {
        "dob" : dob,
        "phonenumber": phonenumber,
        "ordernumber": ordernumber,
        "customernumber": customernumber,
        "itemnumber": itemnumber, 
        "orderstatus": orderstatus,
    }

    df = pd.DataFrame(columns=names)
    
    relation1 = ["gender", "name", "firstname", "lastname", "email"]
    relation2 = ["address"]
    relation3 = ["dateofpurchase", "dateofdelivery"]
    relation4 = ["paymentmethod", "paymentid"]
    relation5 = ["description", "price"]

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
                    curr_row2 = {"address": []}
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
                    # relation3 = ["dateofpurchase", "dateofdelivery"]
                    curr_row3 = {"dateofpurchase": [], "dateofdelivery": []}
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
                    # relation4 = ["paymentmethod", "paymentid"]
                    curr_row4 = {"paymentmethod": [], "paymentid": []}
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
                    # relation5 = ["description", "price"]
                    curr_row5 = {"description": [], "price": []}
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