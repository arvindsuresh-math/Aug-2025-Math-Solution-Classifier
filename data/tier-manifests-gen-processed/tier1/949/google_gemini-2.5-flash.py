def solve():
    """Index: 949.
    Returns: Yola's weight 2 years ago.
    """
    # L1
    yola_current_weight = 220 # currently weighs 220 pounds
    wanda_more_than_yola_current = 30 # weighs 30 pounds more than Yola currently
    wanda_current_weight = yola_current_weight + wanda_more_than_yola_current

    # L2
    wanda_more_than_yola_two_years_ago = 80 # weighs 80 pounds more than Yola did 2 years ago
    yola_weight_two_years_ago = wanda_current_weight - wanda_more_than_yola_two_years_ago

    # FA
    answer = yola_weight_two_years_ago
    return answer