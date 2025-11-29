import datetime
import time
import random
import string
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validateSuperAdminLogin():
    admin_file = ""
    try:
        admin_file = open('superAdminAcc.txt', 'r')
    except Exception as error:
        print("No Super Admin Account File Information Found")
        exit()
    admin_file_all_lines = admin_file.readlines()
    valid_superadmin = False
    invalid_counter = 1
    while not valid_admin:
        admin_id_entered = input("Enter Admin ID:")
        admin_id_entered = admin_id_entered.strip()
        admin_pass_entered = input("Enter Admin password:")
        admin_pass_entered = admin_pass_entered.strip()

        for ind in range(0, len(admin_file_all_lines)):
            if admin_file_all_lines[ind].startswith("Super Admin ID:"):
                admin_id_line_list = admin_file_all_lines[ind].split(":")
                admin_id_in_file = admin_id_line_list[1].strip()

                admin_pass_line_list = admin_file_all_lines[ind + 1].split(":")
                admin_pass_in_file = admin_pass_line_list[1].strip()

                if admin_id_in_file == admin_id_entered and admin_pass_in_file == admin_pass_entered:
                    valid_superadmin = True
                    break
                elif valid_admin == False:
                    print("Invalid admin details entered. Try again")
                    invalid_counter = invalid_counter + 1
                    if invalid_counter > 4:
                        print("Too many attempts. Logging out. Try again later.")
                        exit()
    return valid_superadmin



def validateAdminLogin():
    admin_file = ""
    try:
        admin_file = open('admin.txt', 'r')
    except Exception as error:
        print("No Admin File Information Found")
        exit()
    admin_file_all_lines = admin_file.readlines()

    valid_admin= False
    invalid_counter = 1
    while not valid_admin:
        admin_id_entered = input("Enter Admin ID:")
        admin_id_entered = admin_id_entered.strip()
        admin_pass_entered = input("Enter Admin password:")
        admin_pass_entered = admin_pass_entered.strip()

        for ind in range(0, len(admin_file_all_lines)):
            if admin_file_all_lines[ind].startswith("Admin ID:"):
                admin_id_line_list = admin_file_all_lines[ind].split(":")
                admin_id_in_file = admin_id_line_list[1].strip()

                admin_pass_line_list = admin_file_all_lines[ind+1].split(":")
                admin_pass_in_file = admin_pass_line_list[1].strip()

                if admin_id_in_file == admin_id_entered and admin_pass_in_file == admin_pass_entered:
                    valid_admin = True
                    break

        if valid_admin == False:
            print("Invalid admin details entered. Try again")
            invalid_counter = invalid_counter +1
            if invalid_counter>4:
                print("Too many attempts. Logging out. Try again later.")
                exit()
    return valid_admin


def validateCustomerLogin():
    valid_customer = False
    customer_AccountNO_entered = input("Enter your account number: ")
    customer_AccountNO_entered = customer_AccountNO_entered.strip()
    customer_ID_entered = input("Enter your customer ID: ")
    customer_ID_entered = customer_ID_entered.strip()
    account_pass_entered = input("Enter the password for your account:")
    account_pass_entered = account_pass_entered.strip()

    accounts = ""
    try:
        accounts = open('accounts.txt', 'r+')
    except Exception as error:
        print("Accounts file Not Found")
        exit()

    account_file_all_lines = accounts.readlines()
    for ind in range(0, len(account_file_all_lines)):
        if account_file_all_lines[ind].startswith("Account no:"):
            account_number_line_list = account_file_all_lines[ind].split(":")
            account_number_in_file = account_number_line_list[1].strip()

            customer_ID_line_list = account_file_all_lines[ind + 1].split(":")
            customer_ID_in_file = customer_ID_line_list[1].strip()

            account_pass_line_list = account_file_all_lines[ind + 2].split(":")
            account_pass_in_file = account_pass_line_list[1].strip()

            if account_number_in_file == customer_AccountNO_entered and customer_ID_in_file == customer_ID_entered and account_pass_in_file == account_pass_entered:
                valid_customer = True
                displayCustomerName(customer_ID_entered)
                break
    return valid_customer


def displayCustomerName(customer_ID_entered):
    CustomerFile = ""
    try:
        CustomerFile = open('customer.txt','r+')
    except Exception as error:
        print("Customer File Not Found")
        exit()

    CustomerFileContent=CustomerFile.readlines()
    for ind in range(0, len(CustomerFileContent)):
        if CustomerFileContent[ind].startswith('Customer ID:'):
            CustomerIDList = CustomerFileContent[ind].split(':')
            CustomerIDInFile = CustomerIDList[1].strip()
            if customer_ID_entered == CustomerIDInFile:
                CustomerFNameList = CustomerFileContent[ind+1].split(":")
                CustomerFName = CustomerFNameList[1].strip()
                CustomerLNameList = CustomerFileContent[ind+2].split(":")
                CustomerLName = CustomerLNameList[1].strip()
                print("===========================================================")
                print('Hello', CustomerFName, CustomerLName, ', Welcome to the PYP banking system ')
                print("===========================================================")



def randomPasswordGenerator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))


def createAdminAccount():
    latest_account_number_file=""
    try:
        latest_account_number_file = open('latestAccountNumberAdmin.txt', 'r')
    except Exception as error:
        print("Latest Account Number File Not Found")
        exit()
    latest_account_number = int(latest_account_number_file.readline())
    latest_account_number_file.close()
    adminID = latest_account_number_file 
    latest_account_number_file = open('latestAccountNumberAdmin.txt', 'w')
    latest_account_number = latest_account_number + 1
    latest_account_number_file.write(str(latest_account_number))
    latest_account_number_file.close()
    password = randomPasswordGenerator()
    print('Admin account ID is', adminID)
    print('Admin account Password is', password)
    admin_file = open('admin.txt', 'a+')
    admin_file.write("Admin ID: ",adminID)
    admin_file.write("Admin password: ",password )
    admin_file.write("================================\n")
    admin_file.close()



def approveCustomer():
    print("Approving customer")
    approval_needed_file = ""
    try:
        approval_needed_file = open('approval_needed.txt', 'r')
    except Exception as error:
        print("Approval File Not Found")
        exit()

    all_lines_in_approval = approval_needed_file.readlines()
    if len(all_lines_in_approval) == 0:
        print("No  more approvals needed")
        exit()
    approval_needed_file.close()

    for ind in range(0, len(all_lines_in_approval)):
        if all_lines_in_approval[ind].startswith("First Time Customer: "):
            first_time_line_list = all_lines_in_approval[ind].split(":")
            first_time_customer = first_time_line_list[1].strip()
            if first_time_customer == 'Yes' and  all_lines_in_approval[ind+8].endswith("Pending\n"):
                print("=======Customer given details=======")
                print(all_lines_in_approval[ind + 1], end="")
                print(all_lines_in_approval[ind + 2], end="")
                print(all_lines_in_approval[ind + 3], end="")
                print(all_lines_in_approval[ind + 4], end="")
                print(all_lines_in_approval[ind + 5], end="")
                print(all_lines_in_approval[ind + 6], end="")
                print(all_lines_in_approval[ind + 7], end="")
                print("===================================")
                approve_yes_or_no = ""
                invalid_input_counter=0
                while approve_yes_or_no not in ['y', 'n']:
                    approve_yes_or_no = input("Do you wish you approve the account creation? y or n")
                    invalid_input_counter = invalid_input_counter+1
                    if invalid_input_counter == 4:
                        print("Invalid value entered too many times. Logging out. Try again!!")
                        exit()
                if approve_yes_or_no == 'n':
                    all_lines_in_approval[ind + 8] = "Approval Status: Denied\n"
                    approval_needed_file_to_deny = open('approval_needed.txt', 'w+')
                    approval_needed_file_to_deny.writelines(all_lines_in_approval)
                    approval_needed_file_to_deny.close()
                    break
                elif approve_yes_or_no == 'y':

                    customer_file = open('customer.txt', 'a+')
                    customer_file.write("=================================================\n")
                    customer_file.write(all_lines_in_approval[ind+1])
                    customer_file.write(all_lines_in_approval[ind+2])
                    customer_file.write(all_lines_in_approval[ind+3])
                    customer_file.write(all_lines_in_approval[ind+4])
                    customer_file.write(all_lines_in_approval[ind+5])
                    customer_file.write("=================================================\n")
                    customer_file.close()

                    latest_account_number_file=""
                    try:
                        latest_account_number_file = open('latestAccountNumber.txt', 'r')
                    except Exception as error:
                        print("Latest Account Number File Not Found")
                        exit()
                    latest_account_number = int(latest_account_number_file.readline())
                    latest_account_number_file.close()

                    account_file = open('accounts.txt', 'a+')
                    account_file.write("=================================================\n")
                    account_file.write("Account no:"+str(latest_account_number)+'\n')
                    account_file.write(all_lines_in_approval[ind+1]) # customer ID
                    #  random password
                    password = randomPasswordGenerator()
                    account_file.write("Account Password: " + password+'\n')
                    account_file.write(all_lines_in_approval[ind + 6]) # account type
                    account_file.write("Account Creation date:"+str(datetime.datetime.now())+'\n') # account creation time
                    # adding balance
                    bal_line = all_lines_in_approval[ind + 7].split(":")
                    bal = bal_line[1].strip()
                    account_file.write("Account Balance: "+ bal+'\n')
                    account_file.write("=================================================\n")

                    account_file.close()

                    # after approving, making changes to the approval status in the approval_neded txt file
                    all_lines_in_approval[ind+8] = "Approval Status: Approved\n"
                    all_lines_in_approval[ind + 9] = "Account number: " + str(latest_account_number) +"\n"
                    all_lines_in_approval[ind + 10] = "Account Password: "+ str(password) +"\n"

                    approval_needed_file = open('approval_needed.txt', 'w+')
                    approval_needed_file.writelines(all_lines_in_approval)
                    approval_needed_file.close()

                    # uodating the latest account number
                    latest_account_number_file = open('latestAccountNumber.txt', 'w')
                    latest_account_number = latest_account_number + 1
                    latest_account_number_file.write(str(latest_account_number))
                    latest_account_number_file.close()

            if first_time_customer == 'No' and all_lines_in_approval[ind+4].endswith("Pending\n"):
                print("=======Customer given details=======")
                print(all_lines_in_approval[ind + 1], end="")
                print(all_lines_in_approval[ind + 2], end="")
                print(all_lines_in_approval[ind + 3], end="")
                print("===================================")
                approve_yes_or_no = input("Do you wish you approve the account creation? y or n")
                while approve_yes_or_no not in ['y', 'n']:
                    approve_yes_or_no = input("Do you wish you approve the account creation? y or n")
                    invalid_input_counter = invalid_input_counter+1
                    if invalid_input_counter == 3:
                        print("Invalid value entered too many times. Logging out. Try again!!")
                        exit()

                if approve_yes_or_no == 'n':
                    all_lines_in_approval[ind + 4] = "Approval Status: Denied\n"
                    approval_needed_file_to_deny = open('approval_needed.txt', 'w+')
                    approval_needed_file_to_deny.writelines(all_lines_in_approval)
                    approval_needed_file_to_deny.close()
                    break
                else:
                    latest_account_number_file=""
                    try:
                        latest_account_number_file = open('latestAccountNumber.txt', 'r')
                    except Exception as error:
                        print("Latest Account Number File Not Found")
                        exit()
                    latest_account_number = int(latest_account_number_file.readline())
                    latest_account_number_file.close()

                    account_file = open('accounts.txt', 'a+')
                    account_file.write("=================================================\n")
                    account_file.write("Account no:" + str(latest_account_number) + '\n')
                    account_file.write(all_lines_in_approval[ind + 1])  # customer ID
                    #  random password
                    password = randomPasswordGenerator()
                    account_file.write("Account Password: " + password + '\n')
                    account_file.write(all_lines_in_approval[ind + 2])  # account type
                    account_file.write("Account Creation date:" + str(datetime.datetime.now()) + '\n')  # account creation time
                    # adding balance
                    bal_line = all_lines_in_approval[ind + 3].split(":")
                    bal = bal_line[1].strip()
                    account_file.write("Account Balance: " + bal + '\n')
                    account_file.write("=================================================\n")

                    account_file.close()

                    # after approving, making changes to the approval status in the approval_neded txt file
                    all_lines_in_approval[ind + 4] = "Approval Status: Approved\n"
                    all_lines_in_approval[ind + 5] = "Account number: " + str(latest_account_number) + "\n"
                    all_lines_in_approval[ind + 6] = "Account Password: " + str(password) + "\n"

                    approval_needed_file = open('approval_needed.txt', 'w+')
                    approval_needed_file.writelines(all_lines_in_approval)
                    approval_needed_file.close()

                    # uodating the latest account number
                    latest_account_number_file = open('latestAccountNumber.txt', 'w')
                    latest_account_number = latest_account_number + 1
                    latest_account_number_file.write(str(latest_account_number))
                    latest_account_number_file.close()



