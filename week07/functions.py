# Reflection questions:
# 1. The first bug I noticed was the syntax error, I found it after using AI to check the code. It tells me I still don't know much about debugging and need to look more carefully at code.
# 2. It takes two inputs and applies discounts on the tiers the inputs are the customers membership and the original price. A colleague would only be able to use it without reading the body if they knew the tiers and discount rates already. 
# 3. AI USE - Debugger (helped on exercise 5) The AI helped build my understanding


# Exercise 1
def calculate_tax(price,rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")


# Exercise 3

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4 

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5 

# broken_sales.py - trace and diagnose before fixing anything.
# sales = [120, 80, 250, 175, 90]

# total = 0
# for sale in sales:
#      print(f"Before: sale={sale}, total={total}")
#     total = sale
#     print(f"After: total={total}"
# print(f"Total: ${total}")

# count = 0
# for sale in sales # Add a colon here to fix the syntax error
#     count += 1
# print(f"Count: {count}")

# i = 0
# while i <= len(sales):
#     print(f"Checking index {i}; list length is {len(sales)}")
#     print(sales[i])
#     i += 1

# # What the syntax error means: SyntaxError: expected ':' means Python expected a colon (:) where one is missing. Colons mark the start of an indented block after statements such as for, while, if, or def


# Exercise 6 

x = 100 

def double_it():
    x = 999
    return x * 2

print(x) # 100 prints here 
print(double_it()) # 1998 prints here 
print(x) # 100 prints here 

# The scope determines where a variable can be used
# assigning 999 doesn't change the global x because the x inside double_it belongs to that function.