def solve():
    """Index: 574.
    Returns: the total amount Pauline spent on dinner ingredients.
    """
    # L1
    num_bell_peppers = 4 # 4 bell peppers
    cost_per_bell_pepper = 1.5 # $1.5 each
    cost_bell_peppers = num_bell_peppers * cost_per_bell_pepper

    # L2
    pounds_of_meat = 2 # 2 pounds of meat
    cost_per_pound_meat = 3 # $3 per pound
    cost_meat = pounds_of_meat * cost_per_pound_meat

    # L3
    cost_taco_shells = 5 # box of taco shells that cost $5
    total_spent = cost_taco_shells + cost_bell_peppers + cost_meat

    # FA
    answer = total_spent
    return answer