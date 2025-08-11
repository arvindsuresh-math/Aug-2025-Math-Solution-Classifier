def solve():
    """Index: 109.
    Returns: the number of chicken nuggets Alyssa ate.
    """
    # L1
    total_nuggets = 100 # Alyssa, Keely, and Kendall ordered 100 chicken nuggets
    alyssa_factor = 1 # A (how many Alyssa ate)
    keely_factor = 2 # Keely ate twice as many as Alyssa
    kendall_factor = 2 # Kendall each ate twice as many as Alyssa
    total_factor = alyssa_factor + keely_factor + kendall_factor
    # 100 = A + 2A + 2A = 5A
    # L2
    alyssa_nuggets = total_nuggets / total_factor
    # FA
    answer = alyssa_nuggets
    return answer