def WelcomePage():
    print('  ===================================================  Hello and welcome to the PYP Banking system  ===================================================  ')
    print('what would u like to do today ?', '1.)Login to your bank account', '2.)Create a new bank account','3.)Check approval staus', sep="\n")


def NewAccount():

    first_time_cust = input('Is this your first time banking with us? enter y for yes and n for no')
    n=1
    while first_time_cust not in ['y','n']:
        print('============================================================')
        print('Invalid option chosen')
        first_time_cust = input('Is this your first time banking with us? enter y for yes and n for no')
        n=n+1
        if n >= 4:
            print('Invalid option chosen too many times, process will be terminated. ')
            print('============================================================')
            exit()

    CustomerID=""
    InitialAmt = int()
    invalid_counter = 1
    while type(CustomerID) != int:
        try:
            CustomerID = int(input('Enter your customerID: '))
        except:
            invalid_counter = invalid_counter +1
            print("Enter Numeric value only")
            if invalid_counter == 4:
                print("Too may wrong attempts. Logging out. Please try again later!!")
                exit()
            continue

    if first_time_cust == 'y':

        AccountType=""
        invalid_counter = 1
        while AccountType not in [1, 2]:
            try:
                print("======================================================")
                print("Enter only the given choices")
                AccountType = int(input("what is the type of account you'd like to create: 1.)Savings 2.)Current"))
            except ValueError as ve:
                print("Enter a numeric value")
            invalid_counter = invalid_counter+1
            if invalid_counter==4:
                print("Too many attempts. Logging out. Try again")
                exit()




        if AccountType == 1:
            print('Minimum amount in this account must be 100 RM')
            InitialAmt = int()
            invalid_counter =1
            while InitialAmt < 100:
                try:
                    InitialAmt = int(input('Enter the amount you would like to start off with:'))
                    if InitialAmt < 100:
                        print('Amount is too less to open a bank account, minimum amount in a saving account is 100 RM,')
                except:
                    print("Invalid number entered.")
                    invalid_counter = invalid_counter +1
                    if invalid_counter <3:
                        continue
                    else:
                        print("Too may attempts. Logging out. Try again later!!")
                        exit()


        elif AccountType == 2:
            print('Minimum amount in this account must be 500 RM')
            InitialAmt = int()
            invalid_counter = 1
            while InitialAmt < 500:
                try:
                    InitialAmt = int(input('Enter the amount you would like to start off with:'))
                    if InitialAmt < 500:
                        print('Amount is too less to open a bank account, minimum amount in a saving account is 500 RM,')
                        invalid_counter = invalid_counter + 1
                except:
                    print("Invalid number entered.")
                    invalid_counter = invalid_counter + 1
                    if invalid_counter < 4:
                        continue
                    else:
                        print("Too may attempts. Logging out. Try again later!!")
                        exit()

        CustomerNameF = input('Enter your first name: ')
        CustomerNameL = input('Enter your last name: ')

        CustomerMobileNo = int()
        invalid_counter = 1
        while len(str(CustomerMobileNo)) != 9:
            try:
                CustomerMobileNo = int(input('Enter your mobile number of 10 digits:'))
                if len(str(CustomerMobileNo)) != 9:
                    print('Invalid Number. Mobile Number  should be of 10 digits:')
                    invalid_counter = invalid_counter + 1
            except:
                print('Invalid Entry. Mobile Number should have only digits')
                invalid_counter = invalid_counter + 1
                if invalid_counter < 4:
                    continue
                else:
                    print("Too may attempts. Logging out. Try again later!!")
                    exit()


        CustomerEmail = input('Enter your email: ')
        invalid_counter =1
        while not re.fullmatch(regex, CustomerEmail):
            invalid_counter = invalid_counter +1
            print("Enter valid email address")
            CustomerEmail = input('Enter your email: ')
            if invalid_counter>2:
                print("Too many attempts. Logging out. Try again later!!")
                exit()
        print("Check approval status for login details to your account after a few days")




        file = open('approval_needed.txt', 'a+')
        file.write('============================================================' + '\n')
        file.write('First Time Customer: Yes' + '\n')
        file.write('Customer ID: ' + str(CustomerID) + '\n')
        file.write('Customer First Name: ' + str(CustomerNameF) + '\n')
        file.write('Customer Last Name: ' + str(CustomerNameL) + '\n')
        file.write('Customer Mobile Number: ' + str(CustomerMobileNo) + '\n')
        file.write('Customer Email: ' + str(CustomerEmail) + '\n')
        if AccountType == 1:
            AccountType = 'savings'
        else:
            AccountType = 'current'
        file.write('Customer Account Type:' + str(AccountType) + '\n')
        file.write('Account Initial Balance:' + str(InitialAmt) + '\n')
        file.write('Approval Status: Pending' + '\n')
        file.write('Account number: To be assigned \n')
        file.write('Account Password: To be assigned \n')
        file.write('============================================================' + '\n')

    # if it is an existing customer
    elif first_time_cust == 'n':
        # validate the existing customer in customer.txt file
        valid_customer = False
        cust_file_reading = ""
        try:
            cust_file_reading = open('customer.txt', 'r')
        except Exception as error:
            print("Customer File Not Found")
            exit()
        all_lines = cust_file_reading.readlines()
        for ind in range(0, len(all_lines)):
            if all_lines[ind].startswith('Customer ID:'):
                cust_line_in_file = all_lines[ind].split(":")
                cust_id_in_file = int(cust_line_in_file[1].strip())
                if CustomerID == cust_id_in_file:
                    valid_customer = True
        if valid_customer == False:
            print("Customer records not found.")
            print('You will be returned to home screen in 10 secs')
            print('============================================================')
            exit()

        AccountType = ""
        invalid_counter = 1
        while AccountType not in [1, 2]:
            try:
                print("Enter only the given choices")
                AccountType = int(input("what is the type of account you'd like to create: 1.)Savings 2.)Current"))
            except ValueError as ve:
                print("Enter a numeric value")
            invalid_counter = invalid_counter + 1
            if invalid_counter == 4:
                print("Too many attempts. Logging out. Try again")
                exit()

        if AccountType == 1:
            print('Minimum amount in this account must be 100 RM')
            InitialAmt = int(input('Enter the amount you would like to start off with:'))
            InitialAmt = int()
            invalid_counter = 1
            while InitialAmt < 100:
                try:
                    InitialAmt = int(input('Enter the amount you would like to start off with:'))
                    if InitialAmt < 100:
                        print(
                            'Amount is too less to open a bank account, minimum amount in a saving account is 100 RM,')
                        invalid_counter = invalid_counter + 1
                except:
                    print("Invalid number entered.")
                    invalid_counter = invalid_counter + 1
                    if invalid_counter < 4:
                        continue
                    else:
                        print("Too may attempts. Logging out. Try again later!!")
                        exit()

        elif AccountType == 2:
            print('Minimum amount in this account must be 500 RM')
            InitialAmt = int()
            invalid_counter = 1
            while InitialAmt < 500:
                try:
                    InitialAmt = int(input('Enter the amount you would like to start off with:'))
                    if InitialAmt < 500:
                        print(
                            'Amount is too less to open a bank account, minimum amount in a saving account is 500 RM,')
                        invalid_counter = invalid_counter + 1
                        if invalid_counter < 4:
                            continue
                        else:
                            print("Too may attempts. Logging out. Try again later!!")
                            exit()
                except:
                    print("Invalid number entered.")
                    invalid_counter = invalid_counter + 1
                    if invalid_counter < 4:
                        continue
                    else:
                        print("Too may attempts. Logging out. Try again later!!")
                        exit()


        # saving account details for the existing customer
        file = open('approval_needed.txt', 'a+')
        file.write('============================================================' + '\n')
        file.write('First Time Customer: No' + '\n')
        file.write('Customer ID: ' + str(CustomerID) + '\n')
        if AccountType == 1:
            AccountType = 'savings'
        else:
            AccountType = 'current'
        file.write('Customer Account Type:' + AccountType + '\n')
        file.write('Account Initial Balance:' + str(InitialAmt) + '\n')
        file.write('Approval Status: Pending\n')
        file.write('Account number: To be assigned\n')
        file.write('Account Password: To be assigned\n')
        file.write('============================================================' + '\n')
        print('You will be returned to home screen in 10 secs')
        print('============================================================')
        exit()


