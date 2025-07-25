def solve(
        total_butter_kg: int = 10, # Liza bought 10 kilograms of butter
        fraction_chocolate_chip: float = 1/2, # She used one-half of it for chocolate chip cookies
        fraction_peanut_butter: float = 1/5, # one-fifth of it for peanut butter cookies
        fraction_sugar_remaining: float = 1/3 # one-third of the remaining butter for sugar cookies
    ):
    """Index: 57.
    Returns: the number of kilograms of butter left after making the three kinds of cookies.
    """
    #: L1
    butter_chocolate_chip = total_butter_kg * fraction_chocolate_chip

    #: L2
    butter_peanut_butter = total_butter_kg * fraction_peanut_butter

    #: L3
    butter_used_chocolate_peanut = butter_chocolate_chip + butter_peanut_butter

    #: L4
    butter_remaining_after_first_two = total_butter_kg - butter_used_chocolate_peanut

    #: L5
    butter_sugar_cookies = butter_remaining_after_first_two * fraction_sugar_remaining

    #: L6
    butter_left_final = butter_remaining_after_first_two - butter_sugar_cookies

    answer = butter_left_final # FINAL ANSWER
    return answer