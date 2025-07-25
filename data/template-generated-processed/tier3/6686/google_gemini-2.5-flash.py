def solve():
    """Index: 6686.
    Returns: the number of champagne bottles Ashley will need.
    """
    # L1
    glasses_per_guest = 2 # 2 glasses of champagne to each
    num_guests = 120 # 120 wedding guests
    total_servings_needed = glasses_per_guest * num_guests

    # L2
    servings_per_bottle = 6 # 1 bottle of champagne has 6 servings
    bottles_needed = total_servings_needed / servings_per_bottle

    # FA
    answer = bottles_needed
    return answer