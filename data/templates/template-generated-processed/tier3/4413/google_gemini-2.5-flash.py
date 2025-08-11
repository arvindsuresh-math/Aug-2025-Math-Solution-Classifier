def solve():
    """Index: 4413.
    Returns: the number of sodas each sibling receives.
    """
    # L1
    sisters = 2 # he has 2 sisters
    multiplier_brothers = 2 # twice as many brothers as sisters
    num_brothers = sisters * multiplier_brothers

    total_siblings = sisters + num_brothers

    # L2
    total_sodas = 12 # a 12 pack of soda
    sodas_per_sibling = total_sodas / total_siblings

    # FA
    answer = sodas_per_sibling
    return answer