def count_occurrence(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


# Examples
string1 = "Programming is cool!"
char1 = "o"
print(count_occurrence(string1, char1))  # Output: 3

string2 = "This is a great example"
char2 = "y"
print(count_occurrence(string2, char2))  # Output: 0
