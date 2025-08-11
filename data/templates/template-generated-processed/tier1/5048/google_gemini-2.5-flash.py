def solve():
    """Index: 5048.
    Returns: the number of awards the rival won.
    """
    # L1
    jessie_multiplier = 3 # 3 times as many athletic awards as his buddy Scott
    scott_awards = 4 # Scott, who won 4 awards
    jessie_awards = jessie_multiplier * scott_awards

    # L2
    rival_multiplier = 2 # twice as many awards as Jessie
    rival_awards = rival_multiplier * jessie_awards

    # FA
    answer = rival_awards
    return answer