def solve():
    """Index: 1240.
    Returns: the maximum height in feet the balloon can fly.
    """
    # L1
    initial_money = 200 # $200
    sheet_cost = 42 # $42 for sheet
    rope_cost = 18 # $18 for rope
    tank_burner_cost = 14 # $14 for propane tank and burner
    money_for_helium = initial_money - sheet_cost - rope_cost - tank_burner_cost

    # L2
    helium_price_per_oz = 1.5 # $1.50 per ounce
    helium_ounces = money_for_helium / helium_price_per_oz

    # L3
    feet_per_ounce = 113 # 113 feet higher per ounce
    max_height = helium_ounces * feet_per_ounce

    # FA
    answer = max_height
    return answer