valid_pin=303030
current_account_bal=400000
name=input("Please enter your name")
pin=int(input("Please enter account pin."))
def atm():
    if pin==valid_pin:
        amount=int(input("How much are you withdrawing?"))
    else :
        print("Your pin is incorrect.")
    if amount < current_account_bal:
            new_bal=current_account_bal-amount
            print(name,",", amount,"has been withdrawn from your account.")
            print("Balance is:",new_bal)
    else :
        print("Your account Balance is insufficient.")
        return amount
atm()