#ADMIN ONLY FUNCTIONLAITY
def changeDetails():

    CustomerID = int(input("Enter the CustomerID to change details: "))
    CustomerFile=""
    try:
        CustomerFile = open('customer.txt', 'r')
    except Exception as error:
        print("Customer File Not Found")
        exit()
    #print("Hellooo",CustomerFile)
    ContentsFileList = CustomerFile.readlines()
    CustomerExists='no'
    for ind in range(0, len(ContentsFileList)):
        SingleLine = ContentsFileList[ind]
        if SingleLine.startswith('Customer ID: '):
            SingleLineValues = SingleLine.split(":")
            CustomerIDOfFile = int(SingleLineValues[1].strip())
            if CustomerIDOfFile == CustomerID:
                CustomerExists = 'yes'
                CustomerMobileNo = ContentsFileList[ind+3]
                CustomerEmail = ContentsFileList[ind+4]

                ToBeChanged=""
                invalid_option_cnt=1
                while type(ToBeChanged)!=int or ToBeChanged not in [1,2]:
                    try:
                        print('What would u like to change?')
                        print('1.)' + CustomerMobileNo)
                        ToBeChanged = int(input('2.)'+CustomerEmail))
                    except:
                        invalid_option_cnt =invalid_option_cnt+1
                        print("Invalid entry. Please enter the corresponding number of your choice")
                        if invalid_option_cnt>3:
                            print("Too many attempts. Logging out. Try again later!!")
                            exit()
                        else:
                            continue
                if ToBeChanged == 1:
                    NewMobileNumber = int()
                    invalid_counter = 1
                    while len(str(NewMobileNumber)) != 10:
                        try:
                            NewMobileNumber = int(input('Enter your mobile number of 10 digits:'))
                            if len(str(NewMobileNumber)) != 10:
                                print('Invalid Number. Mobile Number  should be of 10 digits:')
                                invalid_counter = invalid_counter + 1
                        except:
                            print('Invalid Entry. Mobile Number should have only digits')
                            invalid_counter = invalid_counter + 1
                            if invalid_counter < 4:
                                continue
                            else:
                                print("Too may attempts. Logging out. Try again later!!")
                                exit()
                    ContentsFileList[ind + 3] = "Customer Mobile Number:" + str(NewMobileNumber) + "\n"
                    print("Mobile number changed successfully, new mobile number is: ", NewMobileNumber)
                    print('Thank you')

                elif ToBeChanged == 2:
                    NewCustomerEmail = input('Enter new email for the customer: ')
                    invalid_counter = 1
                    while not re.fullmatch(regex, NewCustomerEmail):
                        invalid_counter = invalid_counter + 1
                        print("Enter valid email address")
                        NewCustomerEmail = input('Enter new email for the customer: ')
                        if invalid_counter > 2:
                            print("Too many attempts. Logging out. Try again later!!")
                            exit()
                    ContentsFileList[ind + 4] = "Customer Email:" + str(NewCustomerEmail) + "\n"
                    print("Email changed successfully, new email is: ", NewCustomerEmail)
                    print("Thank you")

    if CustomerExists=="no":
        print("Invalid Customer ID entered")

    cust_file = open('customer.txt', 'w')
    cust_file.writelines(ContentsFileList)


