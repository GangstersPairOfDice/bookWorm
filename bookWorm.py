def bookWorm(text, n):
    
    words = text.split() # Splits the string into individual words
    
    rows = [words[i:i+n] for i in range(0, len(words), n)]  # Divide the words into rows of length n
    
    for i, row in enumerate(rows):
        if i % 2 == 0:
            print(' '.join(row))  # Print the normal order of words for even-numbered rows
        else:
            print(' '.join(reversed(row)))  # Print the reversed order of words for odd-numbered rows
