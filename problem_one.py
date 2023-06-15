def reverse_word(word):
    return word[::-1]  # Returns the reversed word

def scramble_note(note):
    # Split the note into words
    words = note.split()
    # Reverse the order of words
    reversed_words = words[::-1]
    # Reverse each word
    scrambled_words = [reverse_word(word) for word in reversed_words]
    # Join the scrambled words back into a string
    scrambled_note = ' '.join(scrambled_words)
    return scrambled_note

# Get user input for the note to be scrambled
note = input("Enter the note you want to scramble: ")

# Call the function to scramble the note
scrambled_note = scramble_note(note)

# Print the scrambled note
print(scrambled_note)