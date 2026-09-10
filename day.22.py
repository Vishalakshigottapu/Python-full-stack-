'''
vishala_details_ICIC ={
    "Name": "vishala",
    'Adr': ' 12345678',
    'pan': 'gn12374978w',
    'ATMPIN': '2909',
    'Balance': 10000
}
All_attmps = 3
while All_attmps > 0:
    user_pin =input('enter a  your atm pin:')
    if user_pin in vishala_details_ICIC['ATMPIN']:
        print('WELCOME ICIC ATM')
        choice_ = int(input('enter \n1.Withdraw \n2.Deposite:'))
        if choice_ == 1:
            with_m = int(input('enter amount to Withdraw:'))
            if with_m <= vishala_details_ICIC['Balance'] and with_m % 100 ==0:
                vishala_details_ICIC['Balance'] -= with_m
                print(f'Take your cash the balance is {vishala_details_ICIC ["Balance"]}')
            else:
                print('insufficient balance or This ATM can not provide change')
        elif choice_ == 2:
            depo_m = int(input('enter amount to deposite:'))
            if depo_m % 100 ==0:
                vishala_details_ICIC['Balance'] += depo_m
                print(f'amount to deposit and total amount in your Balance is {vishala_details_ICIC ["Balance"]}')
            else:
                print('This ATM is not accepts change')
        break
    else:
        All_attmps -=1
        if All_attmps > 0:
            print(f'Incorrect pin entered and you have {All_attmps} left')
        else:
            print('Your card is blocked')
            
'''
vishala_details_ICIC = {
    "Name": "vishala",
    "Adr": "12345678",
    "pan": "gn12374978w",
    "ATMPIN": "2909",
    "Balance": 10000,
    "Mini state": []
}

All_attmps = 3

while All_attmps > 0:
    user_pin = input("Enter your 4 digit ATM PIN: ")

    if len(user_pin) == 4:

        if user_pin == vishala_details_ICIC["ATMPIN"]:
            print("WELCOME ICIC ATM")

            choice_ = int(input("Enter \n1. Withdraw \n2. Deposit \n3. Check Balance: "))

            if choice_ == 1:
                with_m = int(input("Enter amount to Withdraw: "))

                if with_m <= vishala_details_ICIC["Balance"] and with_m % 100 == 0:
                    vishala_details_ICIC["Balance"] -= with_m
                    print(f"Take your cash. The balance is {vishala_details_ICIC['Balance']}")
                    vishala_details_ICIC['Mini state'].append(f'Withdraw: {with_m}')
                    print(f'{vishala_details_ICIC['Mini state']}')
                    user_opt =  int(input('enter \n1.Home page \n2. Exit:'))
                    if user_opt == 1:
                        print('Taking to home page')
                    elif user_opt == 2:
                        print('Thanks for visiting')
                        break
                else:
                    print("Insufficient balance or this ATM cannot provide change")

            elif choice_ == 2:
                depo_m = int(input("Enter amount to Deposit: "))

                if depo_m % 100 == 0:
                    vishala_details_ICIC["Balance"] += depo_m
                    print(f"Amount deposited. Total balance is {vishala_details_ICIC['Balance']}")
                    vishala_details_ICIC['Mini state'].append(f'Deposite:{depo_m}')
                    print(f'{vishala_details_ICIC['Mini state']}')
                    user_opt =  int(input('enter \n1.Home page \n2. Exit:'))
                    if user_opt == 1:
                        print('Taking to home page')
                    elif user_opt == 2:
                        print('Thanks for visiting')
                        break
                    
                else:
                    print("This ATM does not accept change")
            elif choice_ == 3:
                print(f'your Balance is {vishala_details_ICIC['Balance']}')

            break

        else:
            All_attmps -= 1

            if All_attmps > 0:
                print(f"Incorrect PIN entered. You have {All_attmps} attempts left")
            else:
                print("Your card is blocked")

    else:
        print("PIN must contain exactly 4 digits")
