import random
import math
from datetime import date

# admin authentication
def auth():
    username = input("Enter Username:")
    password = input("Enter Password:")
    if username == "admin" and password == "admin123":
        print("Welcomee Admin!")
        admin_menu()
    else:
        print("Invalid username and password. Try again!")
        auth()

# this function is for to get back to admin menu
def go_backto_admin():
    choice = int(input("Press 1 to go back to admin menu 0 to exit!"))
    if choice == 1:
        admin_menu()
    elif choice == 0:
        exit()
    else:
        print("invalid option")

# this function helps admin to view requests and ask admin for approval.
def approve():
    f = open("customer_details.txt", "r")
    print(f.read())
    choice=int(input("Press 1 to approve "))
    if choice==1:
        name=input("Enter the name you want to approve")
        approve1(name)
        print("approved sucessfully!")


    go_backto_admin()

# this function helps admin to approve requests.
def approve1(name):
    e=" "
    fin = open("customer_details.txt","rt")
    fout = open("registration.txt","at")
    f=open("registration.txt","a")
    check=False
    for i in fin:
        for j in i.split():
            if j==name:
                check=True
        if check==True:
            a=i.replace("NR","R")
            n=str(generate_id())
            f.write(" "+n+" ")
            random_date=str(generate_date())
            f.write(" " + random_date + " ")
            amt=str(generate_installment())
            f.write(" " + amt + " ")
            e=amt


            fout.writelines(a)

            break

    fin.close()
    fout.close()
    f.close()
    return e

def datetoday():
    today = date.today()
    return today

# this function helps to generate random ID
def generate_id():
    f = open("customer_details.txt", "r")
    n = random.randint(0, 50) #n represents randomly generated user ID
    return n

# generates random installment amount
def generate_p():
    n = random.randint(100000,150000)
    return n

