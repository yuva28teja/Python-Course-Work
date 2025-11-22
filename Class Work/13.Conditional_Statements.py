'''
In Python, the main types of conditional statements are:
1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested Conditional Statements
'''

# ---------------------------
# 1. IF → Check if restaurant is open
# ---------------------------
restaurant_open = True

if restaurant_open:
    print("Restaurant is accepting orders.\n")

# (Output)
# Restaurant is accepting orders.


# ---------------------------
# 2. IF-ELSE → Check for delivery charges
# ---------------------------
order_amount = 350   # sample input

if order_amount >= 300:
    print("You get FREE Delivery!\n")
else:
    print("Delivery Charges: ₹30\n")

# (Output)
# You get FREE Delivery!


# ---------------------------
# 3. IF-ELIF-ELSE → Order status tracker
# ---------------------------
status = "preparing"   # sample input

if status == "order placed":
    print("Your order has been placed")
elif status == "preparing":
    print("Your food is being prepared")
elif status == "out for delivery":
    print("Your order is on the way")
elif status == "delivered":
    print("Your order has been delivered")
else:
    print("Invalid status entered")

# (Output)
# Your food is being prepared


print()


# ---------------------------
# 4. NESTED IF → Special discount
# ---------------------------
payment_method = "online"   # sample input

if order_amount >= 400:
    print("You are eligible for a 10% discount")

    if payment_method == "online":
        print("Extra 5% discount for choosing online payment")
    else:
        print("Pay online next time for extra discount")
else:
    print("No discount for orders below ₹400.\n")

# (Output)
# No discount for orders below ₹400.


print("\nThank you for ordering with us!")

# (Output)
# Thank you for ordering with us!
