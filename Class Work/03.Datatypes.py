#data types in python:

'''1. Numeric Types:
->int – Integer
->float – Floating-point
->complex – Complex Numbers'''

#int:
product_quantity = 3
order_id = 1049543
type(product_quantity)      # <class 'int'>

#float
product_price = 739.99
discount = 45.5
type(discount)              # <class 'float'>

#complex
z = 5 + 2j
type(z)                     # <class 'complex'>

'''
2. Sequence data types
->str - String
->list - List
->tuple - Tuple
'''

#str
name = "Yuvateja"
Address = "Pragati nagar rd,Hyderabad"
print(type(Address))        # <class 'str'>

#list
cart_items = ["Shoes", "shirts", "Tshirts", "headphones"]
top_categories = ["Mobiles", "Fashion", "Home"]
print(type(top_categories)) # <class 'list'>

#tuple
warehouse_location = (12.954323, 564324)
product_dimensions = (12.5, 9.7, 34)
print(type(product_dimensions))  # <class 'tuple'>

'''
3. Set data types
->set
->frozenset
'''

#set
available_sizes = {"M", "L", "XL", "XXL"}
popular_brands = {"Nike", "Adidas", "Puma", "Nike"}
print(type(available_sizes))     # <class 'set'>

#frozenset
frozen_tags = frozenset(["Sale", "Limited edition", "Trending"])
print(type(frozen_tags))         # <class 'frozenset'>

#Mapping type

#Dict - Dictionary
product_details = {
    "name": "wireless mouse",
    "brand": "logitech",
    "Price": 899.99,
    "rating": 4.5
}
print(type(product_details))     # <class 'dict'>

#boolean type
is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(type(is_logged_in))        # <class 'bool'>

#none type
tracking_number = None
delivery_partner = None
print(type(tracking_number))     # <class 'NoneType'>

