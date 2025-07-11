def solve():
    """Index: 1845.
    Returns: how much money Julia is short.
    """
    # L1
    rock_roll_cd_price = 5 # rock and roll CDs are $5 each
    num_each_type = 4 # buy 4 of each
    rock_roll_cost = rock_roll_cd_price * num_each_type

    # L2
    pop_cd_price = 10 # pop CDs are $10 each
    pop_cost = pop_cd_price * num_each_type

    # L3
    dance_cd_price = 3 # dance CDs are $3 each
    dance_cost = dance_cd_price * num_each_type

    # L4
    country_cd_price = 7 # country CDs are $7 each
    country_cost = country_cd_price * num_each_type

    # L5
    total_cost_needed = rock_roll_cost + pop_cost + dance_cost + country_cost

    # L6
    julia_has_money = 75 # she only has 75 dollars
    money_short = total_cost_needed - julia_has_money

    # FA
    answer = money_short
    return answer