def withdraw():
    withdrawal_success = False
    acc_num = int(input("Enter Account Number you would like to withdraw from"))
    acc_file=""
    try:
        acc_file = open('accounts.txt', 'r')
    except Exception as error:
        print("Accounts File Not Found")
        exit()
    contents_file_list = acc_file.readlines()

    account_exists= 'no'

    for ind in range(0, len(contents_file_list)):
        single_line = contents_file_list[ind]
        if single_line.startswith('Account no:'):
            single_line_values = single_line.split(":")
            acc_num_in_file = int(single_line_values[1].strip())
            if acc_num_in_file == acc_num:
                account_exists='yes'
                # checking account type
                acc_type_line = contents_file_list[ind + 3]
                acc_type_line_vals = acc_type_line.split(":")
                acc_type_in_file = acc_type_line_vals[1].strip()

                acc_balance_line = contents_file_list[ind + 5]
                acc_balance_line_vals = acc_balance_line.split(":")
                acc_balance_in_file = float(acc_balance_line_vals[1].strip())



                print("Your account balance is:", acc_balance_in_file)



                rem_bal=0

                #only one wrong amt can be entered before the process ends
                if acc_type_in_file == 'savings':
                    print("Min balance for savings account must be 100")

                    max_withamt_possible = acc_balance_in_file - 100
                    print("Max amount that can be withdrawn", max_withamt_possible)

                    # asking user to enter withdrawal amount
                    withdramt = float()
                    invalid_counter = 1
                    while withdramt <= 0:
                        try:
                            withdramt = float(input('Enter the amount you would like to withdraw:'))
                            if withdramt <= 0:
                                print('Please enter a positive number')
                                invalid_counter = invalid_counter + 1
                                if invalid_counter < 4:
                                    continue
                                else:
                                    print("Too may attempts. Logging out. Try again later!!")
                                    exit()
                        except:
                            print("Invalid number entered.")
                            invalid_counter = invalid_counter + 1
                            if invalid_counter < 4:
                                continue
                            else:
                                print("Too may attempts. Logging out. Try again later!!")
                                exit()

                    rem_bal = acc_balance_in_file - withdramt
                    if rem_bal < 100:
                        print("Min balance should be 100 in savings account. Cannot withdraw.")
                    else:
                        contents_file_list[ind + 5] = "AccountBalance:" + str(rem_bal) +"\n"
                        print("Successfully withdrawn: Current balance is", rem_bal)
                        withdrawal_success =True
                        # add this thing to the transaction text file
                        # add_transaction('withdrawal')


                if acc_type_in_file == 'current':
                    print("Min balance for current account must be 500")

                    max_withamt_possible = acc_balance_in_file - 500
                    print("Max amount that can be withdrawn", max_withamt_possible)

                    # asking user to enter withdrawal amount
                    withdramt = float()
                    invalid_counter = 1
                    while withdramt <= 0:
                        InitialAmt = int()
                        try:
                            withdramt = float(input('Enter the amount you would like to withdraw:'))
                            if InitialAmt <= 0:
                                print('Please enter a positive number')
                                invalid_counter = invalid_counter + 1
                                if invalid_counter < 4:
                                    continue
                                else:
                                    print("Too may attempts. Logging out. Try again later!!")
                                    exit()
                        except:
                            print("Invalid number entered.")
                            invalid_counter = invalid_counter + 1
                            if invalid_counter < 4:
                                continue
                            else:
                                print("Too may attempts. Logging out. Try again later!!")
                                exit()

                    rem_bal = acc_balance_in_file - withdramt
                    if rem_bal < 500:
                        print("Min balance should be 500 in current account. Cannot withdraw.")
                    else:
                        contents_file_list[ind + 5] = "AccountBalance:" + str(rem_bal) +"\n"
                        print("Successfully withdrawn: Current balance is", rem_bal)
                        withdrawal_success =True
                        # add this thing to the transaction text file
                        # add_transaction('withdrawal')


                # getting details of the customer and account to save the transaction
                #acc_num
                cust_id_line = contents_file_list[ind+1]
                cust_id_line_details=cust_id_line.split(":")
                cust_id = cust_id_line_details[1].strip()
                #acc_type_in_file
                #acc_balance_in_file
                #rem_bal

                if withdrawal_success :
                    add_transaction(datetime.datetime.now() , 'withdrawal' , acc_num, cust_id, acc_type_in_file,  acc_balance_in_file, withdramt, rem_bal)

                break

    if account_exists=='no':
        print('Invalid account number entered')

    # writing in the file
    acc_file = open('accounts.txt', 'w')
    acc_file.writelines(contents_file_list)


