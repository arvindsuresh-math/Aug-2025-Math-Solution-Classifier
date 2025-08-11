def solve():
    """Index: 7471.
    Returns: the total cost of all lunches.
    """
    # L1
    children_count = 35 # 35 children in her class
    chaperone_count = 5 # 5 volunteer chaperones
    janet_count = 1 # herself
    additional_lunches = 3 # three additional sack lunches
    total_lunches = children_count + chaperone_count + janet_count + additional_lunches

    # L2
    cost_per_lunch = 7 # Each sack lunch costs $7
    total_cost = cost_per_lunch * total_lunches

    # FA
    answer = total_cost
    return answer