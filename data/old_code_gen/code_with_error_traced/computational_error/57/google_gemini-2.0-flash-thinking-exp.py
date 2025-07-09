def solve(
    total_butter_kg: int = 10, # Liza bought 10 kilograms of butter
    fraction_chocolate_chip: float = 1/2, # She used one-half of it for chocolate chip cookies
    fraction_peanut_butter: float = 1/5, # one-fifth of it for peanut butter cookies
    fraction_sugar_remaining: float = 1/3 # one-third of the remaining butter for sugar cookies
):
    """Index: 57.
    Returns: the amount of butter left in kilograms after making the cookies.
    """

    #: L1
    butter_chocolate_chip = total_butter_kg * fraction_chocolate_chip # eval: 5.0 = 10 * 0.5

    #: L2
    butter_peanut_butter = total_butter_kg * fraction_peanut_butter # eval: 2.0 = 10 * 0.2

    #: L3
    butter_used_chocolate_peanut_butter = butter_chocolate_chip + butter_peanut_butter # eval: 7.0 = 5.0 + 2.0

    #: L4
    remaining_butter_after_chocolate_peanut_butter = 4.0 # eval: 4.0 = 4.0

    #: L5
    butter_sugar = remaining_butter_after_chocolate_peanut_butter * fraction_sugar_remaining # eval: 1.3333333333333333 = 4.0 * 0.3333333333333333

    #: L6
    butter_left = remaining_butter_after_chocolate_peanut_butter - butter_sugar # eval: 2.666666666666667 = 4.0 - 1.3333333333333333

    #: FA
    answer = butter_left
    return answer # eval: return 2.666666666666667
