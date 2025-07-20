def solve():
    """Index: 4199.
    Returns: the amount of money Jenn will have left over after buying the bike.
    """
    # L1
    num_jars = 5 # 5 jars
    quarters_per_jar = 160 # 160 quarters
    total_quarters = num_jars * quarters_per_jar

    # L2
    quarter_value_dollars = 0.25 # WK
    total_money_dollars = total_quarters * quarter_value_dollars

    # L3
    bike_cost = 180 # bike costs 180 dollars
    money_left_over = total_money_dollars - bike_cost

    # FA
    answer = money_left_over
    return answer