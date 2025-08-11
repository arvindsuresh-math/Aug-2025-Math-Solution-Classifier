def solve():
    """Index: 4965.
    Returns: the total cost of the shirts.
    """
    # L1
    first_shirt_cost = 15 # first shirt costs $15
    cost_difference = 6 # $6 more than the second shirt
    second_shirt_cost = first_shirt_cost - cost_difference

    # L2
    total_cost = first_shirt_cost + second_shirt_cost

    # FA
    answer = total_cost
    return answer