

''''''



import math
from datetime import datetime

def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_tire_volume(w, a, d):
    pi = math.pi
    v = (pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
    return round(v)

price = 0

def get_tire_price(w, a, d):
    global price  # Declare 'price' as a global variable to modify it
    if w == 195 and a == 65 and d == 15:
        price = 27500.00
    elif w == 265 and a == 65 and d == 17:
        price = 150500.00
    elif w == 225 and a == 70 and d == 16:
        price = 44800.00
    elif w == 205 and a == 65 and d == 15:
        price = 32000.00
    else:
        price = 0  # Set a default price if dimensions are not found
    return price  # Return the calculated price

def save_user_data():
    w = get_user_input("Enter the tire width in millimeters: ")
    a = get_user_input("Enter the aspect ratio of the tire: ")
    d = get_user_input("Enter the wheel diameter in inches: ")

    v = calculate_tire_volume(w, a, d)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info = f"============================\nDate appended: {current_date}\nTire width in MM: {w}\nAspect Ratio of the tire: {a}\nDiameter of the wheel: {d}\n\nThe value of V = {v:.2f}\n"

    file_name = 'volumes.txt'
    with open(file_name, 'at', encoding='utf-8') as database:
        print(info, file=database)

    print(f"Date appended:{current_date}\nTire volume: {v:.2f} liters")
    tire_price = get_tire_price(w, a, d)

    if tire_price != 0:
        print(f"Tire Price: ₦{tire_price:.2f}")
        q = input("Would you like to purchase a tire of this size? (YES or NO): ")
        if q.lower() == 'yes':
            name = input("Please enter your name: ")
            phone_number = input("Please enter your phone number: ")
            with open(file_name, 'at', encoding='utf-8') as database:
                print(f"Name: {name}\nPhone Number: {phone_number}\n==============================", file=database)
            print(f"Thank you, {name}! Your phone number ({phone_number}) has been saved.\nThe price for that size is ₦{tire_price:.2f}")
    else:
        print("Tire price not found for the entered dimensions.")

if __name__ == "__main__":
    save_user_data()

