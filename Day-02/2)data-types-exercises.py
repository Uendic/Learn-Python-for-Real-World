
"""
DAY 02 — DATA TYPES
PRACTICAL EXERCISES

Instructions:
- Complete all 10 exercises.
- Write your own Python code.
- Run the file and check your results.
- Do not look at the solutions before trying each exercise.

Each exercise introduces a practical programming situation.
"""

# ============================================================
# EXERCISE 1 — CUSTOMER PROFILE
# Level: Beginner
# ============================================================

"""
Create a dictionary (a collection of key-value pairs) called
customer.

Store the following information:

- customer_id: 1050
- name: "Sarah Johnson"
- email: "sarah@example.com"
- age: 29
- account_active: True

Tasks:
1. Create the dictionary.
2. Print the customer's name.
3. Print the customer's email.
4. Print the customer's account status.
5. Print the data type of each value using type().
"""


# ============================================================
# EXERCISE 2 — INVENTORY MANAGEMENT
# Level: Beginner
# ============================================================

"""
An online store needs to track its product inventory.

Create a list called inventory containing:

- 45
- 30
- 75
- 20

Each number represents the available quantity of a product.

Tasks:
1. Print the complete inventory.
2. Print the first product quantity.
3. Print the last product quantity.
4. Add 15 to the list.
5. Change the second quantity to 50.
6. Print the total number of items in the list.
7. Calculate the total inventory quantity using sum().
"""


# ============================================================
# EXERCISE 3 — SUBSCRIPTION PRICE CALCULATOR
# Level: Beginner
# ============================================================

"""
A software company sells monthly subscriptions.

The prices are:

- Starter: 9.99
- Professional: 29.99
- Business: 79.99

Tasks:
1. Store each price in a separate variable.
2. Create a list containing all three prices.
3. Calculate the total price of all three plans.
4. Calculate the average price using sum() and len().
5. Display each result with two decimal places.

Average means the total value divided by the number of values.
"""


# ============================================================
# EXERCISE 4 — SUPPORT TICKET TRACKER
# Level: Intermediate
# ============================================================

"""
A support team needs to organize customer support tickets.

A support ticket is a record of a customer's request for help.

Create a dictionary called support_ticket containing:

- ticket_id: 7001
- customer_name: "Daniel Brown"
- issue: "Unable to access account"
- priority: "High"
- resolved: False

Tasks:
1. Create the dictionary.
2. Print the ticket ID and customer name.
3. Change resolved to True.
4. Add a new key called "assigned_to" with the value "Emma".
5. Add a new key called "response_time_hours" with the value 2.5.
6. Print the complete dictionary.
7. Use .get() to request a key called "customer_phone".
   If it does not exist, display "Not provided".
"""


# ============================================================
# EXERCISE 5 — DATA TYPE INSPECTION
# Level: Intermediate
# ============================================================

"""
A software application receives information from different sources.

Create these variables:

customer_name = "Michael"
customer_id = 2045
monthly_payment = 49.95
payment_received = True
payment_reference = None

Tasks:
1. Print the value of every variable.
2. Print the data type of every variable using type().
3. Convert customer_id into a string.
4. Convert monthly_payment into an integer.
5. Convert customer_name into a Boolean.
6. Print the new data types.

Important:
Converting a float to an integer removes its decimal part.
Do not assume that the converted value keeps its original precision.
"""


# ============================================================
# EXERCISE 6 — EMPLOYEE RECORD
# Level: Intermediate
# ============================================================

"""
A company needs to store employee information.

Create a dictionary called employee containing:

- employee_id: 301
- name: "Olivia Carter"
- department: "Engineering"
- monthly_salary: 3200.50
- full_time: True
- skills: ["Python", "SQL", "Problem Solving"]
- office_location: ("Tirana", "Albania")

Tasks:
1. Create the dictionary.
2. Print the employee's name.
3. Print the employee's second skill.
4. Add "Git" to the skills list.
5. Change the department to "Software Engineering".
6. Print the office location.
7. Print the number of skills.
"""


# ============================================================
# EXERCISE 7 — SERVER STATUS MONITOR
# Level: Intermediate
# ============================================================

"""
A company monitors the status of its computer servers.

Create a dictionary called server containing:

- server_name: "production-server-01"
- cpu_usage: 68.5
- memory_usage: 72.0
- server_online: True
- active_services: ["Website", "Database", "API"]

CPU usage means the percentage of processing capacity currently used.
Memory usage means the percentage of computer memory currently used.
An API (Application Programming Interface) is a way for software systems
to communicate with each other.

Tasks:
1. Create the dictionary.
2. Check whether cpu_usage is greater than 80.
3. Store the result in a Boolean variable called high_cpu_usage.
4. Check whether memory_usage is greater than 90.
5. Print both Boolean results.
6. Add "Email Service" to active_services.
7. Print the number of active services.
"""


# ============================================================
# EXERCISE 8 — CUSTOMER DATA CLEANING
# Level: Advanced
# ============================================================

"""
A customer database contains duplicate country names and
inconsistent email formatting.

Create these variables:

customer_countries = [
    "Albania",
    "Germany",
    "Albania",
    "Italy",
    "Germany",
    "France"
]

customer_email = "  SARAH@EXAMPLE.COM  "

Tasks:
1. Convert customer_countries into a set to remove duplicates.
2. Print the unique countries.
3. Convert customer_email to lowercase.
4. Remove unnecessary spaces from the beginning and end.
5. Store the cleaned email in a new variable.
6. Print the cleaned email.
7. Print the number of unique countries.

The strip() method removes spaces from the beginning and end of text.
"""


# ============================================================
# EXERCISE 9 — SAAS REVENUE DATA
# Level: Advanced
# ============================================================

"""
A SaaS (Software as a Service — software that customers access
through a subscription) company sells three subscription plans.

The company has:

Starter plan:
- 120 customers
- 9.99 per month

Professional plan:
- 75 customers
- 29.99 per month

Business plan:
- 25 customers
- 79.99 per month

MRR (Monthly Recurring Revenue — money a business expects to
receive each month from ongoing subscriptions) is calculated
by multiplying the number of customers by the monthly plan price.

Tasks:
1. Create a dictionary for each subscription plan.
2. Store the customer count and monthly price in each dictionary.
3. Calculate the MRR for each plan.
4. Calculate the total MRR (combined monthly subscription revenue).
5. Calculate the total number of customers.
6. Store the three plan names in a set.
7. Print a clear business report.

Do not hardcode the calculated totals.
Calculate them from the stored information.
"""


# ============================================================
# EXERCISE 10 — CUSTOMER AND ORDER DATA MANAGER
# Level: Advanced
# ============================================================

"""
Build a small customer and order data manager.

Create a customer dictionary with:

- customer_id: 9001
- name: "James Wilson"
- email: "james@example.com"
- account_active: True
- phone_number: None

Create an order dictionary with:

- order_id: 6001
- products: ["Keyboard", "Mouse", "Monitor"]
- prices: [59.99, 24.99, 189.99]
- quantities: [2, 1, 1]
- payment_completed: False

Tasks:
1. Create both dictionaries.
2. Print the customer's name and email.
3. Print the customer's phone number.
   If it is None, display "Phone number not provided".
4. Calculate the total order value.
   Each product price must be multiplied by its quantity.
5. Store the result in total_order_value.
6. Change payment_completed to True.
7. Print the order ID, products, total order value,
   and payment status.
8. Print the data type of total_order_value.

Important:
Do not simply add the product prices.
You must multiply each price by its corresponding quantity.
Use a loop (a programming structure that repeats instructions)
or calculate each product separately.
"""

