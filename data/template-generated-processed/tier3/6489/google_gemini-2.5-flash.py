def solve():
    """Index: 6489.
    Returns: the number of acorns the squirrel has to eat at the beginning of spring.
    """
    # L1
    total_acorns = 210 # stashed 210 acorns
    num_piles = 3 # divided the pile into thirds
    acorns_per_pile = total_acorns / num_piles

    # L2
    left_per_month = 60 # leaving 60 acorns for each winter month
    taken_per_pile = acorns_per_pile - left_per_month

    # L3
    acorns_for_spring = num_piles * taken_per_pile

    # FA
    answer = acorns_for_spring
    return answer