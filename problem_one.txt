def reverse_word(word):
    return word[::-1]

def scramble_note(note):
    words = note.split()
    reversed_words = reversed(words)  # Reversed the order of words
    scrambled_words = [reverse_word(word) for word in reversed_words]
    scrambled_note = ' '.join(scrambled_words)
    return scrambled_note

# Get user input for the note to be scrambled
note = input("Enter the note you want to scramble: ")

# Call the function to scramble the note
scrambled_note = scramble_note(note)

# Print the scrambled note
print(scrambled_note)
