
# DAY 01 : PYTHON VARIABLES

**Course:** Python from Zero to Advanced  
**Module:** 01 : Variables  

---

# 1. What Are Variables?

A variable is a name that refers to a value stored in a Python program.
Variables allow software applications to store, access and update information.
Almost every business application uses variables.

For example, an e-commerce application needs to store customer information, product prices, inventory quantities and order details.

```python
customer_name = "Michael Anderson"
product_price = 149.99
available_stock = 45
is_payment_completed = True
```

Let's understand every line.

`customer_name` is the variable name.

`=` is the assignment operator. It assigns the value on the right to the name on the left.

`"Michael Anderson"` is a string containing text.

`product_price` stores the product price.

`available_stock` stores the number of available products.

`is_payment_completed` stores a Boolean value.

The program can use these variables whenever it needs the information.

# 2. Why Do Real Applications Need Variables?

Imagine building an online store.

A customer places an order for three products.

The application needs to remember:

- Who placed the order.
- Which product was purchased.
- How much each product costs.
- How many units were purchased.
- Whether payment was completed.

Without variables, the application would have no practical way to manage this information during execution.

Example:

```python
customer_name = "Sarah Williams"
product_name = "Wireless Headphones"
unit_price = 89.99
quantity = 3
payment_completed = True
```

We can calculate the order subtotal:

```python
order_subtotal = unit_price * quantity

print(order_subtotal)
```

Output:

```text
269.97
```

The calculation uses existing variables instead of repeating the values manually.

This is one of the main reasons variables are essential in software development.

# 3. Assignment and Reassignment

Assignment creates a variable binding.

```python
available_stock = 120
```

Reassignment changes the value associated with the variable name.

```python
available_stock = 95
```

The variable now refers to the new value.

Example from warehouse management:

```python
available_stock = 120
units_sold = 25

available_stock = available_stock - units_sold

print(available_stock)
```

Output:

```text
95
```

Python evaluates the right side first and then assigns the result.

A shorter version is:

```python
available_stock -= units_sold
```

This is called augmented assignment.

Other examples:

```python
monthly_revenue = 5000
monthly_revenue += 1200

failed_login_attempts = 2
failed_login_attempts += 1

remaining_credits = 100
remaining_credits -= 15
```

# 4. Basic Data Types

Variables can refer to different kinds of values.

## String (str)

A string represents text.

```python
company_name = "Northstar Technologies"
customer_email = "customer@example.com"
```

Strings are used for names, descriptions, emails, addresses, and other text-based information.

## Integer (int)

An integer represents a whole number.

```python
employee_count = 85
available_products = 240
total_orders = 1250
```

Integers are useful for quantities and counters.

## Float (float)

A float represents a floating-point number.

```python
product_price = 149.99
average_rating = 4.7
conversion_rate = 0.035
```

Floats are commonly used for measurements and approximate decimal calculations.

For financial applications, use Decimal rather than relying on float for exact monetary arithmetic. We will study this later.

## Boolean (bool)

A Boolean represents one of two values:

`True` or `False`.

```python
is_account_active = True
payment_completed = False
is_email_verified = True
```

Boolean values are essential for representing conditions and application states.

# 5. Dynamic Typing

Python is dynamically typed.

This means you do not need to declare the variable's type before assigning a value.

Example:

```python
account_status = "trial"
account_status = "active"
```

Python allows a variable name to refer to values of different types.

```python
account_value = 100
account_value = "One hundred"
```

However, changing types unnecessarily can make business applications harder to maintain.

Prefer predictable and consistent data.

Example:

```python
account_balance = 100.00
account_status = "active"
```

You can inspect a value's type using `type()`.

```python
customer_name = "Sarah Williams"
employee_count = 85
monthly_revenue = 12500.50
is_verified = True

print(type(customer_name))
print(type(employee_count))
print(type(monthly_revenue))
print(type(is_verified))
```

You can also verify a type using `isinstance()`.

```python
employee_count = 85

print(isinstance(employee_count, int))
```

Output:

```text
True
```

# 6. Professional Variable Naming

Good variable names communicate what information is stored.

Professional developers prefer descriptive names.

Good examples:

```python
customer_email = "sarah@example.com"
monthly_revenue = 25000
subscription_status = "active"
available_inventory = 450
```

