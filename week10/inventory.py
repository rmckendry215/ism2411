# inventory.py
# Author: Randall McKendry
# Module 10 Lab: Inventory List Manager


# Exercise 1: Build a list

print("--- Exercise 1: Build a list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory) # prints the entire list
print(len(inventory)) # prints the length of the list

# Exercise 2: Index Practice

print ("--- Exercise 2: Index Practice ---")
print(inventory[0]) # always grab the first item in a list
print(inventory[-1]) # always grab the last item in a list

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item in a list (not hard coded)


# Exercise 3: List Slicing

print("--- Exercise 3: List Slicing ---")
print(inventory[:3]) # grabs the first three items
print(inventory[-2:]) # grabs the last two items
print(inventory[::2]) # grabs every second item

# Exercise 4: List Methods

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
inventory.append("tape") # adds an item to the end of the list
print(inventory)

inventory.remove("tape") # removes an item from the list
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

# Exercise 5: Tuple Comparison

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")


# Exercise 6: List Average Sales

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average:.2f}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

# Exercise 7: Accumulator Pattern

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount and round to 2 decimal places
print(prices)
print(discounted)

# Exercise 8: Filter

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # empty list
for amount in sales:
    if amount > 300:
        high_sales.append(amount) # add to the list if the amount is greater than 300

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")

# Reflection 1: What is the most surprising thing about how lists work in Python compared to what you expected coming in?
# The most surprising thing to me is how easy it is to get different parts of a list. I didn't expect things like negative numbers or slicing to make it so simple to pick the certain items I want. 
#
# Reflection 2: Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel. 
# In a finance class, I could use a list to keep track of daily sales or prices. Python could add them, find the highest and lowest, and calculate the average without me doing a single step in Excel. 
