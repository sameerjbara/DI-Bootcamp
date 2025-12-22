# Reverse the Sentence
# Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You


sentence = "You have entered a wrong domain"

words = sentence.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)
print(result)
