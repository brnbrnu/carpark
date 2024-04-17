

from datetime import datetime
import uuid


register = {}
max_capacity = 10 
   
# otopark boş mu
def  is_empty():
    count_register = len(register)
    if count_register < max_capacity:
        empty_park = max_capacity - count_register
        print(f"The parking lot is not full. There are {empty_park} empty spaces available.")
        return True
    
    else:
        print("The parking lot is full.")
        return False

def control(lic_plate, name, surname):
    try:
        if len(lic_plate) != 7 or not lic_plate.isalnum():
            raise ValueError("License plate number must be 7 alphanumeric characters")
        if not name.isalpha() or not surname.isalpha():
            raise ValueError("Name and surname must contain only alphabetic characters")
        
        return True
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return False
         

def  park_your_car():
    if is_empty() :
        lic_plate = input("License Plate Number (7 digits) : ")
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        if control(lic_plate,name,surname):
            time_in = datetime.now().strftime("%H:%M:%S")
            ticket_id = uuid.uuid4()
    

        data = {"ticketid":ticket_id,lic_plate: {"Name": name,"Surname":surname, "Time In": time_in}}
        register.update(data)
        print(register)
        print(f"\nYour ticket has been registered.\nLicense Plate:{lic_plate}\nOwner Name:{name} {surname}\nTime in:{time_in}")
    

def remove_your_car():
    license_plate = input("Enter License Plate Number: ")
    if license_plate in register:
        time_in = register[license_plate]["Time In"]
        del register[license_plate]
        print(f"{license_plate}'s car has been removed.")
        cost = calculate_paid(time_in)  # Pass the time_in value to calculate the parking fee
        print(f"Total parking fee: ${cost:.2f}")
    else:
        print("No registration found for this license plate number.")
        

def calculate_paid(time_in, price_per_hour=5):
    time_diff = datetime.now() - datetime.strptime(time_in, "%H:%M:%S")
    cost = time_diff.seconds / 3600 * price_per_hour
    return cost

     
if __name__=="__main__":
    
    
    while True:
        print("\tCAR PARK SYSTEM")
        print("\t---------------------------")
        
        print("Welcome to carpark\n1- for entry\n2- for exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            park_your_car()
        elif choice == 2:
            remove_your_car()
        else:
            print("Invalid Choice! Please enter a valid option.")
    
    








