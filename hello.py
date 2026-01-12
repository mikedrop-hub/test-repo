import csv
import os
import wikipediaapi as wiki

# Defining stuff yk the drill
DATEI = "expenses.csv"
BALANCE_FILE = "balance.csv"
EMPTY_ROW = ["", ""]


def is_float(input):
    try:
       float(input)
       return True
    except:
        return False 
    
def speichern(betrag, kategorie):
    # 'a' steht für 'append' (anhängen), damit alte Daten nicht gelöscht werden
    if search(DATEI, kategorie) == EMPTY_ROW:
        with open(DATEI, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([betrag, kategorie])
        return True
    else: 
        print(str(kategorie)+ " already exists. Saving cancelled.")
        return False


def get_amount_of_rows(file_input):
    amount_of_rows = 0
    with open(file_input) as file:
        for row in file:
            amount_of_rows += 1
    return amount_of_rows


def search(file, query) -> list[str]: # returns a row
    query = str(query)
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row.__contains__(query): #This searches for exact matches only
                #print("Found "+ str(query))
                return row    
        return EMPTY_ROW    
           

def get_price(item): #item is a row
    try:
        price = item[0]
        #print("The expense of " + item[1] + " is " + price + "€")
        return float(price)
    except IndexError:
        print("-> "+ str(item)+ " lowkey might not exist. Maybe check the spelling...")
        return float(price)
    
def get_expense(item): #item is a row
    try:
        expense = item[1]
        #print("The expense of " + item[1] + " is " + price + "€")
        return expense
    except IndexError:
        print("-> "+ str(item)+ " lowkey might not exist. Maybe check the spelling...")
        ""

def clear_file(file):
    with open(file, mode="w+"):
        pass

def check_if_sure(thing_that_is_boutta_be_done) -> bool:
    thing_that_is_boutta_be_done = str(thing_that_is_boutta_be_done)
    yes_or_no = input("Are you sure you want to "+ thing_that_is_boutta_be_done +"? (y or anything else) ")
    if yes_or_no.lower() == "y":
        print("")
        return True
    print("")
    return False

def get_balance() -> float:
    with open(BALANCE_FILE) as file:
        reader = csv.reader(file)
        balance = search(BALANCE_FILE, "Total balance")[1]
        #print(balance)
        if not(is_float(balance)):
            print("add_balance() says: The balance aint no number and this is probably problematic :(")
            return 0.0
        else: 
            return float(balance)
        
def add_balance(amount_to_be_added):
    balance = get_balance() 
    #print("Got balance: " + str(balance))
    new_balance = float(balance) + float(amount_to_be_added)

    clear_file(BALANCE_FILE)
    with open(BALANCE_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow(["Total balance", new_balance])
           
def get_row_by_index(file_input, target_row):
    with open(file_input) as file:
        reader = csv.reader(file)
        for (counter,row) in enumerate(reader):
            if counter == target_row:
                return row
           
def delete_row(item_to_be_deleted):
    new_file: list[list[str]]= []
    to_be_deleted_items: list[list[str]] = []
    counter_of_to_be_deleted_items = 0
    if item_to_be_deleted.lower() == "all":
        if check_if_sure("delete every expense"):
            clear_file(DATEI)
    else: 
        with open(DATEI, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row.__contains__(str(item_to_be_deleted)):
                    to_be_deleted_items.append(row)
                    counter_of_to_be_deleted_items += 1
                    continue
                else: 
                    new_file.append(row)
        if counter_of_to_be_deleted_items > 0:
            if check_if_sure("delete " + str(counter_of_to_be_deleted_items) + " thing(s)"):
                clear_file(DATEI)
                with open(DATEI, mode='a') as f:
                    writer = csv.writer(f)
                    for row in new_file:
                        writer.writerow(row)
        else:
            print(item_to_be_deleted +" might be a typo because I couldn't find it.")   

def clear_balance():
    clear_file(BALANCE_FILE)
    with open(BALANCE_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow(["Total balance", 0.0])

def get_total_money_left():
    return get_balance() - sum_of_total_prices()
    
def sum_of_total_prices():
    sum_of_total_prices = 0.0
    with open(DATEI) as file:
        reader = csv.reader(file)
        for row in reader:
            sum_of_total_prices = sum_of_total_prices + get_price(row)
    return sum_of_total_prices

def get_total_rounded_money_left():
    return round(get_total_money_left(), 2)

def print_total_balance():
    if get_total_money_left() < 0:
        print("You are "+ str(abs(get_total_rounded_money_left())) +"€ in debt. Get your funny up, brokie.")
    elif get_total_money_left() >= 0:
        print("You have "+str(get_total_rounded_money_left()) +"€ of spendable money.")

def print_list_of_things(file_input):
    with open(file_input) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[1] +" costs "+ row[0]+ "€")



#print(search(DATEI, "cookies"))
#print(search(DATEI, "a b c"))
