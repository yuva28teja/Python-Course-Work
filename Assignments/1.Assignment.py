# ---------------- Zepto Product Information System ----------------
# User Name: Yuva
# User Phone: 9876543210

# Product Details
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

categories = input("Enter Categories (comma-separated): ").split(",")

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage: "))

product_features = set(input("Enter Product Features (comma-separated): ").split(","))

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

print("\n=========== ZEPTO PRODUCT DETAILS ===========\n")

# Using the static details from comments
print("User Name: Yuva")
print("User Phone Number: 9876543210")
print()

# ----- Output -----

# 1. Using Comma Separation
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Product Discount: %.2f%%" % discount_percentage)

# 3. Using f-strings
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")

# 4. Using .format() method
print("Supplier Details: Name - {}, Contact - {}, Location - {}"
      .format(supplier_details['name'], supplier_details['contact'], supplier_details['location']))


# ------------------------- SAMPLE OUTPUT -------------------------
# Enter Product ID: 101
# Enter Product Name: Amul Milk
# Enter Price: 28
# Enter Categories (comma-separated): Dairy,Daily
# Enter Available Stock: 120
# Enter Sold Stock: 80
# Enter Discount Percentage: 5
# Enter Product Features (comma-separated): Fresh,High Quality,Low Fat
# Enter Supplier Name: Amul Pvt Ltd
# Enter Supplier Contact Number: 9988776655
# Enter Supplier Location: Gujarat
#
# =========== ZEPTO PRODUCT DETAILS ===========
#
# User Name: Yuva
# User Phone Number: 9876543210
#
# Product ID, Name, Price: 101, Amul Milk, 28.0
# Product Discount: 5.00%
# Product Name: Amul Milk
# Price: ₹28.0
# Discount: 5.0%
# Stock Available: 120 units
# Supplier Details: Name - Amul Pvt Ltd, Contact - 9988776655, Location - Gujarat
