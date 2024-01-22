import Levenshtein

# List of known words
known_words = ["apple", "banana", "cherry", "orange", "grape", "pear"]

def spell_checker(word):
    if word in known_words:
        return f"{word} is spelled correctly."

    # Find the word with the smallest Levenshtein distance
    closest_word = min(known_words, key=lambda x: Levenshtein.distance(word, x))

    return f"Did you mean '{closest_word}' instead of '{word}'?"

# Test the spell checker
word_to_check = input("Enter a word: ")
result = spell_checker(word_to_check)
print(result)