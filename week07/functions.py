# Self-Assessment 1:
# You start with total = 0. Then the loop goes through each number and adds it to the total amount then when the loop is done, the total has the final answer.

# Self-Assessment 2:
# The while loop was longer because I had to keep track of the number myself. The for loop was easier for me to read and took less code to do.

# Self-Assessment 3:
# In finance, I could use/have a list of daily sales. I could use a loop to add them up or find the biggest sale of the day or soemthing like that then I could print the total or highest amount.

# Ai Disclosure: I used chatgpt to help me with the error codes and to tell me what the message means, so i could then take that knowledge and fix the issue myself. 

# --- Exercice 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercice 2 ---

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# --- Exercice 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercice 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")


# --- Exercice 5 ---
# import unit2.module07.broken_sales

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:  # goes through each sale in the list
    total += sale  # add the sale to the total - added the "+" next to the "=" to make addition work correctly
print(f"Total: ${total}")

count = 0
for sale in sales:  # goes through each sale in the list - added the ":" to make it a loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # stops before the index goes out of the range - removed the "=" next to the "<" to make it a less than comparison not less than or equal to
    print(sales[i])
    i += 1


# --- Exercice 6 ---

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x) # x will come out as 100
print(double_it()) # will come out as 1998 (double 999)
print(x) # x will come out as 100