import hidden_stuff.hello as hello
import time
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Join that path with your folder and filename
DATEI = os.path.join(BASE_DIR, "hidden_stuff", "expenses.csv")

print("--- TOP TIER BUDGETING PROGRAM (the people love it) ---\n")

while True: # program loop
    hello.print_total_balance()
    time.sleep(0.4 * random.random())
    print("Show list of expenses: S")
    time.sleep(0.2 * random.random())
    print("Add an expense: A")
    time.sleep(0.1 * random.random())
    print("Delete an expense: D")
    time.sleep(0.1 * random.random())
    print("Modify balance: M" )
    print("View balance: V")
    time.sleep(0.1 * random.random())
    time.sleep(0.3 * random.random())
    print("Exit: E")
    action = input("\n")
    #EXIT
    if action.lower() == "exit" or action.lower() == 'e':
        time.sleep(0.7 * random.random())
        break
    #SHOW EXPENSES
    elif action.lower() == "show" or action.lower() == 's':
        print("---YOUR EXPENSES---(%s)---" % hello.get_amount_of_rows(DATEI))
        hello.print_list_of_things(DATEI)
        print("\nThese all together cost "+ str(round(hello.sum_of_total_prices(), 2)) +"€") if hello.get_amount_of_rows(DATEI) > 1 else 1
        print("---------\n")
    #DELETE EXPENSE
    elif action.lower() == 'd' or action.lower() == "delete" """ or action.lower() == 'l' or action.lower() == "löschen" """ :
        unwanted_item = input("What do you want to delete? (To delete every expense type 'all') ")
        hello.delete_row(unwanted_item)
    #ADD EXPENSE
    elif action.lower() == "a" or action.lower() == "add":
        expense = input("Cateegory (e.g. food, transport, uni): ")
        price = input("How much will that cost in €?: ")
        try:
            price = float(price)
            if hello.speichern(price, expense):
                print("Alright, it went through")
            
        except ValueError:
            print("Error: Input a number.")
    #VIEW BALANCE
    elif action.lower() == "vb" or action.lower() == "v":
        balance = hello.get_balance()
        print(f"You currently have {abs(round(balance, 2)) if round(balance, 2) == 0.0 else round(balance, 2)}€\n")
    #CHANGE BALANCE
    elif action.lower() == "m":
        balance = hello.get_balance()
        print(f"You currently have {abs(round(balance, 2)) if round(balance, 2) == 0.0 else round(balance, 2)}€\n")
        new_balance = input("Modify balance (e.g 200, -90.9, +19.99): ")
        if hello.is_float(new_balance):
            hello.add_balance(new_balance)
        else:
            print("Bro next time just input a number bro. I even gave your fatass examples..🙏😭")
    #FOR MORONS
    else:
        print("You've got to input one of the things I listed...")

print("Aight pack it up.")