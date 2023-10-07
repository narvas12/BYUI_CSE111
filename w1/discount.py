from datetime import datetime

# get current datetime
dt = datetime.now()
print('Datetime is:', dt)

# get day of week as an integer


subtotal = input("Input the the subtotal to be paid: ")
subtotal = int(subtotal)
def discount():
    while subtotal > 0:
        x = dt.weekday()
        if x == 2 or x == 6:
            amount_to_complete = 50 - subtotal 
            if subtotal >= 50:
                
                discount = subtotal / 100 * 10
                print (f"You'll get a discount of 10% wich is {discount}:")
            else:
                print(f"The amount ain't enough to get you a discount today...\nyou'll need {amount_to_complete}$ to complete the amount eligible for a discount")
        else:
            print("It's not your lcky day today come back again ")

        break

total_discount = discount()

print(total_discount)