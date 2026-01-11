import hello
import time

DATEI = "ausgaben.csv"

print("--- TOP TIER BUDGETING PROGRAM (the people love it) ---\n")

while True: # program loop
    hello.print_total_balance()
    time.sleep(0.4)
    print("Show list of expenses: S")
    time.sleep(0.2)
    print("Add an expense: A")
    time.sleep(0.1) 
    print("Delete an expense: D") 
    time.sleep(0.1) 
    print("Modify balance: M" )
    print("View balance: V")
    time.sleep(0.1) 
    time.sleep(0.3)
    print("Exit: E")
    action = input("\n")
    #EXIT
    if action.lower() == "exit" or action.lower() == 'e':
        time.sleep(0.7)
        break
    #SHOW EXPENSES
    elif action.lower() == "show" or action.lower() == 's':
        print("---YOUR EXPENSES---")
        hello.print_list_of_things(DATEI)
        print("\nThese all together cost "+ str(round(hello.sum_of_total_prices(), 2)) +"€\n")
        print("---------")
    #DELETE EXPENSE
    elif action.lower() == 'd' or action.lower() == "delete" """ or action.lower() == 'l' or action.lower() == "löschen" """ :
        unwanted_item = input("Was soll gelöscht werden? (To delete every expense type 'all') ")
        hello.delete_row(unwanted_item)
    #ADD EXPENSE
    elif action.lower() == "a" or action.lower() == "add":    
        expense = input("Kategorie (z.B. Essen, Fahrtkosten): ")
        price = input("How much will that cost in €?: ")
        try:
            price = float(price)
            if hello.speichern(price, expense):
                print("Alright,it went through")
            
        except ValueError:
            print("Fehler: Bitte eine Zahl eingeben.") 
    #VIEW BALANCE
    elif action.lower() == "vb" or action.lower() == "v":
        print("You have " + str(round(hello.get_balance(), 2)) +"€\n")  
    #CHANGE BALANCE
    elif action.lower() == "m":
        print("You currently have " + str(round(hello.get_balance(), 2)) +"€\n")  
        new_balance = input("Modify balance(e.g 200, -90.9, +19.99): ")
        if hello.is_float(new_balance):
            hello.add_balance(new_balance)
        else:
            print("Bro next time just input a number bro. I even gave your fatass examples..🙏😭")
    #FOR MORONS
    else:
        print("You've got to input one of the things I listed...")

print("Aight I'm done.")