def deposit():
    acc_num = int(input("Enter Account Number you would like to deposit to:"))
    acc_file=""
    try:
        acc_file = open('accounts.txt', 'r')
    except Exception as error:
        print("Accounts File Not Found")
        exit()

    contents_file_list = acc_file.readlines()

    account_exists= 'no'

    depositamt = 0
    new_bal = 0

    for ind in range(0, len(contents_file_list)):
        single_line = contents_file_list[ind]
        if single_line.startswith('Account no:'):
            single_line_values = single_line.split(":")
            acc_num_in_file = int(single_line_values[1].strip())
            if acc_num_in_file == acc_num:
                account_exists= 'yes'
                acc_balance_line = contents_file_list[ind + 5]
                acc_balance_line_vals = acc_balance_line.split(":")
                acc_balance_in_file = float(acc_balance_line_vals[1].strip())




                # asking user to enter withdrawal amount
                depositamt = float()
                invalid_counter = 1
                while depositamt <= 0:
                    try:
                        depositamt = float(input('Enter the amount you would like to deposit:'))
                        if depositamt <= 0:
                            print('Please enter a positive number')
                            invalid_counter = invalid_counter + 1
                            if invalid_counter < 4:
                                continue
                            else:
                                print("Too may attempts. Logging out. Try again later!!")
                                exit()
                    except:
                        print("Invalid number entered.")
                        invalid_counter = invalid_counter + 1
                        if invalid_counter < 4:
                            continue
                        else:
                            print("Too may attempts. Logging out. Try again later!!")
                            exit()

                new_bal = acc_balance_in_file + depositamt
                contents_file_list[ind + 5] = "AccountBalance:" + str(new_bal) + "\n"
                print("Successfully deposited: Current balance is", new_bal)

                # getting details of the customer and account to save the transaction
                # acc_num
                cust_id_line = contents_file_list[ind + 1]
                cust_id_line_details = cust_id_line.split(":")
                cust_id = cust_id_line_details[1].strip()
                # acc_type_in_file
                acc_type_line = contents_file_list[ind + 3]
                acc_type_details = acc_type_line.split(":")
                acc_type_in_file = acc_type_details[1].strip()
                # acc_balance_in_file
                # rem_bal

                add_transaction(datetime.datetime.now(), 'deposit', acc_num, cust_id, acc_type_in_file,
                                acc_balance_in_file, depositamt, new_bal)

                break


    if account_exists=='no':
        print('Invalid account number entered')


    acc_file = open('accounts.txt', 'w')
    acc_file.writelines(contents_file_list)


def changepass():
    acc_num = int(input("Enter the account number to change password: "))
    acc_file=""
    try:
        acc_file = open('accounts.txt', 'r')
    except Exception as error:
        print("Accounts File Not Found")
        exit()
    contents_file_list = acc_file.readlines()

    account_exists = 'no'

    for ind in range(0, len(contents_file_list)):
        single_line = contents_file_list[ind]
        if single_line.startswith('Account no:'):
            single_line_values = single_line.split(":")
            acc_num_in_file = int(single_line_values[1].strip())
            if acc_num_in_file == acc_num:
                account_exists= 'yes'
                acc_pass_line = contents_file_list[ind + 2]
                acc_password_line_vals = acc_pass_line.split(":")
                acc_password_in_file = acc_password_line_vals[1].strip()
                attempts_remaining=3
                while attempts_remaining>0:

                    old_pass = input("Enter old password:")

                    if old_pass ==acc_password_in_file:
                        new_pass= input("Enter new password:")
                        contents_file_list[ind + 2] = "AccountPassword:" + str(new_pass) + "\n"
                        print("Password changed successfully, new password is: ", new_pass)
                        break
                    else:
                        print("Invalid old password entered. Cannot change password. "+str(attempts_remaining)+" attempts remaining")
                        attempts_remaining = attempts_remaining -1
                        exit()



    if account_exists=='no':
        print('Invalid account number entered')


    acc_file = open('accounts.txt', 'w')
    acc_file.writelines(contents_file_list)


