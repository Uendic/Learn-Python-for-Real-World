
"""
DAY 02 — DATA TYPES
EXERCISE SOLUTIONS

Try to solve every exercise independently before checking this file.
"""


# ============================================================
# EXERCISE 1 — CUSTOMER PROFILE
# ============================================================

customer = {
    "customer_id": 1050,
    "name": "Sarah Johnson",
    "email": "sarah@example.com",
    "age": 29,
    "account_active": True
}

print("EXERCISE 1")

print(customer["name"])
print(customer["email"])
print(customer["account_active"])

for key, value in customer.items():
    print(key, type(value))


# ============================================================
# EXERCISE 2 — INVENTORY MANAGEMENT
# ============================================================

inventory = [45, 30, 75, 20]

print("\nEXERCISE 2")

print("Original inventory:", inventory)
print("First quantity:", inventory[0])
print("Last quantity:", inventory[-1])

inventory.append(15)
inventory[1] = 50

print("Updated inventory:", inventory)
print("Number of products:", len(inventory))
print("Total inventory quantity:", sum(inventory))


# ============================================================
# EXERCISE 3 — SUBSCRIPTION PRICE CALCULATOR
# ============================================================

starter_price = 9.99
professional_price = 29.99
business_price = 79.99

subscription_prices = [
    starter_price,
    professional_price,
    business_price
]

total_price = sum(subscription_prices)
average_price = total_price / len(subscription_prices)

print("\nEXERCISE 3")

print(f"Starter: ${starter_price:.2f}")
print(f"Professional: ${professional_price:.2f}")
print(f"Business: ${business_price:.2f}")
print(f"Total: ${total_price:.2f}")
print(f"Average: ${average_price:.2f}")


# ============================================================
# EXERCISE 4 — SUPPORT TICKET TRACKER
# ============================================================

support_ticket = {
    "ticket_id": 7001,
    "customer_name": "Daniel Brown",
    "issue": "Unable to access account",
    "priority": "High",
    "resolved": False
}

print("\nEXERCISE 4")

print("Ticket ID:", support_ticket["ticket_id"])
print("Customer:", support_ticket["customer_name"])

support_ticket["resolved"] = True
support_ticket["assigned_to"] = "Emma"
support_ticket["response_time_hours"] = 2.5

customer_phone = support_ticket.get(
    "customer_phone",
    "Not provided"
)

print("Customer phone:", customer_phone)
print("Complete ticket:", support_ticket)


# ============================================================
# EXERCISE 5 — DATA TYPE INSPECTION
# ============================================================

customer_name = "Michael"
customer_id = 2045
monthly_payment = 49.95
payment_received = True
payment_reference = None

print("\nEXERCISE 5")

print(customer_name, type(customer_name))
print(customer_id, type(customer_id))
print(monthly_payment, type(monthly_payment))
print(payment_received, type(payment_received))
print(payment_reference, type(payment_reference))

customer_id = str(customer_id)
monthly_payment = int(monthly_payment)
customer_name = bool(customer_name)

print("\nAfter conversion:")

print(customer_id, type(customer_id))
print(monthly_payment, type(monthly_payment))
print(customer_name, type(customer_name))


# ============================================================
# EXERCISE 6 — EMPLOYEE RECORD
# ============================================================

employee = {
    "employee_id": 301,
    "name": "Olivia Carter",
    "department": "Engineering",
    "monthly_salary": 3200.50,
    "full_time": True,
    "skills": [
        "Python",
        "SQL",
        "Problem Solving"
    ],
    "office_location": ("Tirana", "Albania")
}

print("\nEXERCISE 6")

print("Employee:", employee["name"])
print("Second skill:", employee["skills"][1])

employee["skills"].append("Git")
employee["department"] = "Software Engineering"

print("Department:", employee["department"])
print("Office location:", employee["office_location"])
print("Number of skills:", len(employee["skills"]))


# ============================================================
# EXERCISE 7 — SERVER STATUS MONITOR
# ============================================================

