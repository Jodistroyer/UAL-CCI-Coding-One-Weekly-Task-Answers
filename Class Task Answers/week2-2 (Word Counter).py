paragraph = "the quick brown fox jumps over the lazy dog"

# Initialize a dictionary to store counts for each letter
letter_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

# Iterate through the characters in the paragraph
for char in paragraph:
    # Check if the character is a lowercase alphabet letter
    if 'a' <= char <= 'z':
        # Increment the count for that letter in the dictionary
        letter_counts[char] += 1

# Print the counts for each letter
for letter, count in letter_counts.items():
    print(f"{letter}: {count}", end=", ")