def generate_installment():
    f = open("registration.txt", "r")
    n = generate_p()
    r = 12
    t = 3
    # for one month interest
    r = r / (12 * 100)
    # for one month period
    t = t * 12
    amt = (n * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    amt = math.floor(amt)
    return amt

# generate date for transaction.
def generate_date():
    f=open("registration.txt","r")
    import datetime
    import random
    start_date = datetime.date(2021, 8, 1)
    end_date = datetime.date(2022, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

# this function helps to show transaction of certain customer.
def view_trans_customer():
    f = open("transaction1.txt", "r")
    name = input("Enter the name of customer you want to search!")
    for i in f:
        c = 0
        for j in i.split():
            if c == 2:
                break
            if j == name:
                print(i)
            c = c + 1
    f.close()

# this function shows transaction of specific loan types.
def view_trans_specific_loan():
    f = open("transaction1.txt", "r")
    loan_type = input("Enter the code to search![El/HL/PL/CL/]")
    for i in f:
        c = 0
        for j in i.split():
            if c == 4:
                break
            if j == loan_type:
                print(i)
            c = c + 1
    f.close()

# this function shows transaction of all customers
def view_trans_allcustomer():
    f = open("transaction1.txt", "r")
    print(f.read())
    go_backto_admin()

# this function shows transaction of all loan types.
def view_trans_allloan_types():
    f = open("transaction1.txt", "r")
    print(f.read())
    go_backto_admin()

# this function shows admin menu.
def admin_menu():
    print("**********************************************************")
    print("1.View and Approve New Request")
    print("2.View transaction made by specific Customer")
    print("3.View transaction of specific loan types[EL/CL/HL/PL]")
    print("4.View transaction Of all Customer")
    print("5.View transaction of all loan types")
    print("6.Go back to main menu")
    print("7.Exit")
    print("**********************************************************")
    ch = int(input("Please select your choice:"))
    if ch == 1:
        approve()
    elif ch == 2:
        view_trans_customer()
    elif ch == 3:
        view_trans_specific_loan()
    elif ch == 4:
        view_trans_allcustomer()
    elif ch == 5:
         view_trans_allloan_types()
    elif ch == 6:
        welcome()
    elif ch == 7:
        exit()
    else:
        print("invalid option")

# this function is used to authenticate admin part.
def admin():
    auth()

# Loan Calculator for EL
def education_l():
    loan_amt = float(input("Please enter the amount of loan you wish to withdraw:"))
    time = float(input("How many years you want loan for?"))
    interest = (loan_amt*time*4)/100
    print("The total interest for entered amount is: ",interest)

# Loan Calculator for CL
def car_l():
    loan_amt = float(input("Please enter the amount of loan you wish to withdraw:"))
    time = float(input("How many years you want loan for?"))
    interest = (loan_amt * time * 7) / 100
    print("The total interest for entered amount is: ", interest)

# Loan Calculator for HL
def home_l():
    loan_amt = float(input("Please enter the amount of loan you wish to withdraw:"))
    time = float(input("How many years you want loan for?"))
    interest = (loan_amt * time * 6) / 100
    print("The total interest for entered amount is: ", interest)

# Loan Calculator for PL
def personal_l():
    loan_amt = float(input("Please enter the amount of loan you wish to withdraw:"))
    time = float(input("How many years you want loan for?"))
    interest = (loan_amt * time * 5) / 100
    print("The total interest for entered amount is: ", interest)


# this function shows the loan details provided by MBOLMS.
def loan_details():
    print("***** Following loans are provided by MBOLMS *****")
    print("1. Education Loan ** rate of interest is 4%")
    print("2. Car Loan ** rate of interest is 7%")
    print("3. Home Loan ** rate of interest is 6%")
    print("4. Personal Loan ** rate of interest is 5%")
    print("********************************************")
    ch = int(input("Press 1 to go back to customer menu for registration and 0 to exit:"))
    if ch == 1:
        new_customer()
    elif ch == 0:
        exit()
    else:
        print("invalid option")

# this function shows the menu for loan calculator.
def loan_calculator():
    print("*********************")
    print("1. Education Loan")
    print("2. Car Loan ")
    print("3. Home Loan ")
    print("4. Personal Loan")
    print("*********************")
    ch = int(input("Which type of loan you are looking for?"))

    if ch == 1:
        education_l()
    elif ch == 2:
        car_l()
    elif ch == 3:
        home_l()
    elif ch == 4:
        personal_l()
    else:
        print("invalid option")
    ch = int(input("Press 1 to go back to customer menu for registration and 0 to exit:"))
    if ch == 1:
        new_customer()
    elif ch == 0:
        exit()
    else:
        print("invalid option")

# this function is used to register new customers.
def registration():
    f = open("customer_details.txt", "a")
    f.write("\n")
    name = input("Enter your name:")
    password1 = input("Enter your password:")
    password0 = input("Please re-enter your password:")
    if password1 == password0:
        print("Password confirmed!")
    else:
        print("Invalid password.")
        registration()
    n = str(generate_id())
    email = input("Enter your email:")
    gender = input("Enter your gender:")
    dob = input("Enter your Date of birth in dd/mm/yyyy format:")
    address = input("Enter your address:")
    contact = (input("Enter Contact Number:"))
    loan_type = input("Enter loan type[EL/CL/HL/PL]:")
    loan_t = (input("How many years do you want the loan for?"))
    i_amount = (input("Enter the installment amount:"))
    f.write(n + " " + name + " "+ password1 +" " + "NR" + " " + email + " " + gender + " " + dob + " " + address + " " + contact + " " + loan_type + " " + loan_t + " " + i_amount )
    f.close()
    print("Registration complete! You can proceed to login!!")
    ch = int(input("Press 1 to go back to main menu and 0 to exit:"))
    if ch == 1:
        welcome()
    elif ch == 0:
        exit()
    else:
        print("invalid option")

# this function shows menu for new customer.
def new_customer():
    print("*********************")
    print("1.Loan Detail")
    print("2.Loan Calculator")
    print("3.Registration")
    print("4.Exit")
    print("*********************")
    ch = int(input("Please select your choice:"))
    if ch == 1:
        loan_details()
    elif ch == 2:
        loan_calculator()
    elif ch == 3:
        registration()
    elif ch == 4:
        exit()
    else:
        print("invalid option")

# Menu for registered users.
def reg_user1(username,password):
    print("***************************")
    print("1.Pay loan installment")
    print("2.See status of Loan")
    print("3.View Own transactions")
    print("4.Exit")
    print("***************************")
    ch = int(input("Select your choice"))
    if ch == 1:
        pay(username, password)
    elif ch == 2:
        view_status(username,password)
    elif ch == 3:
        own_transaction(username,password)
    elif ch == 4:
        exit()
    else:
        print("invalid option")

# authentication for registered users.
def authenticate(username,password):
    loan_type = " "
    f = open("registration.txt", "r")
    u=0
    p=0
    r=0
    loan_type=0
    for i in f:
        c=0
        for j in i.split():
            if c==13:
                break
            if j==username:
                u=1
            if j==password:
                p=1
            if j=="R":
                r=1
            if u == 1 and p == 1 and r == 1:
                if c>8and c<10:
                    loan_type = j

            c = c + 1
        if u == 1:
            break
    f.close()
    if u == 1 and p == 1 and r == 1:
        print("Logged In Successfully!!")
        reg_user1(username,password)

    else:
        print("Invalid username and password!")
        registered_customer1()

# this function helps to write specific loan type in transaction file.
def loan_type1(username,password):
    loan_type = " "
    f = open("registration.txt", "r")
    us = 0
    ps = 0
    rs = 0
    loan_type = 0
    for i in f:
        c = 0
        for j in i.split():
            if c == 13:
                break
            if j == username:
                us = 1
            if j == password:
                ps = 1
            if j == "R":
                rs = 1
            if us == 1 and ps == 1 and rs == 1:
                if c>8 and c<10:
                    loan_type = j

            c = c + 1
        if us == 1:
            break
    return loan_type

# this function allows customer to pay installment.
def pay(username,password):
    f = open("transaction1.txt", "a")
    loan_type = str(loan_type1(username, password))
    f.write(username + " ")
    amt = str(approve1(username))
    f.write(" " + amt + " ")
    f.write(" " + loan_type + " ")
    today = str(datetoday())
    f.write(" " + today + " ")
    f.write("\n")
    print("*****************************")
    print("Transaction success!!")
    print("*****************************")
    print("Name: ", username, "")
    print("Loan type: ", loan_type)
    print("Installment amount: ", amt)
    print("Date: ", today, "")
    print("*****************************")
    ch = int(input("Press 1 to go back to registered menu and 0 to exit:"))
    if ch == 1:
        reg_user1(username,password)
    elif ch == 0:
        exit()
    else:
        print("invalid option")

# this function helps customer to see either their loan is registered or not.
def view_status(username,password):
    f = open("registration.txt", "r")
    rs = 0
    for i in f:
        c = 0
        for j in i.split():
            if c == 13:
                break
            if j == "R":
                rs = 1
            c = c + 1
    f.close()
    if rs == 1:
        print("loan is registered!")
    ch = int(input("Press 1 to go back to registered menu and 0 to exit:"))
    if ch == 1:
        reg_user1(username,password)
    elif ch == 0:
        exit()
    else:
        print("invalid option")

# helps customer to view their own transactions.
def own_transaction(username,password):
    f = open("transaction1.txt", "r")
    for i in f:
        c = 0
        for j in i.split():
            if c == 2:
                break
            if j == username:
                print(i)
            c = c + 1
    print("\n")
    input("Press enter to continue")
    reg_user1(username, password)

# only works for customer approved by admin.
def registered_customer1():
    username = input("Enter username")
    password = input("Enter password")
    authenticate(username,password)

# shows welcome menu.
def welcome():
    print("*****************************")
    print("***** Welcome To MBOLMS *****")
    print("*****************************")
    print("1.Admin")
    print("2.New Customer")
    print("3.Registered Customer")
    ch = int(input("Please select your choice:"))

    if ch == 1:
        admin()
    elif ch == 2:
        new_customer()
    elif ch == 3:
        registered_customer1()
    else:
        print("invalid option")

welcome()


