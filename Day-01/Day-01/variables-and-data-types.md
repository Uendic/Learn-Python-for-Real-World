# Day 1: Variables and Data Types in Real Software and Business

Welcome to Day 1. When building a software product, mobile app or online business, your code needs a reliable place to store important data. Variables and data types are the fundamental containers that allow backend systems to remember customer details, pricing tiers, and system states.

## 1. Variables
A variable is a named container stored in computer memory that holds a specific piece of information. You create a variable by giving it a clear name and assigning a value to it using the equals sign. For example, when a new customer creates an account on your platform, your system saves their username like this:

    customer_handle = "eni_founder"

## 2. Strings (`str`)
Strings represent text data and they must always be enclosed inside quotation marks. In real business applications, strings are used to store customer email addresses, company names, support messages and subscription plan titles:

    company_name = "Nexa Cloud"
    subscription_plan = "Enterprise"

## 3. Integers (`int`)
Integers represent whole numbers without any decimal points. Software systems rely on integers to count discrete items that cannot be split into fractions, such as total active users, seats purchased in a team plan and remaining API request credits etc:

    active_seats = 15
    monthly_credits = 5000

## 4. Floats (`float`)
Floats are numbers that contain decimal points. Whenever your application handles financial transactions, subscription billing, tax rates or customer satisfaction scores, you use floats to keep exact numerical precision:

    monthly_revenue = 249.99
    customer_rating = 4.8

## 5. Booleans (`bool`)
Booleans represent a binary logical state that can only evaluate to either True or False. Behind the scenes, every software application uses booleans to control feature access, check if an invoice has been paid or verify whether a user's free trial is still active:

    is_paid_subscriber = True
    trial_expired = False

## 6. The Print Function (`print()`)
The print function outputs data directly to your terminal screen. Developers use print statements every single day to inspect live data, log system events and also verify that business logic works correctly before deploying code to production:

    print("Active Company:", company_name)

---

## Daily Practice Exercise
Write clean Python code to solve each business scenario below. 

1. Store a new client's company name in a string variable called `client_name`.
2. Store the number of software licenses they bought in an integer variable called `licenses_purchased`.
3. Store the exact price per license in a float variable called `price_per_license`.
4. Store whether their payment was successfully confirmed in a boolean variable called `payment_confirmed`.
5. Store their primary contact email in a string variable called `billing_email`.
6. Use the `print()` function to display a clean account summary for this business client in your terminal.



