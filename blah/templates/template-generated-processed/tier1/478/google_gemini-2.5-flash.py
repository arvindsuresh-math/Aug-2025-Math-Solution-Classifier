def solve():
    """Index: 478.
    Returns: the total weight of Stan, Steve, and Jim.
    """
    # L1
    jim_weight = 110 # Jim weighs 110 pounds
    steve_lighter_than_jim = 8 # Steve is eight pounds lighter than Jim
    steve_weight = jim_weight - steve_lighter_than_jim

    # L2
    stan_more_than_steve = 5 # Stan weighs 5 more pounds than Steve
    stan_weight = steve_weight + stan_more_than_steve

    # L3
    total_weight = steve_weight + stan_weight + jim_weight

    # FA
    answer = total_weight
    return answer