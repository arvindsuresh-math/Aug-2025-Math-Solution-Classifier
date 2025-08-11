def solve():
    """Index: 7210.
    Returns: the total cost to spend on chips.
    """
    # L1
    chips_per_bag = 24 # A bag has 24 chips
    calories_per_chip = 10 # Each chip is 10 calories
    calories_per_bag = chips_per_bag * calories_per_chip

    # L2
    desired_calories = 480 # If he wants to eat 480 calories
    bags_needed = desired_calories / calories_per_bag

    # L3
    cost_per_bag = 2 # costs $2
    total_cost = bags_needed * cost_per_bag

    # FA
    answer = total_cost
    return answer