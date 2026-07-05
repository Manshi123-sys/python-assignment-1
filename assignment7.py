import csv
import os

filename = "contacts.csv"

# Create file with header if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Mobile", "Email"])


while True:

    print("\n===== ADDRESS BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")

        contact = [name, mobile, email]

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(contact)

        print("Contact Added Successfully!")

    elif choice == "2":

        with open(filename, "r") as file:
            reader = csv.reader(file)

            print("\n----- Contact List -----")

            for row in reader:
                print(row)

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice! Please Try Again.")
