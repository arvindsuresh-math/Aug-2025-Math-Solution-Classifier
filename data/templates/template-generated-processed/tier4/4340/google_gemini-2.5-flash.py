def solve():
    """Index: 4340.
    Returns: the total money Claudia makes from the art classes.
    """
    # L1
    saturday_kids = 20 # 20 kids attend Saturday’s class
    sunday_half_factor = 2 # half that many attend Sunday’s class
    sunday_kids = saturday_kids / sunday_half_factor

    # L2
    total_kids = saturday_kids + sunday_kids

    # L3
    charge_per_kid = 10.00 # charges $10.00 for her one-hour class
    total_money_made = charge_per_kid * total_kids

    # FA
    answer = total_money_made
    return answer