server = {
    "server_name": "production-server-01",
    "cpu_usage": 68.5,
    "memory_usage": 72.0,
    "server_online": True,
    "active_services": [
        "Website",
        "Database",
        "API"
    ]
}

print("\nEXERCISE 7")

high_cpu_usage = server["cpu_usage"] > 80
high_memory_usage = server["memory_usage"] > 90

print("High CPU usage:", high_cpu_usage)
print("High memory usage:", high_memory_usage)

server["active_services"].append("Email Service")

print("Active services:", server["active_services"])
print("Number of active services:", len(server["active_services"]))


# ============================================================
# EXERCISE 8 — CUSTOMER DATA CLEANING
# ============================================================

customer_countries = [
    "Albania",
    "Germany",
    "Albania",
    "Italy",
    "Germany",
    "France"
]

customer_email = "  SARAH@EXAMPLE.COM  "

print("\nEXERCISE 8")

unique_countries = set(customer_countries)

cleaned_email = customer_email.strip().lower()

print("Unique countries:", unique_countries)
print("Cleaned email:", cleaned_email)
print("Number of unique countries:", len(unique_countries))


# ============================================================
# EXERCISE 9 — SAAS REVENUE DATA
# ============================================================

starter_plan = {
    "name": "Starter",
    "customers": 120,
    "monthly_price": 9.99
}

professional_plan = {
    "name": "Professional",
    "customers": 75,
    "monthly_price": 29.99
}

business_plan = {
    "name": "Business",
    "customers": 25,
    "monthly_price": 79.99
}

plans = [
    starter_plan,
    professional_plan,
    business_plan
]

print("\nEXERCISE 9")
print("SUBSCRIPTION REVENUE REPORT")
print("---------------------------")

total_mrr = 0
total_customers = 0

for plan in plans:
    plan_mrr = plan["customers"] * plan["monthly_price"]

    total_mrr += plan_mrr
    total_customers += plan["customers"]

    print(f"\nPlan: {plan['name']}")
    print(f"Customers: {plan['customers']}")
    print(f"Monthly price: ${plan['monthly_price']:.2f}")
    print(f"Plan MRR: ${plan_mrr:.2f}")

plan_names = {
    starter_plan["name"],
    professional_plan["name"],
    business_plan["name"]
}

print("\n---------------------------")
print(f"Total customers: {total_customers}")
print(f"Total MRR: ${total_mrr:.2f}")
print(f"Available plans: {plan_names}")


# ============================================================
# EXERCISE 10 — CUSTOMER AND ORDER DATA MANAGER
# ============================================================

customer = {
    "customer_id": 9001,
    "name": "James Wilson",
    "email": "james@example.com",
    "account_active": True,
    "phone_number": None
}

order = {
    "order_id": 6001,
    "products": [
        "Keyboard",
        "Mouse",
        "Monitor"
    ],
    "prices": [
        59.99,
        24.99,
        189.99
    ],
    "quantities": [
        2,
        1,
        1
    ],
    "payment_completed": False
}

print("\nEXERCISE 10")
print("CUSTOMER AND ORDER REPORT")
print("-------------------------")

print("Customer:", customer["name"])
print("Email:", customer["email"])

if customer["phone_number"] is None:
    print("Phone number not provided")
else:
    print("Phone:", customer["phone_number"])

total_order_value = 0

for index in range(len(order["products"])):
    product_name = order["products"][index]
    product_price = order["prices"][index]
    product_quantity = order["quantities"][index]

    product_total = product_price * product_quantity

    total_order_value += product_total

    print(
        f"{product_name}: "
        f"{product_quantity} x "
        f"${product_price:.2f} = "
        f"${product_total:.2f}"
    )

order["payment_completed"] = True

print("\nOrder ID:", order["order_id"])
print("Products:", order["products"])
print(f"Total order value: ${total_order_value:.2f}")
print("Payment completed:", order["payment_completed"])
print("Total value data type:", type(total_order_value))
