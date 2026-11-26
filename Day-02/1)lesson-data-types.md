
# Day 02 — Data Types

## 1. What Are Data Types?

A data type tells Python what kind of information a value represents.

For example, a customer's name is text, the number of products in an order is a whole number, and the price of a product is usually a decimal number.

Python uses data types to understand how values should be stored and what operations can be performed with them.

Consider these examples:

```python
customer_name = "Alex Morgan"
order_quantity = 5
product_price = 49.99
payment_completed = True
```

These variables contain four different types of information.

Python provides several built-in data types. A built-in data type is a type that is already available in Python without installing anything.

The most important ones are:

- `str` — text (a sequence of characters).
- `int` — integer (a whole number without a decimal part).
- `float` — floating-point number (a number that can contain a decimal part).
- `bool` — Boolean value (a value that represents either True or False).
- `list` — list (an ordered collection of values that can be changed).
- `tuple` — tuple (an ordered collection of values that cannot be changed after creation).
- `set` — set (a collection that stores unique values and does not preserve a guaranteed order).
- `dict` — dictionary (a collection that stores information as key-value pairs).
- `NoneType` — the type of `None` (a special value that represents the absence of a value).

We will study each of them.

---

## 2. Strings — `str`

A string represents text.

Text can contain letters, numbers, spaces, and symbols.

You create a string by placing text inside quotation marks.

```python
customer_name = "Alex Morgan"
company_name = "Northstar Technologies"
email_address = "alex@example.com"
country = "Albania"
```

Python recognizes these values as strings because they are surrounded by quotation marks.

You can use either single or double quotation marks:

```python
first_name = "Alex"
last_name = 'Morgan'
```

Both are valid.

### Combining Strings

You can combine strings using the `+` operator.

This operation is called concatenation (joining text values together).

```python
first_name = "Alex"
last_name = "Morgan"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Alex Morgan
```

Notice that `" "` adds a space between the names.

### String Formatting

When building real applications, you often need to insert variable values into text.

Python provides f-strings (formatted strings that allow variables and expressions to be inserted directly into text).

```python
customer_name = "Alex Morgan"
subscription_plan = "Professional"

message = f"Customer {customer_name} is subscribed to the {subscription_plan} plan."

print(message)
```

Output:

```text
Customer Alex Morgan is subscribed to the Professional plan.
```

The letter `f` before the quotation marks tells Python that the string can contain expressions inside curly brackets.

### Useful String Operations

```python
company_name = "Northstar Technologies"

print(company_name.upper())
print(company_name.lower())
print(company_name.title())
print(len(company_name))
```

Output:

```text
NORTHSTAR TECHNOLOGIES
northstar technologies
Northstar Technologies
23
```

Explanation:

- `.upper()` converts all letters to uppercase.
- `.lower()` converts all letters to lowercase.
- `.title()` capitalizes the first letter of each word.
- `len()` returns the number of characters in the string.

These operations are useful when cleaning customer information or displaying text consistently.

---

## 3. Integers — `int`

An integer is a whole number without a decimal part.

Examples:

```python
customer_id = 1042
number_of_orders = 18
available_products = 250
employee_count = 35
```

Integers are useful for information such as:

- Number of customers.
- Number of orders.
- Product quantities.
- Employee counts.
- Database record numbers.

You can perform mathematical operations with integers.

```python
first_order_count = 120
second_order_count = 85

total_orders = first_order_count + second_order_count

print(total_orders)
```

Output:

```text
205
```

Other mathematical operations:

```python
print(20 + 5)   # Addition
print(20 - 5)   # Subtraction
print(20 * 5)   # Multiplication
print(20 / 5)   # Division
print(20 // 3)  # Floor division (division rounded down to a whole number)
print(20 % 3)   # Modulo (the remainder after division)
print(20 ** 3)  # Exponentiation (raising a number to a power)
```

Output:

```text
25
15
100
4.0
6
2
8000
```

An important detail: normal division with `/` returns a floating-point number, even when the result looks like a whole number.

---

## 4. Floating-Point Numbers — `float`

A float represents a number that can contain a decimal part.

Examples:

```python
product_price = 49.99
monthly_subscription = 19.99
tax_rate = 0.20
average_order_value = 125.75
```

