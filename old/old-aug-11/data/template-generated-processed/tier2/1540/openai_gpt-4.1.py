def solve():
    """Index: 1540.
    Returns: the amount of money Sam has now after all investments and returns.
    """
    # L1
    initial_investment = 10000 # Sam invested $10,000
    first_interest_factor = 1.2 # earned 20% interest compounded
    after_one_year = initial_investment * first_interest_factor

    # L2
    after_two_years = after_one_year * first_interest_factor

    # L3
    after_three_years = after_two_years * first_interest_factor

    # L4
    triple_factor = 3 # three times as much invested
    after_triple_investment = triple_factor * after_three_years

    # L5
    second_interest_factor = 1.15 # 15% return on his investment
    final_amount = after_triple_investment * second_interest_factor

    # FA
    answer = final_amount
    return answer