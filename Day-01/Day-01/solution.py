# DAY 1 SOLUTION: Simple Business Client Profile

# In this script, we store basic business and customer data using 
# different data types. This helps our software application remember 
# important details about our clients.

# 1. We store the company name as a text string because it contains letters.
client_name = "Northstar Logistics"

# 2. We store the total software licenses as an integer because we cannot sell half a license.
licenses = 12

# 3. We store the price per license as a float because money requires precise decimal numbers.
price = 29.99

# 4. We store the account status as a boolean (True or False) to check if the client is active.
is_active = True

# We calculate the total bill by multiplying the number of licenses by the price.
total_bill = licenses * price

# We use print statements to display a neat summary of the client account on our terminal screen.
print("-----------------------------------------")
print("        BUSINESS CLIENT SUMMARY          ")
print("-----------------------------------------")
print("The client company name is:", client_name)
print("The number of purchased licenses is:", licenses)
print("The price for each license is: $", price)
print("The total invoice bill amount is: $", total_bill)
print("Is the client account active? :", is_active)
print("-----------------------------------------")
