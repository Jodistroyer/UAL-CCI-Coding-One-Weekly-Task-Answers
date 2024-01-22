def caesar_cipher(text, shift):
    # Define the original alphabet used for character substitution.
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Create an empty string to store the encrypted text.
    encrypted_text = ''
    
    # Iterate through each character in the input text.
    for char in text:
        # Check if the character is an alphabetic character.
        if char.isalpha():
            # Find the character's position in the alphabet.
            char_index = alphabet.index(char)
            
            # Apply the Caesar cipher shift and wrap around if needed.
            shifted_index = (char_index + shift) % 26
            
            # Use the shifted index to get the new character.
            shifted_char = alphabet[shifted_index]
            
            # Append the shifted character to the encrypted text.
            encrypted_text += shifted_char
        else:
            # If the character is not alphabetic, keep it unchanged.
            encrypted_text += char

    # Return the encrypted text.
    return encrypted_text

# Example usage:
text = "Hello, World!"
shift = 4
encrypted_text = caesar_cipher(text, shift)

# Print the original text and the encrypted text.
print("Original text:", text)
print("Encrypted text:", encrypted_text)