def solve():
    """Index: 3747.
    Returns: the amount of change the teacher received after buying the calculators.
    """
    # L1
    basic_calculator_cost = 8 # A basic calculator costs $8
    scientific_multiplier = 2 # twice the price as the basic
    scientific_calculator_cost = basic_calculator_cost * scientific_multiplier

    # L2
    graphing_multiplier = 3 # thrice the price as the scientific
    graphing_calculator_cost = scientific_calculator_cost * graphing_multiplier

    # L3
    total_spent = basic_calculator_cost + scientific_calculator_cost + graphing_calculator_cost

    # L4
    initial_money = 100 # had $100
    change_received = initial_money - total_spent

    # FA
    answer = change_received
    return answer