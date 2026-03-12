import csv
from email.charset import add_charset


# Add Tourist
def add_tourist():
    id = input("Enter Tourist ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")
    addharNo = input("Enter AddHar No: ")

    with open("tourists.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id,name,phone,email,city,addharNo])

    print("Tourist Added Successfully")


# View Tourists
def view_tourists():
    with open("tourists.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Search Tourist
def search_tourist():
    tid = input("Enter Tourist ID: ")

    with open("tourists.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == tid:
                print("Tourist Found:",row)
                return
    print("Tourist Not Found")


# Show Packages
def show_packages():
    print("\nAvailable Packages\n")

    with open("packages.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Book Package
def book_package():
    booking_id = input("Enter Booking ID: ")
    tourist_id = input("Enter Tourist ID: ")

    show_packages()

    package_id = input("Enter Package ID: ")
    date = input("Enter Travel Date: ")

    with open("bookings.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([booking_id,tourist_id,package_id,date])

    print("Package Booked Successfully")


# View Bookings
def view_bookings():
    with open("bookings.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Generate Bill
def generate_bill():
    pid = input("Enter Package ID: ")

    with open("packages.csv","r") as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0] == pid:
                print("\n----- BILL -----")
                print("Place:",row[1])
                print("Days:",row[2])
                print("Amount:",row[3])
                return


# Main Menu
while True:
    print("\n--- Tourism Management System ---")
    print("1 Add Tourist")
    print("2 View Tourists")
    print("3 Search Tourist")
    print("4 Book Package")
    print("5 View Bookings")
    print("6 Generate Bill")
    print("7 Exit")

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