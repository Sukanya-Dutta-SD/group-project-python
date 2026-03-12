import csv

# Add Tourist
def add_tourist():
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
            print("\nID | Name | Phone | Email | City | Aadhar")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No tourist records found.")


# Search Tourist
def search_tourist():
    tid = input("Enter Tourist ID: ")

    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == tid:
                    print("Tourist Found:", row)
                    return
        print("Tourist Not Found")
    except FileNotFoundError:
        print("File not found.")


# Show Packages
def show_packages():
    print("\nAvailable Packages\n")

    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Packages file not found.")


# Book Package
def book_package():
    booking_id = input("Enter Booking ID: ")
    tourist_id = input("Enter Tourist ID: ")

    show_packages()

    package_id = input("Enter Package ID: ")
    date = input("Enter Travel Date: ")

    print("\nSelect Transport")
    print("1. Bus - 500")
    print("2. Train - 1000")
    print("3. Flight - 5000")

    choice = int(input("Enter transport number: "))

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
        print("Invalid choice")
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
            print("\nBookingID | TouristID | PackageID | Date | Transport | Price")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No bookings found.")


# Generate Bill
def generate_bill():
    pid = input("Enter Package ID: ")

    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == pid:
                    print("\n----- BILL -----")
                    print("Place:", row[1])
                    print("Days:", row[2])
                    print("Package Amount:", row[3])
                    return
        print("Package not found.")
    except FileNotFoundError:
        print("Packages file not found.")


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
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice")