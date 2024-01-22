def pigify(sentence):
    words = sentence.split()
    piglatin_words = [word + "ay" for word in words]
    return ' '.join(piglatin_words)

input_sentence = input("Enter a sentence: ")
piglatin_sentence = pigify(input_sentence)
print("Piggify:", piglatin_sentence)

