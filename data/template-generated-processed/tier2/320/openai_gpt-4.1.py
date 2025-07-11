def solve():
    """Index: 320.
    Returns: the amount Austin started with.
    """
    # L1
    num_robots = 7 # seven friends each a robot
    robot_cost = 8.75 # Each robot costs $8.75
    total_robot_cost = num_robots * robot_cost

    # L2
    tax = 7.22 # charged $7.22 total for tax
    total_spent = total_robot_cost + tax

    # L3
    change = 11.53 # left with $11.53 in change
    starting_amount = total_spent + change

    # FA
    answer = starting_amount
    return answer