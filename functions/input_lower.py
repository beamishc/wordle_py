def input_lower(string, current_attempt, max_attempts):
    '''This function takes a string as an argument and returns the user's input as a lowercase string.'''

    response_dict = {
    'is_alpha': "Please enter a valid input. This input must be a string.    ",
    'is_five': "Please enter a valid input. This input must be a 5 letter word.    ",
    'incorrect': f"You have {max_attempts - current_attempt} attempts remaining.    ",
}
    return input(response_dict[string]).lower()