Floats are commonly used for:

- Prices.
- Measurements.
- Percentages.
- Average values.
- Calculations involving decimal numbers.

Example:

```python
product_price = 49.99
quantity = 3

total_price = product_price * quantity

print(total_price)
```

Output:

```text
149.97
```

### Important: Floating-Point Precision

Computers do not always represent decimal numbers exactly when using floats.

For example:

```python
result = 0.1 + 0.2

print(result)
```

You may see:

```text
0.30000000000000004
```

This happens because many decimal fractions cannot be represented exactly in the computer's binary number system (the system that uses only 0 and 1).

For simple learning examples, floats are fine.

For financial applications that require exact decimal calculations, Python provides the `decimal` module (a built-in module for working with decimal numbers more accurately).

Example:

```python
from decimal import Decimal

price = Decimal("0.10")
tax = Decimal("0.20")

total = price + tax

print(total)
```

Output:

```text
0.30
```

For money calculations, use decimal values created from strings rather than directly from floats.

---

## 5. Booleans — `bool`

A Boolean represents one of two possible values:

- `True`
- `False`

Booleans are useful when a program needs to represent a condition or status.

Examples:

```python
account_active = True
payment_completed = False
email_verified = True
subscription_expired = False
```

Notice that `True` and `False` start with capital letters.

They are not strings. Do not place quotation marks around them.

Correct:

```python
payment_completed = True
```

Incorrect if you want a Boolean:

```python
payment_completed = "True"
```

The second example is a string because it contains quotation marks.

### Boolean Values From Comparisons

Python can create Boolean values by comparing information.

```python
account_balance = 500
required_balance = 300

has_sufficient_balance = account_balance >= required_balance

print(has_sufficient_balance)
```

Output:

```text
True
```

Comparison operators:

```python
print(10 == 10)  # Equal to
print(10 != 5)   # Not equal to
print(10 > 5)    # Greater than
print(10 < 5)    # Less than
print(10 >= 10)  # Greater than or equal to
print(5 <= 10)   # Less than or equal to
```

Each comparison produces either `True` or `False`.

---

## 6. Lists — `list`

A list stores multiple values in a single variable.

Lists are ordered (the values keep their positions) and mutable (the values can be changed after the list is created).

Example:

```python
product_categories = [
    "Electronics",
    "Software",
    "Accessories",
    "Office Equipment"
]
```

A list is useful when you need to store multiple related values.

### Accessing List Items

Each item has an index (a position number used to access an item).

Python starts counting indexes from zero.

```python
product_categories = [
    "Electronics",
    "Software",
    "Accessories"
]

print(product_categories[0])
print(product_categories[1])
print(product_categories[2])
```

Output:

```text
Electronics
Software
Accessories
```

You can also access the last item using `-1`.

```python
print(product_categories[-1])
```

Output:

```text
Accessories
```

### Changing List Items

```python
subscription_plans = [
    "Starter",
    "Professional",
    "Business"
]

subscription_plans[0] = "Basic"

print(subscription_plans)
```

Output:

```text
['Basic', 'Professional', 'Business']
```

### Adding and Removing Items

```python
customer_emails = [
    "alex@example.com",
    "sarah@example.com"
]

customer_emails.append("john@example.com")

print(customer_emails)
```

`.append()` adds a new item to the end of the list.

Remove an item:

```python
customer_emails.remove("sarah@example.com")

print(customer_emails)
```

Other useful list operations:

```python
print(len(customer_emails))
```

Returns the number of items.

```python
customer_emails.sort()
```

Sorts the items in ascending order.

```python
customer_emails.reverse()
```

Reverses the current order.

```python
customer_emails.clear()
```

Removes all items.

---

## 7. Tuples — `tuple`

A tuple is similar to a list, but its items cannot be changed after the tuple is created.

A tuple is useful when you want to keep a group of values together without changing their contents.

Example:

```python
company_location = (
    "Tirana",
    "Albania",
    "Europe"
)

print(company_location[0])
print(company_location[1])
```

Output:

```text
Tirana
Albania
```

You can read tuple items, but you cannot replace them.

This is valid:

```python
company_location = ("Tirana", "Albania")
print(company_location[0])
```

