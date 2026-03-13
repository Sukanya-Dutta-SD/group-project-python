# Add Tourist
import csv
import os
import pyttsx3


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
    speak("Tourist Added Successfully")
    print("Tourist Added Successfully")
    speak(f"Generated Tourist ID {tid}")
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

#speak

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 10.0)
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Fetch Tourist

def fetch_tourist(tid):
    found = False
    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == tid:

                    found = True
                    return row
                    # break

    except:
        print("File not found")

    if not found:
        print("Tourist Not Found")


# Fetch package

def fetch_package(tid):
    found = False
    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == tid:

                    found = True
                    return row
                    # break

    except:
        print("File not found")

    if not found:
        print("Package Not Found")



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

    # tourist_name = input("Enter Tourist Name: ")

    tourist_details = fetch_tourist(tourist_id)

    show_packages()

    package_id = input("Enter Package ID: ")
    package_details = fetch_package(package_id)
    date = input("Enter Travel Date: ")

    with open("bookings.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([booking_id, tourist_id, tourist_details[1], tourist_details[2], tourist_details[3], tourist_details[4], package_details[1], date, package_details[3], package_details[4]])

    speak("Package Booked Successfully")
    print("Package Booked Successfully")
    booking_text = "Generated Booking ID:", booking_id
    speak(booking_text)
    print("Generated Booking ID:", booking_id)


# View Bookings
def view_bookings():
    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            print("\nbooking_id | tourist_id | tourist_name | tourist_phone_no | tourist_email | tourist_city | package_name | date | mode_of_transport | price")
            for row in reader:
                print(row)
    except:
        print("No Booking Records Found")


# Generate Bill
def generate_bill():
    pid = input("Enter Booking ID: ")

    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:



                if row[0] == pid:   # correct column for package_id

                    place = row[5]
                    days = row[7]
                    package_price = row[9]
                    transport = row[8]



                    # total = package_price + transport_price

                    print("\n------ BILL ------")
                    print("Package ID :", pid)
                    print("Place :", place)
                    print("Days :", days)
                    print("Package Price :", package_price)
                    print("Transport :", transport)
                    # print("Transport Price :", transport_price)
                    # print("Total Amount :", total)
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
        speak("Thank You for Visiting Our Site")
        print("Thank You for Visiting Our Site")
        break

    else:
        print("Invalid Choice")