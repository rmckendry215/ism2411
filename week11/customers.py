# customers.py
# Author: Randall McKendry
# Module 11 Lab: Customer Dictionary & Lookup

print("--- Exercise 1 ---")
customer = {
    "name": "Alice", #Key : Value
    "email": "alice@example.com",
    "tier": "gold", 
    "ytd_spend": 12400,
}

print(customer["name"]) #Alice
print(customer["email"]) #alice@example.com
print(customer["tier"]) #gold
print(customer["ytd_spend"]) #12400

print("--- Exercise 2 ---")
customer['phone'] = '555-5555' #adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' #updating the value of an existing key
print(customer)
del customer['name'] #removing a key-value pair from the dictionary
print(customer)
