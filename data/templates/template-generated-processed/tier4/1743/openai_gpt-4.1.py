def solve():
    """Index: 1743.
    Returns: the total amount Wayne will spend on shrimp appetizer.
    """
    # L1
    shrimp_per_guest = 5 # 5 shrimp per guest
    num_guests = 40 # 40 guests
    total_shrimp_needed = shrimp_per_guest * num_guests

    # L2
    shrimp_per_pound = 20 # each pound has 20 shrimp
    total_pounds_needed = total_shrimp_needed / shrimp_per_pound

    # L3
    price_per_pound = 17 # $17.00 per pound
    total_cost = price_per_pound * total_pounds_needed

    # FA
    answer = total_cost
    return answer