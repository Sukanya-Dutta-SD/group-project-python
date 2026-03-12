import csv

# Add Tourist
def add_tourist() -> None:
    tid = input("Enter Tourist ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")
    aadhar = input("Enter Aadhar No: ")

    with open("tourists.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tid, name, phone, email, city, aadhar])

    print("Tourist Added Successfully")


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
    with open("tourists.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == tid:
                print("Tourist Found:", row)
                found = True
                break

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
    booking_id = input("Enter Booking ID: ")
    tourist_id = input("Enter Tourist ID: ")

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
        writer.writerow([booking_id, tourist_id, package_id, date, transport, price])

    print("Package Booked Successfully")


# View Bookings
def view_bookings():
    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print("No Booking Records Found")


# Generate Bill
def generate_bill():
    pid = input("Enter Package ID: ")

    package_price = 0
    place = ""
    days = ""

    with open("packages.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == pid:
                place = row[1]
                days = row[2]
                package_price = int(row[3])
                break

    with open("bookings.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == pid:
                transport = row[4]
                transport_price = int(row[5])

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