Bad examples:

```python
x = "sarah@example.com"
a = 25000
data = "active"
thing = 450
```

Python convention uses snake_case.

Snake case separates words with underscores.

Examples:

```python
customer_name = "Sarah"
order_id = 10452
is_subscription_active = True
total_monthly_revenue = 15000
```

Variable naming rules:

1. Names cannot start with a number.
2. Names can contain letters, numbers, and underscores.
3. Names are case-sensitive.
4. Reserved Python keywords cannot be used as variable names.
5. Use descriptive names that communicate the purpose of the value.

# 7. Using Variables in Business Calculations

Consider a SaaS company selling monthly subscriptions.

The company has 240 customers.

Each customer pays 29.99 per month.

```python
active_customers = 240
monthly_subscription_price = 29.99

monthly_recurring_revenue = (
    active_customers * monthly_subscription_price
)

print(monthly_recurring_revenue)
```

Output:

```text
7197.6
```

The result represents simplified monthly recurring revenue.

This example demonstrates how variables can represent real business metrics.

The same approach is used in reporting systems, dashboards, financial software and business applications.

# 8. Multiple Assignment

Python allows multiple variables to receive values in one statement.

```python
customer_name, subscription_plan, account_age = (
    "Sarah Williams",
    "Enterprise",
    420
)
```

This is called multiple assignment or unpacking.

You can also assign the same initial value to multiple variables:

```python
service_a_enabled = service_b_enabled = False
```

Use this when the variables genuinely share the same initial value.

# 9. Variables and Object References

A variable name refers to an object.

Two different variable names can refer to the same object.

Consider:

```python
primary_account = {"status": "active"}

backup_account = primary_account

backup_account["status"] = "suspended"

print(primary_account)
```

Output:

```text
{'status': 'suspended'}
```

Both names refer to the same dictionary.

Changing the dictionary through one name changes the object that the other name also references.

Compare this with integers:

```python
first_count = 10
second_count = first_count

second_count = 20

print(first_count)
print(second_count)
```

Output:

```text
10
20
```

Integers are immutable. Reassigning one variable does not change the value associated with the other variable.

Remember:

- Assignment binds a name to an object.
- Immutable objects cannot be changed in place.
- Mutable objects can be changed in place.
- Multiple names can refer to the same object.

# 10. Common Errors

## NameError

A variable is used before it has been defined.

```python
print(customer_email)
```

Fix:

```python
customer_email = "customer@example.com"

print(customer_email)
```

## Case sensitivity

Python treats uppercase and lowercase letters differently.

```python
order_total = 250

# print(Order_Total)
```

`order_total` and `Order_Total` are different names.

## TypeError

Python cannot perform an operation between incompatible types.

```python
account_balance = 100
currency = "EUR"

# print(account_balance + currency)
```

A number cannot be directly added to a string.

For display:

```python
print(f"{account_balance} {currency}")
```

# 11. Practical Mini Project — SaaS Account Summary

Build a small account summary using variables.

```python
customer_name = "Sarah Williams"
company_name = "Starry Analytics"
subscription_plan = "Business"

licensed_users = 18
price_per_user = 24.00

is_account_active = True

monthly_subscription_value = (
    licensed_users * price_per_user
)

print("CUSTOMER ACCOUNT")
print("----------------")
print(f"Customer: {customer_name}")
print(f"Company: {company_name}")
print(f"Plan: {subscription_plan}")
print(f"Licensed users: {licensed_users}")
print(f"Monthly value: {monthly_subscription_value:.2f}")
print(f"Account active: {is_account_active}")
```

Your task is to modify the data and observe how the output changes.

Do not modify the calculation itself.

# 12. Day 1 Mastery Checklist

Before moving to Day 2, make sure you can explain:

- What a variable is.
- How assignment works.
- How reassignment works.
- The difference between str, int, float, and bool.
- What dynamic typing means.
- How type() works.
- How isinstance() works.
- Why snake_case is used.
- How to calculate values using variables.
- How multiple assignment works.
- What object references are.
- The difference between mutable and immutable objects.
- How to identify NameError and TypeError.

Completion standard:

You should be able to build the SaaS account summary independently and explain every line of code.




