def solve():
    """Index: 5441.
    Returns: the cost of the computer.
    """
    # L1
    total_budget = 1600 # total budget of $1600
    tv_cost = 600 # The TV costs $600
    fridge_and_computer_cost = total_budget - tv_cost

    # L2
    fridge_cost_more_than_computer = 500 # the fridge costs $500 more than the computer
    divisor_for_average = 2 # WK
    computer_cost = (fridge_and_computer_cost - fridge_cost_more_than_computer) / divisor_for_average

    # FA
    answer = computer_cost
    return answer