This causes an error:

```python
company_location[0] = "Durres"
```

Use a list when the collection needs to change. Use a tuple when the collection should remain unchanged.

---

## 8. Sets — `set`

A set stores unique values (values that do not appear more than once).

Example:

```python
registered_countries = {
    "Albania",
    "Germany",
    "Italy",
    "Albania"
}

print(registered_countries)
```

The repeated value `"Albania"` is stored only once.

Sets are useful when you need to remove duplicates or check whether a value exists in a collection.

Example:

```python
customer_tags = {
    "premium",
    "active",
    "verified"
}

customer_tags.add("enterprise")
customer_tags.discard("active")

print(customer_tags)
```

Important: sets do not guarantee a particular item order. Do not use indexes to access set items.

---

## 9. Dictionaries — `dict`

A dictionary stores information as key-value pairs.

A key is a name used to identify a piece of information. A value is the information associated with that key.

Dictionaries are extremely useful when building applications because they allow you to represent structured information.

Example:

```python
customer = {
    "customer_id": 1042,
    "name": "Alex Morgan",
    "email": "alex@example.com",
    "subscription": "Professional",
    "active": True
}
```

Each key describes a piece of customer information.

### Accessing Dictionary Values

```python
print(customer["name"])
print(customer["email"])
print(customer["subscription"])
```

Output:

```text
Alex Morgan
alex@example.com
Professional
```

### Changing Dictionary Values

```python
customer["subscription"] = "Business"
customer["active"] = False

print(customer)
```

### Adding New Information

```python
customer["country"] = "Albania"
customer["total_orders"] = 12
```

### Removing Information

```python
del customer["total_orders"]
```

### Using `.get()`

If a key does not exist, accessing it with square brackets can cause a `KeyError` (an error that occurs when a requested dictionary key is missing).

You can use `.get()` to safely request a value:

```python
customer = {
    "name": "Alex Morgan",
    "email": "alex@example.com"
}

phone_number = customer.get("phone", "Not provided")

print(phone_number)
```

Output:

```text
Not provided
```

This is useful when working with information that may be incomplete.

---

## 10. The None Value — `None`

`None` represents the absence of a value.

It is different from:

- `0` (the integer zero).
- `""` (an empty string).
- `False` (a Boolean value).

Example:

```python
customer_phone = None

print(customer_phone)
```

You might use `None` when a customer has not provided a phone number yet.

You can check whether a value is `None` using `is`.

```python
if customer_phone is None:
    print("Phone number has not been provided.")
```

The `if` statement runs its code only when its condition is True.

---

## 11. Checking Data Types With `type()`

Python provides the `type()` function to identify the data type of a value.

Example:

```python
customer_name = "Alex Morgan"
customer_id = 1042
monthly_price = 29.99
account_active = True

print(type(customer_name))
print(type(customer_id))
print(type(monthly_price))
print(type(account_active))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This is useful when checking data or finding mistakes in a program.

---

## 12. Type Conversion

Type conversion means changing a value from one data type to another.

Python provides several conversion functions:

- `str()` converts a value into text.
- `int()` converts a suitable value into an integer.
- `float()` converts a suitable value into a float.
- `bool()` converts a value into a Boolean.

### Converting an Integer Into a String

```python
customer_id = 1042

customer_id_text = str(customer_id)

print(customer_id_text)
print(type(customer_id_text))
```

### Converting Text Into an Integer

```python
number_of_orders = "25"

number_of_orders = int(number_of_orders)

print(number_of_orders + 5)
```

Output:

```text
30
```

Without conversion, Python cannot directly add the string `"25"` to the integer `5`.

### Converting Text Into a Float

```python
product_price = "49.99"

product_price = float(product_price)

print(product_price * 2)
```

### Important Conversion Errors

This works:

```python
quantity = int("25")
```

This causes a `ValueError` (an error that occurs when Python receives a value that cannot be converted as requested):

```python
quantity = int("twenty-five")
```

Always check whether incoming information has the expected format before converting it.

---

## 13. Working With User Input

The `input()` function allows a program to receive information from a user.

Important: `input()` always returns a string, even when the user enters a number.

Example:

```python
customer_name = input("Enter customer name: ")

