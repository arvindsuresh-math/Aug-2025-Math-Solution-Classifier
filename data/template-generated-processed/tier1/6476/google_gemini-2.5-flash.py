def solve():
    """Index: 6476.
    Returns: the total amount Geoff will spend on sneakers over three days.
    """
    # L1
    spent_today = 60 # spent $60
    multiplier_tomorrow = 4 # spend 4 times as much
    spent_tomorrow = spent_today * multiplier_tomorrow

    # L2
    multiplier_wednesday = 5 # spend 5 times as much
    spent_wednesday = spent_today * multiplier_wednesday

    # L3
    total_spent = spent_today + spent_tomorrow + spent_wednesday

    # FA
    answer = total_spent
    return answer