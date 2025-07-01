def solve(
    total_butter: int = 10  # Liza bought 10 kilograms of butter
):
    """Index: 57.
    Returns: the kilograms of butter left after making three kinds of cookies.
    """

    #: L1
    butter_chocolate_chip = total_butter / 2 # eval: 5.0 = 10 / 2

    #: L2
    butter_peanut_butter = total_butter / 5 # eval: 2.0 = 10 / 5

    #: L3
    butter_used_first_two = butter_chocolate_chip + butter_peanut_butter # eval: 7.0 = 5.0 + 2.0

    #: L4

    #: L5
    butter_sugar_cookies = total_butter / 3 # eval: 3.3333333333333335 = 10 / 3

    #: L6
    butter_left_final = total_butter - butter_sugar_cookies # eval: 6.666666666666666 = 10 - 3.3333333333333335

    #: FA
    answer = butter_left_final
    return answer # eval: return 6.666666666666666
