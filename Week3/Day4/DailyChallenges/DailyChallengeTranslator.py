# Instructions :
# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module. Take a look at the googletrans module.



# To install googletrans, you should use this command:

# pip install googletrans==4.0.0-rc1



from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translator = Translator()

translations = {}

for word in french_words:
    translated = translator.translate(word, src="fr", dest="en")
    translations[word] = translated.text

print(translations)
