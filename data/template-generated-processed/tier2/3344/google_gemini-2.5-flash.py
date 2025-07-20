def solve():
    """Index: 3344.
    Returns: the number of quarters in the jar.
    """
    # L1
    num_family_members = 5 # All five family members
    cost_per_scoop = 3 # costs $3 each
    total_spent_ice_cream = num_family_members * cost_per_scoop

    # L2
    cents_left_over = 0.48 # 48 cents left over
    total_change_had = total_spent_ice_cream + cents_left_over

    # L3
    num_pennies = 123 # 123 pennies
    penny_value = 0.01 # WK
    pennies_value = num_pennies * penny_value

    # L4
    num_nickels = 85 # 85 nickels
    nickel_value = 0.05 # WK
    nickels_value = num_nickels * nickel_value

    # L5
    num_dimes = 35 # 35 dimes
    dime_value = 0.1 # WK
    dimes_value = num_dimes * dime_value

    # L6
    total_without_quarters = pennies_value + nickels_value + dimes_value

    # L7
    quarters_value = total_change_had - total_without_quarters

    # L8
    quarter_value = 0.25 # WK
    num_quarters = quarters_value / quarter_value

    # FA
    answer = num_quarters
    return answer