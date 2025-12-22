# Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.



# Initial Data:


# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }


# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
# Calculate the class average (the average of all students’ averages) and print it.
# Print the name of each student, their average grade, and their letter grade.
# Hints:
# Use loops to iterate through the student_grades dictionary.
# You may use sum() and len() functions to help calculate averages.
# Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.


student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}

for student, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[student] = avg

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"

    student_letter_grades[student] = letter


class_average = sum(student_averages.values()) / len(student_averages)


for student in student_averages:
    print(f"{student}: Average = {student_averages[student]:.2f}, Grade = {student_letter_grades[student]}")

print(f"\nClass Average: {class_average:.2f}")



# Exercise 2 : Advanced Data Manipulation and Analysis
# Instructions
# In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.



# sales_data = [
#     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
#     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
#     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
#     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
#     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
#     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
#     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
# ]


# Tasks:
# Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

# Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

# Sales Data Enhancement:

# Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.
# High-Value Transactions:

# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.
# Customer Loyalty Identification:

# Identify any customer who has made more than one purchase, suggesting potential loyalty.
# Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.
# Bonus: Insights and Analysis:

# Calculate the average transaction value for each product category.
# Identify the most popular product based on the quantity sold.
# Provide insights into how these analyses could inform the company’s marketing strategies.


sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]


product_sales = {}

for sale in sales_data:
    product = sale["product"]
    revenue = sale["price"] * sale["quantity"]

    product_sales[product] = product_sales.get(product, 0) + revenue



customer_spending = {}

for sale in sales_data:
    customer = sale["customer_id"]
    total = sale["price"] * sale["quantity"]

    customer_spending[customer] = customer_spending.get(customer, 0) + total


for sale in sales_data:
    sale["total_price"] = sale["price"] * sale["quantity"]


high_value_transactions = [
    sale for sale in sales_data if sale["total_price"] > 500
]

high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)



purchase_count = {}

for sale in sales_data:
    customer = sale["customer_id"]
    purchase_count[customer] = purchase_count.get(customer, 0) + 1

loyal_customers = [cid for cid, count in purchase_count.items() if count > 1]


product_totals = {}
product_counts = {}

for sale in sales_data:
    product = sale["product"]
    total = sale["total_price"]

    product_totals[product] = product_totals.get(product, 0) + total
    product_counts[product] = product_counts.get(product, 0) + 1

average_transaction = {
    product: product_totals[product] / product_counts[product]
    for product in product_totals
}



product_quantity = {}

for sale in sales_data:
    product = sale["product"]
    product_quantity[product] = product_quantity.get(product, 0) + sale["quantity"]

most_popular_product = max(product_quantity, key=product_quantity.get)
