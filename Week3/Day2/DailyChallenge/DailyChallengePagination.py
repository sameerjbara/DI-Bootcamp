# Instructions: Pagination System

# 📄 What is Pagination?

# In web development, pagination helps break large lists into smaller, manageable chunks (pages), making it easier to navigate content like search results, product listings, or articles.

# Here’s a visual example:

# Page 1      Page 2      Page 3
# [a, b, c]   [d, e, f]   [g, h, i]


# Goal:

# Create a Pagination class that simulates a basic pagination system.



# Step 1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.


# Step 2: Implement the __init__ Method

# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Behavior:

# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.


# Step 3: Implement the get_visible_items() Method

# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.


# Step 4: Implement Navigation Methods

# These methods should help navigate through pages:

# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

# first_page()
# → Navigates to the first page.

# last_page()
# → Navigates to the last page.

# next_page()
# → Moves one page forward (if not already on the last page).

# previous_page()
# → Moves one page backward (if not already on the first page).

# 📝 Note:

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.


# Bonus

# Step 5: Add a Custom __str__() Method

# This magic method should return a string displaying the items on the current page, each on a new line.
# Example:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# print(str(p))
# # Output:
# # a
# # b
# # c
# # d


# Step 6: Test Your Code

# Use the following test cases:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)

# print(p.get_visible_items())
# # ['a', 'b', 'c', 'd']

# p.next_page()
# print(p.get_visible_items())
# # ['e', 'f', 'g', 'h']

# p.last_page()
# print(p.get_visible_items())
# # ['y', 'z']

# p.go_to_page(10)
# print(p.current_idx + 1)
# # Output: ValueError

# p.go_to_page(0)
# # Raises ValueError


# Bonus: upgrade your code by changing the return statement in a way that will allor you to concatenate methods like this:
# p.nextPage().nextPage().nextPage().getVisibleItems()
# output: [‘m’, ‘n’, ‘o’, ‘p’]



import math


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        if not isinstance(items, list):
            raise TypeError("items must be a list")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer")

        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # 0-based page index
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        # user gives 1-based page number
        if not isinstance(page_num, int):
            raise TypeError("page_num must be an int")

        if self.total_pages == 0:
            raise ValueError("No pages available (items list is empty).")

        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"page_num out of range. Valid: 1..{self.total_pages}")

        self.current_idx = page_num - 1
        return self  # allow chaining

    def first_page(self):
        if self.total_pages > 0:
            self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(str(x) for x in self.get_visible_items())


# -------------------- Tests --------------------
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())
    # ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())
    # ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())
    # ['y', 'z']

    try:
        p.go_to_page(10)
        print(p.current_idx + 1)
    except ValueError as e:
        print("ValueError:", e)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print("ValueError:", e)

    # Bonus chaining:
    p = Pagination(alphabetList, 4)
    print(p.next_page().next_page().next_page().get_visible_items())
    # ['m', 'n', 'o', 'p']

    # Bonus __str__ demo:
    p = Pagination(alphabetList, 4)
    print(str(p))
