def check_chars(guess, target_word, correct, misplaced, incorrect):
    '''Check the characters of the guess against the target word and update the correct, misplaced, and incorrect characters.'''
    # Iterate through the guess and compare to target word
    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            correct[i] = letter
            # Remove from misplaced if now in correct
            if letter in misplaced:
                misplaced.remove(letter)
        elif letter in target_word:
            # Add to misplaced if not already in correct or misplaced
            if letter not in correct and letter not in misplaced:
                misplaced.append(letter)
        else:
            incorrect.append(letter)
    return correct, misplaced, incorrect
