# Add Tourist
import csv
import os
import matplotlib.pyplot as plt
import pyttsx3
from datetime import datetime
from pyttsx3 import speak



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

def speak_back(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 10.0)
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()
    return text



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

    name = input(speak_back("Enter Name: "))


    while True:
        phone = input(speak_back("Enter Phone no: "))
        if len(phone) == 10 and phone.isdigit():
            break
        print(speak_back("Please enter a valid 10 digit phone number"))

    while True:
        email = input(speak_back("Enter Email: "))
        if email[-10:] == "@gmail.com":
            break
        print(speak_back("Please enter a valid email Id"))



    city = input(speak_back("Enter City: "))

    while True:
        aadhar = input(speak_back("Enter Aadhar No: "))
        parts = aadhar.split(" ")

        if len(parts) == 3 and all(len(p) == 4 and p.isdigit() for p in parts):
            break
        print(speak_back("Please enter a valid 12 digit Aadhar number"))

    with open("tourists.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tid, name, phone, email, city, aadhar])

    print(speak_back("Tourist Added Successfully"))
    tourist_id_speak = "Generated Tourist ID:", tid
    print(speak_back(tourist_id_speak))
# View Tourists
def view_tourists():
    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print(speak_back("No Tourist Records Found"))


# Search Tourist
def search_tourist():
    tid = input(speak_back("Enter Tourist ID: "))

    found = False
    try:
        with open("tourists.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == tid:
                    tourist_found_text = "Tourist Found:", row
                    print(speak_back(tourist_found_text))
                    found = True
                    break
    except:
        print(speak_back("File not found"))

    if not found:
        print(speak_back("Tourist Not Found"))



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
        print(speak_back("File not found"))

    if not found:
        print(speak_back("Tourist Not Found"))


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
        print(speak_back("File not found"))

    if not found:
        print(speak_back("Package Not Found"))




# Show Packages
def show_packages():
    print(speak_back("\nAvailable Packages\n"))

    try:
        with open("packages.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print(speak_back("Package File Not Found"))


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

    tourist_id = input(speak_back("Enter Tourist ID: "))

    # tourist_name = input("Enter Tourist Name: ")

    tourist_details = fetch_tourist(tourist_id)

    show_packages()

    package_id = input(speak_back("Enter Package ID: "))
    package_details = fetch_package(package_id)

    date = input(speak_back("Enter Travel Date (dd-mm-yyyy): "))
    while True:
        try:
            datetime.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            date = input(speak_back("Please enter valid date :"))

    #date input second method
    # while True:
    #     date = input("Enter Travel Date (dd-mm-yyyy): ")
    #     parts = date.split("-")
    #
    #     if len(parts) == 3 and all(p.isdigit() for p in parts):
    #         dd, mm, yyyy = parts
    #
    #         if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
    #             break
    #
    #     print("Please enter date in dd-mm-yyyy format")

    print("\nTransport Type")
    print("1. Bus")
    print("2. Train")
    print("3. Flight")

    choice = int(input(speak_back("Enter Transport Number: ")))

    if choice == 1:
        transport = "Bus"
        price = package_details[3]
    elif choice == 2:
        transport = "Train"
        price = package_details[4]
    elif choice == 3:
        transport = "Flight"
        price = package_details[5]
    else:
        print("Invalid Choice")
        return

    with open("bookings.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([booking_id, tourist_id, tourist_details[1], tourist_details[2], tourist_details[3], tourist_details[4], package_details[1], date, transport, price])

    print(speak_back("Package Booked Successfully"))
    booking_text = "Generated Booking ID:", booking_id

    print(speak_back(booking_text))
# CHART FUNCTIONS
#transport chart
def transport_chart():

    bus = 0
    train = 0
    flight = 0

    try:
        with open("bookings.csv", "r") as f:

            reader = csv.reader(f)

            for row in reader:

                if not row:
                    continue

                if row[8] == "Bus":
                    bus += 1

                elif row[8] == "Train":
                    train += 1

                elif row[8] == "Flight":
                    flight += 1

    except:
            print("Bookings file not found")
            return

    labels = ["Bus", "Train", "Flight"]
    values = [bus, train, flight]


    plt.pie(values, labels=labels)
    plt.title("Transport Usage")
    # plt.xlabel("Transport")
    # plt.ylabel("Bookings")
    plt.show()

#package chart
def package_chart():

    package_count = {}

    try:
        with open("bookings.csv", "r") as f:

            reader = csv.reader(f)
            next(reader)

            for row in reader:

                pid = row[6]

                if pid in package_count:
                    package_count[pid] += 1
                else:
                    package_count[pid] = 1

    except:
            print("Bookings file not found")
            return

    packages = list(package_count.keys())
    counts = list(package_count.values())

    plt.pie(counts, labels=packages)
    plt.title("Package Popularity")
    # plt.xlabel("Package Name")
    # plt.ylabel("Bookings")
    plt.show()

    #city chart
def city_chart():

    city_count = {}

    try:
        with open("tourists.csv", "r") as f:

            reader = csv.reader(f)

            for row in reader:

                city = row[4]

                if city in city_count:
                    city_count[city] += 1
                else:
                    city_count[city] = 1

    except:
        print("Tourists file not found")
        return

    cities = list(city_count.keys())
    counts = list(city_count.values())

    plt.pie(counts, labels = cities)
    plt.title("Tourists by City")
    # plt.xlabel("City")
    # plt.ylabel("Tourists")
    plt.show()

    # CHART MENU
def chart_menu():

    while True:

        print("\n------ CHART ANALYTICS ------")
        print("1. Transport Usage Chart")
        print("2. Package Popularity Chart")
        print("3. Tourist City Chart")
        print("4. Back to Main Menu")

        ch = input("Enter Choice: ")

        if ch == "1":
            transport_chart()

        elif ch == "2":
            package_chart()

        elif ch == "3":
            city_chart()

        elif ch == "4":
            break

        else:
            print("Invalid Choice")



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
    pid = input(speak_back("Enter Booking ID: "))






    try:
        with open("bookings.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:



                if row[0] == pid:   # correct column for package_id

                    name = row[2]
                    tourist_add = row[5]
                    place = row[6]
                    date = row[7]
                    package_price = row[9]
                    transport = row[8]

                    with open("packages.csv", "r") as p_f:
                        p_reader = csv.reader(p_f)

                        for p_row in p_reader:
                            if p_row[1] == row[6]:
                                duration = p_row[2]




                    print("\n------ BILL ------")
                    print("Package ID :", pid)
                    print("Tourist Name :", name)
                    print("Tourist Address :", tourist_add)
                    print("Date :", date)
                    print("Duration :", duration)
                    print("Place :", place)
                    print("Package Price :", package_price)
                    print("Transport :", transport)
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
    print("7. View Chart")
    print("8. Exit")

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
        chart_menu()

    elif ch == "8":
        print(speak_back("Thank You for Visiting Our Site"))
        break

    else:
        print(speak_back("Invalid Choice"))