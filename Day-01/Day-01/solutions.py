
"""
DAY 01 : COMPLETE SOLUTIONS
Beginner to Advanced

Attempt all exercises in exercises.py first.
"""


# ==================================================
# EXERCISE 01 : CUSTOMER PROFILE
# ==================================================

customer_full_name = "Jordan Lee"
customer_email = "jordan.lee@example.com"
customer_age = 34
is_account_verified = True

print(customer_full_name)
print(customer_email)
print(customer_age)
print(is_account_verified)


# ==================================================
# EXERCISE 02 : INVENTORY MANAGEMENT
# ==================================================

inventory_units = 850

inventory_units -= 135
inventory_units += 240

print("Final inventory:", inventory_units)


# ==================================================
# EXERCISE 03 : SUBSCRIPTION CALCULATOR
# ==================================================

active_seats = 36
monthly_price_per_seat = 18.50

monthly_subscription_value = (
    active_seats * monthly_price_per_seat
)

print(f"Monthly value: {monthly_subscription_value:.2f}")


# ==================================================
# EXERCISE 04 : SUPPORT TICKET TRACKER
# ==================================================

open_tickets = 12

open_tickets += 9
tickets_after_arrivals = open_tickets

open_tickets -= 14

print("After arrivals:", tickets_after_arrivals)
print("Final open tickets:", open_tickets)


# ==================================================
# EXERCISE 05 : DATA TYPE INSPECTION
# ==================================================

product_name = "Wireless Access Point"
stock_quantity = 48
unit_price = 129.95
is_product_available = True

print(product_name, type(product_name))
print(stock_quantity, type(stock_quantity))
print(unit_price, type(unit_price))
print(is_product_available, type(is_product_available))

print(isinstance(stock_quantity, int))
print(isinstance(is_product_available, bool))


# ==================================================
# EXERCISE 06 : EMPLOYEE RECORD
# ==================================================

employee_id = 70418
employee_department = "Software Engineering"
annual_salary = 68000.00
employment_status = "Full-time"

print(f"Employee ID: {employee_id}")
print(f"Department: {employee_department}")
print(f"Annual salary: {annual_salary:.2f}")
print(f"Employment: {employment_status}")


# ==================================================
# EXERCISE 07 : SERVER SWAPPING
# ==================================================

primary_server = "api-primary"
backup_server = "api-backup"

print("Before:", primary_server, backup_server)

primary_server, backup_server = (
    backup_server,
    primary_server
)

print("After:", primary_server, backup_server)


# ==================================================
# EXERCISE 08 : MUTABLE REFERENCES
# ==================================================

primary_customer = {
    "name": "Jordan Lee",
    "status": "active"
}

support_customer = primary_customer

support_customer["status"] = "under_review"

print("Original:", primary_customer)
print("Support:", support_customer)

independent_customer = primary_customer.copy()

independent_customer["status"] = "suspended"

print("Original after copy update:", primary_customer)
print("Independent copy:", independent_customer)


# ==================================================
# EXERCISE 09 : SAAS REVENUE REPORT
# ==================================================

starter_accounts = 125
starter_monthly_price = 12.00

growth_accounts = 80
growth_monthly_price = 29.00

business_accounts = 24
business_monthly_price = 79.00

starter_mrr = starter_accounts * starter_monthly_price
growth_mrr = growth_accounts * growth_monthly_price
business_mrr = business_accounts * business_monthly_price

total_mrr = (
    starter_mrr
    + growth_mrr
    + business_mrr
)

print("\nMONTHLY RECURRING REVENUE")
print("-------------------------")

print(f"Starter MRR:  {starter_mrr:.2f}")
print(f"Growth MRR:   {growth_mrr:.2f}")
print(f"Business MRR: {business_mrr:.2f}")
print(f"Total MRR:    {total_mrr:.2f}")


# ==================================================
# EXERCISE 10 : B2B ACCOUNT SNAPSHOT
# ==================================================

customer_name = "Taylor Morgan"
company_name = "Vertex Operations"
account_id = "ACCT-20841"
plan_name = "Business"

licensed_seats = 75
used_seats = 61
price_per_seat = 32.00

is_account_active = True
open_support_tickets = 3

customer_region = "EMEA"
account_manager = "Alex Rivera"

unused_seats = licensed_seats - used_seats

monthly_contract_value = (
    licensed_seats * price_per_seat
)

annualized_contract_value = (
    monthly_contract_value * 12
)

print("\nB2B CUSTOMER ACCOUNT")
print("--------------------")

print(f"Customer: {customer_name}")
print(f"Company: {company_name}")
print(f"Account ID: {account_id}")
print(f"Plan: {plan_name}")
print(f"Licensed seats: {licensed_seats}")
print(f"Used seats: {used_seats}")
print(f"Unused seats: {unused_seats}")

print(f"Monthly contract value: {monthly_contract_value:.2f}")
print(f"Annual contract value: {annualized_contract_value:.2f}")

print(f"Active: {is_account_active}")
print(f"Open tickets: {open_support_tickets}")
print(f"Region: {customer_region}")
print(f"Account manager: {account_manager}")


customer_record = {
    "customer_name": customer_name,
    "company_name": company_name,
    "status": "active"
}

customer_record_for_support = customer_record

customer_record_for_support["status"] = "under_review"

print("\nOriginal customer:", customer_record)
print("Support customer:", customer_record_for_support)


# EXPLANATION:
#
# String values:
# customer_name, company_name, account_id, plan_name,
# customer_region, account_manager.
#
# Integer values:
# licensed_seats, used_seats, open_support_tickets,
# unused_seats.
#
# Float values:
# price_per_seat, monthly_contract_value,
# annualized_contract_value.
#
# Boolean:
# is_account_active.
#
# Calculations:
# unused_seats depends on licensed_seats and used_seats.
# monthly_contract_value depends on licensed_seats and price_per_seat.
# annualized_contract_value depends on monthly_contract_value.
#
# Dictionary reference:
# Both customer_record and customer_record_for_support
# refer to the same dictionary object.
# Therefore, changing the dictionary through one name
# is visible through the other name.
