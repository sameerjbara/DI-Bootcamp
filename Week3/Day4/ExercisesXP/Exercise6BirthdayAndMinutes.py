# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.




import datetime

def minutes_lived(birthdate_str):
    # format example: "2000-05-10"
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()

    diff_seconds = (now - birthdate).total_seconds()
    diff_minutes = int(diff_seconds // 60)

    print(f"You lived about {diff_minutes} minutes.")

minutes_lived("2000-05-10")
