def solve():
    """Index: 6217.
    Returns: the total number of lemons they have in all.
    """
    # L1
    levi_lemons = 5 # Levi has 5 lemons
    jayden_more_than_levi = 6 # Jayden has 6 more lemons than Levi
    jayden_lemons = levi_lemons + jayden_more_than_levi

    # L2
    eli_multiplier = 3 # one-third as many lemons as Eli has (meaning Eli has 3 times Jayden's lemons)
    eli_lemons = jayden_lemons * eli_multiplier

    # L3
    ian_multiplier = 2 # one-half as many lemons as Ian has (meaning Ian has 2 times Eli's lemons)
    ian_lemons = eli_lemons * ian_multiplier

    # L4
    total_lemons = levi_lemons + jayden_lemons + eli_lemons + ian_lemons

    # FA
    answer = total_lemons
    return answer