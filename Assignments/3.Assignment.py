'''Python Weekly Test - 3 Solutions'''

# Q1: Automated Salary Tax Calculator
sal = float(input("Enter the salary: "))
tax = 0

if sal <= 250000:
    tax = 0
elif sal <= 500000:
    tax = sal * 0.05
elif sal <= 1000000:
    tax = sal * 0.2
else:
    tax = sal * 0.3

print(f'Tax amount: {tax}\nSalary after tax: {sal - tax}')


# Q2: Movie Ticket Pricing System
n = int(input("No of persons: "))
total = 0

for _ in range(n):
    age = int(input("Enter age: "))
    if age < 5:
        continue
    elif age <= 18:
        total += 100
    elif age <= 60:
        total += 150
    else:
        total += 120

print(total)


# Q3: Electricity Bill Generator
units = int(input("Enter units: "))
bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 150 + (units - 100) * 2.5
elif units <= 500:
    bill = 400 + (units - 200) * 4
else:
    bill = 1600 + (units - 500) * 6

print(bill)


# Q4: Car Parking Fee Calculator
hrs = int(input("Enter hours: "))
fee = 30

if hrs <= 2:
    fee = 30
elif hrs < 24:
    fee = 30 + (hrs - 2) * 10
else:
    fee = 200

print(fee)


# Q5: Product Inventory Checker
name = input("Enter product name: ")
qty = int(input("Enter quantity: "))

if qty == 0:
    status = "Out of Stock"
elif qty <= 10:
    status = "Low Stock"
elif qty <= 50:
    status = "In Stock"
else:
    status = "Overstocked"

print(f'{name}: {status}')


# Q6: Pattern - Row-wise Alternating 0 and 1
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=' ')
    print()


# Q7: Gym Subscription Billing
billing = {1: 500, 2: 1300, 3: 5000}
choice = int(input("Enter choice (1/2/3): "))
persons = int(input("Enter number of persons: "))

print(billing[choice] * persons)


# Q8: Billing Bot - Discount
amount = float(input("Enter amount: "))

if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.05
elif amount < 10000:
    discount = amount * 0.1
else:
    discount = amount * 0.15

print(amount - discount)


# Q9: ATM PIN Verification
stored_pin = 1234

for i in range(3):
    pin = int(input("Enter PIN: "))
    if pin == stored_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")


# Q10: Bus Booking System
n = int(input("Enter total seats: "))
booked_seats = list(map(int, input().split()))

print(f"Total Seats: {n}")
print(f"Booked: {len(booked_seats)}")
print(f"Available: {n - len(booked_seats)}")
