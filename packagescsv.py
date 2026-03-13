# Add Tourist
import csv
import os

def add_tourist():

    # Automatic Tourist ID (101,102,103...)
    tid = 101

    if os.path.exists("tourists.csv"):
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)

            ids = []

            for row in reader:
                if row:
                    try:
                        ids.append(int(row[0]))
                    except ValueError:
                        continue

            if ids:
                tid = max(ids) + 1

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")
    aadhar = input("Enter Aadhar No: ")

    with open("tourists.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tid, name, phone, email, city, aadhar])

    print("Tourist Added Successfully")
    print("Generated Tourist ID:", tid)
# View Tourists
def view_tourists():
    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print("No Tourist Records Found")


# Search Tourist
def search_tourist():
    tid = input("Enter Tourist ID: ")

    found = False
    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == tid:
                    print("Tourist Found:", row)
                    found = True
                    break
    except:
        print("File not found")

    if not found:
        print("Tourist Not Found")


# Show Packages
def show_packages():
    print("\nAvailable Packages\n")

    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print("Package File Not Found")


# Book Package
def book_package():

    # Automatic Booking ID (A01, A02, A03...)
    booking_id = "A01"

    if os.path.exists("bookings.csv"):
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)

            last_number = 0

            for row in reader:
                if row and row[0].startswith("A"):
                    try:
                        num = int(row[0][1:])
                        if num > last_number:
                            last_number = num
                    except:
                        pass

            booking_id = f"A{last_number + 1:02d}"

    tourist_id = input("Enter Tourist ID: ")
    tourist_name = input("Enter Tourist Name: ")

    show_packages()

    package_id = input("Enter Package ID: ")
    date = input("Enter Travel Date: ")

    print("\nTransport Type")
    print("1. Bus - 500")
    print("2. Train - 1000")
    print("3. Flight - 5000")

    choice = int(input("Enter Transport Number: "))

    if choice == 1:
        transport = "Bus"
        price = 500
    elif choice == 2:
        transport = "Train"
        price = 1000
    elif choice == 3:
        transport = "Flight"
        price = 5000
    else:
        print("Invalid Choice")
        return

    with open("bookings.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([booking_id, tourist_id, tourist_name, package_id, date, transport, price])

    print("Package Booked Successfully")
    print("Generated Booking ID:", booking_id)

    print("Package Booked Successfully")

# View Bookings
def view_bookings():
    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            print("\nbooking_id | tourist_id | tourist_name | package_id | date | transport | price")
            for row in reader:
                print(row)
    except:
        print("No Booking Records Found")


# Generate Bill

    print("Booking Not Found")
# def generate_bill():
#     pid = input("Enter Package ID: ")
# 
#     package_price = 0
#     place = ""
#     days = ""
# 
#     try:
#         with open("packages.csv", "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 if row[0] == pid:
#                     place = row[1]
#                     days = row[2]
#                     package_price = int(row[3])
#                     break
#     except:
#         print("Package file not found")
#         return
# 
#     try:
#         with open("bookings.csv", "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
# 
#                 if row[3] == pid:   # correct column for package_id
# 
#                     transport = row[5]
#                     transport_price = int(row[6])
# 
#                     total = package_price + transport_price
# 
#                     print("\n------ BILL ------")
#                     print("Package ID :", pid)
#                     print("Place :", place)
#                     print("Days :", days)
#                     print("Package Price :", package_price)
#                     print("Transport :", transport)
#                     print("Transport Price :", transport_price)
#                     print("Total Amount :", total)
#                     print("------------------")
#                     return
#     except:
#         print("Booking file not found")

def generate_bill():
    pid = input("Enter Package ID: ")

    package_price = 0
    place = ""
    days = ""

    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == pid:
                    place = row[1]
                    days = row[2]
                    package_price = int(row[4].replace(",",""))
                    break
    except:
        print("Package file not found")
        return

    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:

                if row[3] == pid:   # correct column for package_id

                    transport = row[5]
                    transport_price = int(row[6])

                    total = package_price + transport_price

                    print("\n------ BILL ------")
                    print("Package ID :", pid)
                    print("Place :", place)
                    print("Days :", days)
                    print("Package Price :", package_price)
                    print("Transport :", transport)
                    print("Transport Price :", transport_price)
                    print("Total Amount :", total)
                    print("------------------")
                    return
    except:
        print("Booking file not found")

    print("Booking Not Found")

# Main Menu
while True:
    print("\n--- Tourism Management System ---")
    print("1. Add Tourist")
    print("2. View Tourists")
    print("3. Search Tourist")
    print("4. Book Package")
    print("5. View Bookings")
    print("6. Generate Bill")
    print("7. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        add_tourist()

    elif ch == "2":
        view_tourists()

    elif ch == "3":
        search_tourist()

    elif ch == "4":
        book_package()

    elif ch == "5":
        view_bookings()

    elif ch == "6":
        generate_bill()

    elif ch == "7":
        print("Thank You for Visiting Our Site")
        break

    else:
        print("Invalid Choice")