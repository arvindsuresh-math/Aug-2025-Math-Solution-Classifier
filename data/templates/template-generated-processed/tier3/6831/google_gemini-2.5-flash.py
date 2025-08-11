def solve():
    """Index: 6831.
    Returns: the number of jellybeans the fourth student guessed.
    """
    # L1
    first_guess = 100 # The first thinks it contains 100 jellybeans.
    second_guess_multiplier = 8 # The second says there are 8 times as many.
    second_guess = second_guess_multiplier * first_guess

    # L2
    third_guess_difference = 200 # The third guesses 200 less than the third.
    third_guess = second_guess - third_guess_difference

    # L3
    sum_of_first_three_guesses = first_guess + second_guess + third_guess

    # L4
    number_of_guesses_for_average = 3 # WK
    average_of_first_three_guesses = sum_of_first_three_guesses / number_of_guesses_for_average

    # L5
    fourth_guess_addition = 25 # and then adds 25 to it.
    fourth_guess = average_of_first_three_guesses + fourth_guess_addition

    # FA
    answer = fourth_guess
    return answer