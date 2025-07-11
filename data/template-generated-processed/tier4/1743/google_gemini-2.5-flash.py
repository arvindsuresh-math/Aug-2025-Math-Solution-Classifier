def solve():
    """Index: 1743.
    Returns: the total cost Wayne will spend on the appetizer.
    """
    # L1
    shrimp_per_guest = 5 # 5 shrimp per guest
    num_guests = 40 # 40 guests
    total_shrimp_needed = shrimp_per_guest * num_guests

    # L2
    shrimp_per_pound = 20 # each pound has 20 shrimp
    pounds_of_shrimp_needed = total_shrimp_needed / shrimp_per_pound

    # L3
    cost_per_pound = 17.00 # $17.00 per pound
    total_cost = cost_per_pound * pounds_of_shrimp_needed

    # FA
    answer = total_cost
    return answer