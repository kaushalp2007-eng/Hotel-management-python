import random
import datetime

name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i = 0

def date(c):
    try:
        day_val, month_val, year_val = c[0], c[1], c[2]
        if not (2019 <= year_val <= 2026):
            return False

        datetime.date(year_val, month_val, day_val)
        return True
    except ValueError:
        return False

def Home():
    while True:
        print("\t\t\t\t WELCOME TO HOTEL ANCASA")
        print("\t\t\t 1 Booking")
        print("\t\t\t 2 Rooms Info")
        print("\t\t\t 3 Room Service(Menu Card)")
        print("\t\t\t 4 Payment")
        print("\t\t\t 0 Exit")

        try:
            ch = int(input("-> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            Booking()
        elif ch == 2:
            Rooms_Info()
        elif ch == 3:
            restaurant()
        elif ch == 4:
            Payment()
        elif ch == 0:
            print("Exiting Hotel AnCasa. Thank you!")
            break
        else:
            print("Invalid Choice! Please try again.")

def Booking():
    global i
    print("\n---- BOOKING ROOMS ----\n")

    while True:
        n = str(input("Name: "))
        p1 = str(input("Phone No.: "))
        a = str(input("Address: "))
        if n != "" and p1 != "" and a != "":
            name.append(n)
            phno.append(p1)
            add.append(a)
            break
        else:
            print("Name, Phone no. & Address cannot be empty..!!")

    ci_list = []
    co_list = []
    d1 = None
    d2 = None

    while True:
        cii_str = input("Check-In (dd/mm/yyyy): ")
        try:
            ci_list = [int(x) for x in cii_str.split('/')]
            if len(ci_list) != 3:
                raise ValueError("Date must be in dd/mm/yyyy format.")
            if not date(ci_list):
                print("Invalid Check-In date. Please try again.")
                continue
            d1 = datetime.datetime(ci_list[2], ci_list[1], ci_list[0])
            break
        except ValueError as e:
            print(f"Invalid Check-In date format or value: {e}. Please use dd/mm/yyyy.")

    while True:
        coo_str = input("Check-Out (dd/mm/yyyy): ")
        try:
            co_list = [int(x) for x in coo_str.split('/')]
            if len(co_list) != 3:
                raise ValueError("Date must be in dd/mm/yyyy format.")
            if not date(co_list):
                print("Invalid Check-Out date. Please try again.")
                continue
            d2 = datetime.datetime(co_list[2], co_list[1], co_list[0])
            if d2 <= d1:
                print("\nCheck-Out date must fall after Check-In. Please re-enter Check-Out date.")
                continue
            break
        except ValueError as e:
            print(f"Invalid Check-Out date format or value: {e}. Please use dd/mm/yyyy.")

    checkin.append(cii_str)
    checkout.append(coo_str)
    d = (d2 - d1).days
    day.append(d)

    print("\n----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC - Rs. 3500/day")
    print(" 2. Standard AC - Rs. 4000/day")
    print(" 3. 3-Bed Non-AC - Rs. 4500/day")
    print(" 4. 3-Bed AC - Rs. 5000/day")

    while True:
        try:
            ch = int(input("-> "))
            if ch == 1:
                room.append('Standard Non-AC')
                price.append(3500)
                break
            elif ch == 2:
                room.append('Standard AC')
                price.append(4000)
                break
            elif ch == 3:
                room.append('3-Bed Non-AC')
                price.append(4500)
                break
            elif ch == 4:
                room.append('3-Bed AC')
                price.append(5000)
                break
            else:
                print("Wrong choice. Please enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10


    while rn in roomno:
        rn = random.randrange(60) + 300
    while cid in custid:
        cid = random.randrange(60) + 10

    roomno.append(rn)
    custid.append(cid)
    rc.append(0)
    p.append(0)

    print("\n*** ROOM BOOKED SUCCESSFULLY ***")
    print(f"Room No. - {rn}")
    print(f"Customer Id - {cid}")
    i += 1

def Rooms_Info():
    print("\n------ HOTEL ROOMS INFO ------\n")
    print("STANDARD NON-AC - Double Bed, TV, Telephone, Balcony, Washroom\n")
    print("STANDARD AC - Double Bed, TV, Telephone, Balcony, Washroom, AC\n")
    print("3-Bed NON-AC - 3 Beds, TV, Telephone, Balcony, Washroom\n")
    print("3-Bed AC - 3 Beds, TV, Telephone, Balcony, Washroom, AC\n")

def restaurant():
    try:
        ph = int(input("Customer Id: "))
    except ValueError:
        print("Invalid input. Please enter a valid Customer Id (number).")
        return

    global i
    f = 0
    r = 0
    for n in range(i):
        if n < len(custid) and custid[n] == ph and p[n] == 0:
            f = 1
            print("\n---- HOTEL ANCASA MENU ----")
            print("39 Masala Dosa - 130")
            print("32 Butter Naan - 20")
            print("40 Paneer Dosa - 130")
            print("Press 0 to end order")

            while True:
                try:
                    ch = int(input("-> "))
                    if ch == 39:
                        r += 130
                    elif ch == 32:
                        r += 20
                    elif ch == 40:
                        r += 130
                    elif ch == 0:
                        break
                    else:
                        print("Invalid choice. Please choose from the menu or press 0.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            print(f"\nTotal Restaurant Bill: Rs. {r}")
            rc[n] += r
            break
    if f == 0:
        print("Invalid Customer Id or payment already made.")


def Payment():
    ph = str(input("Phone Number: "))
    global i
    f = 0

    for n in range(i):
        if n < len(phno) and ph == phno[n]:
            if p[n] == 0:
                f = 1
                print("\n---- PAYMENT ----")
                print("1- Credit/Debit Card")
                print("2- Paytm/PhonePe")
                print("3- Using UPI")
                print("4- Cash")
                try:
                    _ = int(input("-> "))
                except ValueError:
                    print("Invalid input for payment method. Please enter a number.")
                    return


                if n < len(price) and n < len(day) and n < len(rc):
                    total_amt = (price[n] * day[n]) + rc[n]
                else:
                    print("Error: Booking details incomplete for this customer.")
                    return

                print(f"\nAmount to Pay: Rs. {total_amt}")

                ch = input("Confirm Payment? (y/n): ")
                if ch.lower() == 'y':
                    print("\n---- HOTEL ANCASA BILL ----")
                    print(f"Name: {name[n]}")
                    print(f"Phone No.: {phno[n]}")
                    print(f"Address: {add[n]}")
                    print(f"Check-In: {checkin[n]}")
                    print(f"Check-Out: {checkout[n]}")
                    print(f"Room Type: {room[n]}")
                    print(f"Room Charges: {price[n] * day[n]}")
                    print(f"Restaurant Charges: {rc[n]}")
                    print(f"Total Amount Paid: {total_amt}")
                    print("\nThank You. Visit Again!\n")

                    p[n] = 1

                    if n < len(roomno):
                        roomno[n] = 0
                    if n < len(custid):
                        custid[n] = 0
            else:
                print("Payment already done.")
            f = 1
            break
    if f == 0:
        print("Invalid Phone Number or no booking found for this number.")

Home()