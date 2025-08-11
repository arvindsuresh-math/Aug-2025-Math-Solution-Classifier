def solve():
    """Index: 5342.
    Returns: how many more chocolates Alix has than Nick.
    """
    # L1
    nick_chocolates = 10 # Nick hides 10 chocolates
    alix_multiplier = 3 # 3 times as many chocolates than Nick hides
    alix_initial_chocolates = alix_multiplier * nick_chocolates

    # L2
    mom_took_chocolates = 5 # took 5 chocolates from Alix
    alix_remaining_chocolates = alix_initial_chocolates - mom_took_chocolates

    # L3
    alix_more_than_nick = alix_remaining_chocolates - nick_chocolates

    # FA
    answer = alix_more_than_nick
    return answer