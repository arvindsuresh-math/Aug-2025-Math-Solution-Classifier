def solve():
    """Index: 320.
    Returns: the amount Austin started with.
    """
    # L1
    num_friends = 7 # seven friends
    cost_per_robot = 8.75 # Each robot costs $8.75
    total_robot_cost = num_friends * cost_per_robot

    # L2
    tax_amount = 7.22 # charged $7.22 total for tax
    total_spent_in_store = total_robot_cost + tax_amount

    # L3
    change_left = 11.53 # left with $11.53 in change
    starting_amount = total_spent_in_store + change_left

    # FA
    answer = starting_amount
    return answer