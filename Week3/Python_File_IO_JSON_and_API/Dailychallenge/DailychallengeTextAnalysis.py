# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.



# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).


# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.


# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.


# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.


# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.


# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.


# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.


# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.


import string
import re


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return None
        return count

    def most_common_word(self):
        words = self.text.split()
        freq = {}

        for w in words:
            freq[w] = freq.get(w, 0) + 1

        most_common = max(freq, key=freq.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return cls(content)


class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "are", "was", "were", "in", "on", "at", "to",
            "and", "or", "but", "of", "for", "with", "as", "by", "this", "that",
            "it", "be", "from", "have", "has", "had", "i", "you", "he", "she",
            "they", "we", "my", "your", "his", "her", "their", "our"
        }

        words = self.text.split()
        filtered = [w for w in words if w.lower() not in stop_words]
        self.text = " ".join(filtered)
        return self.text

    def remove_special_characters(self):
        self.text = re.sub(r"[^a-zA-Z0-9\s]", "", self.text)
        return self.text


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    t = Text("hello hello world world world")
    print(t.word_frequency("world"))      # 3
    print(t.most_common_word())           # world
    print(t.unique_words())               # ['hello', 'world'] (order may vary)

    tm = TextModification("Hello!!! This is, a test... #Python @2026")
    print(tm.remove_punctuation())        # Hello This is a test Python 2026
    print(tm.remove_stop_words())         # Hello test Python 2026
    print(tm.remove_special_characters()) # Hello test Python 2026
