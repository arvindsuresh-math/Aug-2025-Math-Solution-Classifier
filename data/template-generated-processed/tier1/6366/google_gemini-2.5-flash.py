def solve():
    """Index: 6366.
    Returns: the number of marbles Elsa ended the day with.
    """
    # L1
    initial_marbles = 40 # started the day with 40 marbles
    lost_at_breakfast = 3 # lost 3 marbles while playing
    gave_to_susie = 5 # gave her best friend Susie 5 marbles
    marbles_after_loss_and_giving = initial_marbles - lost_at_breakfast - gave_to_susie

    # L2
    mom_bought = 12 # mom bought her a new bag with 12 marbles
    marbles_after_mom_bought = mom_bought + marbles_after_loss_and_giving

    # L3
    multiplier_twice = 2 # twice as many marbles
    received_from_susie = multiplier_twice * gave_to_susie

    # L4
    total_marbles_end_of_day = marbles_after_mom_bought + received_from_susie

    # FA
    answer = total_marbles_end_of_day
    return answer