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
    butter_left_after_two = total_butter - butter_used_first_two # eval: 3.0 = 10 - 7.0

    #: L5
    butter_sugar_cookies = butter_left_after_two / 3 # eval: 1.0 = 3.0 / 3

    #: L6
    butter_left_final = butter_left_after_two + butter_sugar_cookies # eval: 4.0 = 3.0 + 1.0

    #: FA
    answer = butter_left_final
    return answer # eval: return 4.0
