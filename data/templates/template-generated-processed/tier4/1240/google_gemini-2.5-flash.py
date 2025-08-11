def solve():
    """Index: 1240.
    Returns: the total height in feet the balloon can fly.
    """
    # L1
    initial_money = 200 # $200
    sheet_cost = 42 # $42
    rope_cost = 18 # $18
    burner_cost = 14 # $14
    money_for_helium = initial_money - sheet_cost - rope_cost - burner_cost

    # L2
    helium_cost_per_ounce = 1.50 # $1.50 per ounce
    ounces_of_helium = money_for_helium / helium_cost_per_ounce

    # L3
    feet_per_ounce = 113 # 113 feet higher
    total_feet_flown = ounces_of_helium * feet_per_ounce

    # FA
    answer = total_feet_flown
    return answer