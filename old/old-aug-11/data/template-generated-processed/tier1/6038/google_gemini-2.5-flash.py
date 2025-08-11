def solve():
    """Index: 6038.
    Returns: the total number of candy Mary has.
    """
    # L1
    megan_candy = 5 # Megan has 5 pieces of candy
    mary_multiplier = 3 # 3 times as much candy as Megan
    mary_initial_candy = megan_candy * mary_multiplier

    # L2
    mary_added_candy = 10 # adds 10 more pieces of candy
    mary_total_candy = mary_initial_candy + mary_added_candy

    # FA
    answer = mary_total_candy
    return answer