def generateReport():
    # account num?
    # start date?
    # end date?
    acc_no = int(input("Enter the account number"))

    valid_date_entered = False
    invalid_counter = 1
    while not valid_date_entered:
        try:
            print("Enter dates in 24 hours Format YYYY-MM-DD HH:MM:SS")
            print("HH:MM:SS will be 00:00:00 if unentered")

            start = input("Enter transaction start time:")
            values_entered = start.split()
            # if YYYY-MM-DD is entered, list length will be 1
            if len(values_entered)==1:
                start = values_entered[0] +" 00:00:00"


            end = input("Enter transaction end time:")
            values_entered = end.split()
            # if YYYY-MM-DD is entered, list length will be 1
            if len(values_entered)==1:
                end = values_entered[0] +" 00:00:00"


            #start = "2021-12-04 19:30:00"
            #end = "2021-12-04 19:35:00"
            start_time = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            valid_date_entered = True
        except:
            print("Enter a valid date")
            invalid_counter = invalid_counter +1
            if invalid_counter >3:
                print("Too many attempts. Logging out. Try again!!")
                exit()

    trans_file = ""
    try:
        trans_file = open('transactions.txt', 'r')
    except Exception as error:
        print("Transaction File Not Found")
        exit()

    already_printed_details= False
    trans_no = 0
    contents_file_list = trans_file.readlines()
    total_deposits = 0
    total_withdrawls = 0
    for ind in range(0, len(contents_file_list)):
        if contents_file_list[ind].startswith("Account No"):

            accnt_line = contents_file_list[ind].split(":")
            accnt_num_in_file =int(accnt_line[1].strip())
            if accnt_num_in_file == acc_no:

                trans_time_line = contents_file_list[ind+1].split("=")
                date_of_transaction_in_file = trans_time_line[1].strip()
                date_time_obj_in_file = datetime.datetime.strptime(date_of_transaction_in_file, '%Y-%m-%d %H:%M:%S.%f')
                if date_time_obj_in_file >= start_time and date_time_obj_in_file <= end_time and not already_printed_details:
                    # printing some details only one time, end="" because each line in transaction file already ends with \n
                    print("=============Customer and Account Details =====================")
                    print(contents_file_list[ind], end="")
                    print(contents_file_list[ind + 3], end="")
                    print(contents_file_list[ind + 4], end="")
                    already_printed_details = True
                    print("=====================================================\n")

                    # printing details for every transaction, end="" because each line in transaction file already ends with \n
                    trans_no += 1
                    print("===============Transaction: "+ str(trans_no) + "======================")
                    print(contents_file_list[ind+1], end="")
                    print(contents_file_list[ind+2], end="")
                    print(contents_file_list[ind+5], end="")
                    print(contents_file_list[ind+6], end="")
                    print(contents_file_list[ind+7], end="")
                    print("=====================================================")


                    # logic to calculate total depost and total withdrawal in the given time range
                    type_line = contents_file_list[ind + 2].split(":")
                    transaction_type = type_line[1].strip()
                    if transaction_type == 'deposit':
                        trans_amt_line = contents_file_list[ind + 6].split(":")
                        transaction_amt = trans_amt_line[1].strip()
                        total_deposits = total_deposits + float(transaction_amt)
                    else:
                        trans_amt_line = contents_file_list[ind + 6].split(":")
                        transaction_amt = trans_amt_line[1].strip()
                        total_withdrawls = total_withdrawls + float(transaction_amt)







                elif date_time_obj_in_file >= start_time and date_time_obj_in_file <= end_time and already_printed_details:
                    # printing details for every transaction, end="" because each line in transaction file already ends with \n
                    trans_no += 1
                    print("===============Transaction: " + str(trans_no) + "======================")
                    print(contents_file_list[ind+1], end="")
                    print(contents_file_list[ind+2], end="")
                    print(contents_file_list[ind+5], end="")
                    print(contents_file_list[ind+6], end="")
                    print(contents_file_list[ind+7], end="")
                    print("=====================================================")


                    # logic to calculate total depost and total withdrawal in the given time range
                    type_line = contents_file_list[ind + 2].split(":")
                    transaction_type = type_line[1].strip()
                    if transaction_type == 'deposit':
                        trans_amt_line = contents_file_list[ind + 6].split(":")
                        transaction_amt = trans_amt_line[1].strip()
                        total_deposits = total_deposits + float(transaction_amt)

                    else:
                        trans_amt_line = contents_file_list[ind + 6].split(":")
                        transaction_amt = trans_amt_line[1].strip()
                        total_withdrawls = total_withdrawls + float(transaction_amt)



    if trans_no ==0:
        print("=== No transactions in the given time range ===")
    else:
        print("\n=============TOTAL WITHDRAWAL AND DEPOSIT FOR THIS ACCOUNT================")
        print("TOTAL WITHDRAWAL FOR THIS ACCOUNT: "+ str(total_withdrawls ))
        print("TOTAL DEPOSIT FOR THIS ACCOUNT: "+ str(total_deposits))
        print("=====================================================")



def checkApprovalStatus():
    cust_id_match = False
    # asking Customer to enter CustID
    givenCustomerID = int()
    valid_id = False
    invalid_counter = 1
    while not valid_id:
        try:
            givenCustomerID = int(input('please enter your Customer ID'))
            valid_id = True
        except:
            print("Invalid number entered.")
            invalid_counter = invalid_counter + 1
            if invalid_counter < 4:
                continue
            else:
                print("Too may attempts. Logging out. Try again later!!")
                exit()
    # opening the approval_needed.txt file
    aproval=""
    try:
        aproval = open('approval_needed.txt', 'r')
    except Exception as e:
        print("Approval Needed File Not Found")
        exit()
    # reading all lines from the file
    list_of_lines = aproval.readlines()
    # checking each line if it is CustomerID:4567 line
    for ind in range(0, len(list_of_lines)):
        if list_of_lines[ind].startswith('Customer ID:'):
            # splitting the line on :
            values = list_of_lines[ind].split(':')  # values will be a list of ['CustomerID', '4567']
            # values[1] will be 4567. removing leading and trailing white spaces
            customerID = int(values[1].strip())
            # comparing customerID from approval file with givenCustomerID entered by user
            if customerID == givenCustomerID:
                cust_id_match = True
                line_before_cust_id  = list_of_lines[ind-1]
                first_time_list_list = line_before_cust_id.split(":")
                first_time_customer = first_time_list_list[1].strip()
                if first_time_customer == 'No':
                    print(list_of_lines[ind +3], end="")
                    status_list = list_of_lines[ind +3].split(":")
                    status = status_list[1].strip()
                    if status == 'Approved':
                        print("You may login with the following details")
                        print(list_of_lines[ind + 4], end="")
                        print(list_of_lines[ind + 5], end="")
                        print("====================================")
                elif first_time_customer == 'Yes':
                    print(list_of_lines[ind+7], end="")
                    status_list = list_of_lines[ind + 7].split(":")
                    status = status_list[1].strip()
                    if status == 'Approved':
                        print("You may login with the following details")
                        print(list_of_lines[ind + 8], end="")
                        print(list_of_lines[ind + 9], end="")
                        print("====================================")

    # invalid cusotmer id entered
    if cust_id_match == False:
        print("Invalid Customer ID entered. Try again!!")


