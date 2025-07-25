def solve():
    """Index: 3717.
    Returns: the initial number of strawberry plants Mark planted.
    """
    # L1
    plants_given_away = 4 # After 3 months, Mark digs up 4 strawberry plants and gives them to his friend
    plants_remaining = 20 # If he still has 20 strawberry plants
    plants_before_giving_away = plants_given_away + plants_remaining

    # L2
    growth_factor_per_month = 2 # Every month, the number of strawberry plants doubles
    plants_after_two_months = plants_before_giving_away / growth_factor_per_month

    # L3
    plants_after_one_month = plants_after_two_months / growth_factor_per_month

    # L4
    initial_plants = plants_after_one_month / growth_factor_per_month

    # FA
    answer = initial_plants
    return answer