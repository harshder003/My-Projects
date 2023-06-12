import nltk
from autocorrect import Speller

def autospell(text):
    spell = Speller(lang='en')
    tokens = nltk.word_tokenize(text)
    corrected_tokens = [spell(w) for w in tokens]
    return " ".join(corrected_tokens)

# Example usage
input_sentence = input("Enter a sentence: ")
corrected_sentence = autospell(input_sentence)
print(corrected_sentence)
