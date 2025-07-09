def solve_57():
    """
    Calculates the amount of butter left after making three kinds of cookies.

    Liza starts with 10 kg of butter.
    She uses one-half for chocolate chip cookies.
    She uses one-fifth for peanut butter cookies.
    She uses one-third of the remaining butter for sugar cookies.
    """
    total_butter_kg = 10

    # L1: Calculate butter used for chocolate chip cookies
    butter_for_chocolate_chip_kg = total_butter_kg / 2

    # L2: Calculate butter used for peanut butter cookies
    butter_for_peanut_butter_kg = total_butter_kg / 5

    # L3: Calculate total butter used for the first two types of cookies
    butter_used_first_two_types_kg = butter_for_chocolate_chip_kg + butter_for_peanut_butter_kg

    # L4: Calculate butter remaining after the first two types of cookies
    remaining_butter_after_first_two_kg = total_butter_kg - butter_used_first_two_types_kg

    # L5: Calculate butter used for sugar cookies (one-third of the remaining butter)
    butter_for_sugar_cookies_kg = remaining_butter_after_first_two_kg / 3

    # L6: Calculate the final amount of butter left
    final_butter_left_kg = remaining_butter_after_first_two_kg - butter_for_sugar_cookies_kg

    return final_butter_left_kg