def add_transaction(time, type_of_trans, acc_num, cust_id, acc_type, prev_bal, trans_amt, new_bal):
    trans_file = open('transactions.txt', 'a+')
    trans_file.write("======================================================\n")
    trans_file.write("Account No:" + str(acc_num) + "\n")
    trans_file.write("Time of transaction ="+str(time)+"\n")
    trans_file.write("Type of transaction:"+str(type_of_trans)+"\n")
    trans_file.write("Customer ID:"+str(cust_id)+"\n")
    trans_file.write("Account Type:"+str(acc_type)+"\n")
    trans_file.write("Previous Balance:"+str(prev_bal)+"\n")
    trans_file.write("Transaction Amount:"+str(trans_amt)+"\n")
    trans_file.write("New Balance:"+str(new_bal)+"\n")
    trans_file.write("======================================================\n")


def main():
    WelcomePage()
    choice=""
    try:
        choice = int(input('Please enter the number corresponding to your choice:'))
    except Exception as error:
        print("Please enter a valid numeric value only")
    n = 1
    while choice not in [1,2,3]:
        print('============================================================')
        print('Invalid option chosen')
        print('1.)Login to your bank account', '2.)Create a new bank account', '3.)Check approval status', sep="\n")
        try:
            choice = int(input('Please enter the number corresponding to your choice:'))
        except Exception as error:
            print("Please enter a valid numeric values only")
            n = n + 1
            if n > 2:
                print('Invalid option chosen too many times, process will be terminated.')
                print('============================================================')
                exit()

    if choice == 1:
        print('1.)Super Admin Login', '2.)Admin Login', '3.) Customer login', sep='\n')
        who_logs_in = ""
        try:
            who_logs_in = int(input('Please enter the number corresponding to your choice:'))
        except Exception as error:
            print("Please enter a valid numeric values only")

        n = 1
        while who_logs_in not in [1, 2] and n < 4:
            print('============================================================')
            print('Invalid option chosen')
            print('Enter your choice')
            print('1.)Super Admin login', '2.)Admin Login', '3.)Customer Login', sep='\n')
            try:
                who_logs_in = int(input('Please enter the number corresponding to your choice:'))
            except Exception as error:
                print("Please enter a valid numeric values only")
                n = n + 1
                if n >= 4:
                    print('Invalid option chosen too many times, process will be terminated. You can try again!!')
                    print('============================================================')
                    exit()

        if who_logs_in == 1:
            valid_superAdmin = validateSuperAdminLogin()
            if valid_superAdmin == True:
                admin_option = int()
                invalid_counter = 0
                while admin_option not in [1, 2, 3]:
                    invalid_counter = invalid_counter + 1
                    try:
                        # admin menu
                        print('What would you like do today:')
                        print('1.)Approve Customer', '2.)Change Customer Details', '3.)Generate Report','4.)Make admin account', sep='\n')
                        admin_option = int(input('Please enter the number corresponding to your choice:'))
                    except:
                        print("Please enter a valid choice")
                        invalid_counter = invalid_counter + 1
                        if invalid_counter <= 4:
                            continue
                        else:
                            print("Too many attempts. Logging out. Try again later!!")
                            exit()

                if admin_option == 1:
                    approveCustomer()
                if admin_option == 2:
                    changeDetails()
                if admin_option == 3:
                    generateReport()
                if admin_option == 4:
                    createAdminAccount()

        # asking for customer options
        elif who_logs_in == 2:
            valid_admin = validateAdminLogin()
            if valid_admin == True:
                admin_option = int()
                invalid_counter = 0
                while admin_option not in [1, 2, 3]:
                    invalid_counter = invalid_counter + 1
                    try:
                        # admin menu
                        print('What would you like do today:')
                        print('1.)Approve Customer', '2.)Change Customer Details', '3.)Generate Report', sep='\n')
                        admin_option = int(input('Please enter the number corresponding to your choice:'))
                    except:
                        print("Please enter a valid choice")
                        invalid_counter = invalid_counter + 1
                        if invalid_counter <= 4:
                            continue
                        else:
                            print("Too many attempts. Logging out. Try again later!!")
                            exit()

                if admin_option == 1:
                    approveCustomer()
                if admin_option == 2:
                    changeDetails()
                if admin_option == 3:
                    generateReport()
            elif valid_admin == False:
                print("Invalid Admin credentials entered. Please try again!!")
                exit()
        elif who_logs_in == 3:
            valid_customer = validateCustomerLogin()
            if valid_customer == True:
                customer_option = int()
                invalid_counter = 0
                while customer_option not in [1, 2, 3, 4]:
                    invalid_counter = invalid_counter + 1
                    try:
                        print('What would you like do today:')
                        print('1.)Withdraw amount', '2.)Deposit', '3.)Change Password', '4.)Generate Report', sep='\n')
                        customer_option = int(input('Please enter the number corresponding to your choice:'))
                    except:
                        print("Please enter a valid choice")
                        invalid_counter = invalid_counter + 1
                        if invalid_counter <= 4:
                            continue
                        else:
                            print("Too many attempts. Logging out. Try again later!!")
                            exit()
                if customer_option == 1:
                    withdraw()
                if customer_option == 2:
                    deposit()
                if customer_option == 3:
                    changepass()
                if customer_option == 4:
                    generateReport()
            else:
                print("Inavlid Customer credentials entered. Please try again!!")
                exit()
    elif choice == 2:
        NewAccount()
        exit()
    elif choice == 3:
        checkApprovalStatus()

main()

