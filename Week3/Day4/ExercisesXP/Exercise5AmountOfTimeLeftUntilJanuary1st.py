# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

# Step 2: Get the current date and time

# Step 3: Create a datetime object for January 1st of the next year

# Step 4: Calculate the time difference

# Step 5: Display the time difference



import datetime

def time_until_jan_1():
    now = datetime.datetime.now()
    next_year = now.year + 1
    jan_1 = datetime.datetime(next_year, 1, 1)

    diff = jan_1 - now
    print("Time left until Jan 1st:", diff)

time_until_jan_1()
