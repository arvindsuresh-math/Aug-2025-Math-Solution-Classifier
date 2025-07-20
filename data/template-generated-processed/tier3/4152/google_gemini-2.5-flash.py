def solve():
    """Index: 4152.
    Returns: the amount of money Karen would save.
    """
    # L1
    total_years = 30 # over 30 years
    cheaper_coat_duration = 5 # will last for five years
    num_cheaper_coats = total_years / cheaper_coat_duration

    # L2
    cheaper_coat_cost = 120 # costs $120
    total_cost_cheaper_coats = num_cheaper_coats * cheaper_coat_cost

    # L3
    expensive_coat_duration = 15 # will last for 15 years
    num_expensive_coats = total_years / expensive_coat_duration

    # L4
    expensive_coat_cost = 300 # costs $300
    total_cost_expensive_coats = num_expensive_coats * expensive_coat_cost

    # L5
    money_saved = total_cost_cheaper_coats - total_cost_expensive_coats

    # FA
    answer = money_saved
    return answer