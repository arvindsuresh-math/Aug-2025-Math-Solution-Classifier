def solve(
    total_butter: int = 10  # Liza bought 10 kilograms of butter
):
    """Index: 57.
    Returns: the kilograms of butter left after making three kinds of cookies.
    """

    #: L1
    butter_chocolate_chip = total_butter / 2

    #: L2
    butter_peanut_butter = total_butter / 5

    #: L3
    butter_used_first_two = butter_chocolate_chip + butter_peanut_butter

    #: L4

    #: L5
    butter_sugar_cookies = total_butter / 3

    #: L6
    butter_left_final = total_butter - butter_sugar_cookies

    #: FA
    answer = butter_left_final
    return answer