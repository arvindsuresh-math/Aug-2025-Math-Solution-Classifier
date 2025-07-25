def solve():
    """Index: 5758.
    Returns: the average number of dandelions picked by Billy and George.
    """
    # L1
    billy_initial_picks = 36 # Billy picks 36
    george_fraction_denominator = 3 # 1/3 as many as Billy
    george_initial_picks = billy_initial_picks / george_fraction_denominator

    # L2
    additional_picks_each = 10 # pick 10 more each
    george_total_picks = george_initial_picks + additional_picks_each

    # L3
    billy_total_picks = billy_initial_picks + additional_picks_each

    # L4
    total_dandelions_picked = george_total_picks + billy_total_picks

    # L5
    number_of_people = 2 # WK
    average_dandelions_picked = total_dandelions_picked / number_of_people

    # FA
    answer = average_dandelions_picked
    return answer