def solve():
    """Index: 4725.
    Returns: the moose population of Canada in millions.
    """
    # L1
    total_humans_millions = 38 # 38 million people in Canada
    humans_per_beaver = 19 # 19 humans for every one beaver
    beavers_millions = total_humans_millions / humans_per_beaver

    # L2
    beavers_per_moose = 2 # for every moose there are two beavers
    moose_millions = beavers_millions / beavers_per_moose

    # FA
    answer = moose_millions
    return answer