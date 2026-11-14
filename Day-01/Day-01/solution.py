# =====================================================================
# DAY 1 SOLUTION: Business Client Account Summary
# =====================================================================
# This script stores a new business client's details using appropriate 
# data types, calculates the total invoice, and displays a clean summary.

# 1. We store the client's company name in a string variable.
# WHY: Text data must always be enclosed in quotation marks.
client_name = "Northstar Logistics"

# 2. We store the number of software licenses bought in an integer variable.
# WHY: License seats represent discrete whole counts that cannot be fractional.
licenses_purchased = 12

# 3. We store the exact price per license in a float variable.
# WHY: Financial amounts require precise decimal numbers to handle cents accurately.
price_per_license = 29.99

# 4. We store whether payment was successfully confirmed in a boolean variable.
# WHY: Booleans act as binary flags (True or False) to gate features or check status.
payment_confirmed = True

# 5. We store the primary contact email in a string variable.
# WHY: Emails contain text characters like '@' and letters, requiring string formatting.
billing_email = "billing@northstar.io"

# We calculate the total invoice amount by multiplying licenses by the unit price.
total_invoice = licenses_purchased * price_per_license

# 6. We use the print() function to display a clean account summary in our terminal.
# WHY: Print statements allow developers and system logs to verify live data values.
print("-----------------------------------------")
print("        BUSINESS CLIENT SUMMARY          ")
print("-----------------------------------------")
print("Client Company Name :", client_name)
print("Primary Billing Email:", billing_email)
print("Licenses Purchased   :", licenses_purchased)
print("Price per License    : $", price_per_license)
print("Total Invoice Amount : $", total_invoice)
print("Payment Confirmed    :", payment_confirmed)
print("-----------------------------------------")

# EXPECTED TERMINAL OUTPUT:
# -----------------------------------------
#         BUSINESS CLIENT SUMMARY          
# -----------------------------------------
# Client Company Name : Northstar Logistics
# Primary Billing Email: billing@northstar.io
# Licenses Purchased   : 12
# Price per License    : $ 29.99
# Total Invoice Amount : $ 359.88
# Payment Confirmed    : True
# -----------------------------------------