print(f"Customer: {customer_name}")
```

If you want a number, you must convert the input.

```python
number_of_products = int(input("Enter number of products: "))

print(number_of_products * 2)
```

For decimal numbers:

```python
monthly_price = float(input("Enter monthly price: "))

print(monthly_price)
```

In real applications, user input should be checked before it is used. This helps prevent invalid information from breaking the program.

---

## 14. Choosing the Correct Data Type

Consider a customer management application.

```python
customer = {
    "customer_id": 1042,
    "name": "Alex Morgan",
    "email": "alex@example.com",
    "monthly_price": 29.99,
    "account_active": True,
    "subscription_features": [
        "Analytics",
        "Reports",
        "Team Access"
    ],
    "registered_country": "Albania",
    "support_phone": None
}
```

Why are these data types appropriate?

- `customer_id` is an integer because it represents a whole-number identifier.
- `name` is a string because it contains text.
- `email` is a string because it contains text.
- `monthly_price` is a float for this learning example because it contains a decimal value.
- `account_active` is a Boolean because the account is either active or inactive.
- `subscription_features` is a list because it contains multiple features.
- `registered_country` is a string because it contains text.
- `support_phone` is `None` because no phone number has been provided.

Choosing the correct data type makes programs easier to understand and work with.

---

## 15. Mini Project — Customer and Order Data Manager

Now we will combine several data types in one practical example.

The goal is to create a small program that stores customer information and calculates an order total.

```python
customer = {
    "customer_id": 2045,
    "name": "Jordan Smith",
    "email": "jordan@example.com",
    "account_active": True
}

order = {
    "order_id": 5001,
    "products": [
        "Wireless Keyboard",
        "Wireless Mouse",
        "Laptop Stand"
    ],
    "product_prices": [49.99, 24.99, 35.00],
    "paid": False
}

total_price = sum(order["product_prices"])

print("CUSTOMER INFORMATION")
print("--------------------")
print(f"Customer ID: {customer['customer_id']}")
print(f"Name: {customer['name']}")
print(f"Email: {customer['email']}")
print(f"Account Active: {customer['account_active']}")

print("\nORDER INFORMATION")
print("-----------------")
print(f"Order ID: {order['order_id']}")
print(f"Products: {order['products']}")
print(f"Total Price: ${total_price:.2f}")
print(f"Payment Completed: {order['paid']}")
```

Explanation:

- The customer information is stored in a dictionary.
- The order information is stored in another dictionary.
- The product names are stored in a list.
- The prices are stored in another list.
- `sum()` calculates the sum of all prices.
- `:.2f` formats a number to display exactly two decimal places.

This is a simple example of how different data types work together inside a real application.

---

## 16. Common Mistakes

### Mistake 1 — Mixing Strings and Numbers

Incorrect:

```python
price = "49.99"
quantity = 3

total = price * quantity
```

This repeats the text instead of calculating a numeric total.

Correct:

```python
price = float("49.99")
quantity = 3

total = price * quantity
```

### Mistake 2 — Using the Wrong Dictionary Key

Incorrect:

```python
customer = {"name": "Alex"}

print(customer["email"])
```

This causes a `KeyError` because the key does not exist.

Safer:

```python
print(customer.get("email", "Not provided"))
```

### Mistake 3 — Forgetting That Indexes Start at Zero

```python
products = ["Keyboard", "Mouse", "Monitor"]

print(products[0])  # Keyboard
print(products[1])  # Mouse
print(products[2])  # Monitor
```

There is no item at index `3`.

### Mistake 4 — Confusing a String With a Boolean

```python
account_active = "False"
```

This is text, not a Boolean.

Correct:

```python
account_active = False
```

---

## 17. Day 2 Summary

Today you learned:

1. What data types are and why they matter.
2. How to use strings, integers, floats and Booleans.
3. How to store multiple values using lists, tuples and sets.
4. How to organize structured information using dictionaries.
5. How to represent missing information using `None`.
6. How to inspect data types with `type()`.
7. How to convert values using `str()`, `int()`, `float()` and `bool()`.
8. How to receive user input using `input()`.
9. How to combine different data types in a practical application.

The next step is to complete all 10 exercises without looking at the solutions first.
