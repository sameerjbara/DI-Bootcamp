# Exercise 5: Longest word without a specific character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.



longest = ""
while True:
    s = input("Sentence: ")
    if "a" in s.lower(): continue
    if len(s) > len(longest):
        longest = s
        print("Congrats!")
