def solve():
    """Index: 7169.
    Returns: the total number of pints picked by the three.
    """
    # L1
    annie_pints = 8 # eight pints of blueberries
    kathryn_more_than_annie = 2 # two pints more than Annie
    kathryn_pints = annie_pints + kathryn_more_than_annie

    # L2
    ben_fewer_than_kathryn = 3 # three pints fewer than Kathryn
    ben_pints = kathryn_pints - ben_fewer_than_kathryn

    # L3
    total_pints = annie_pints + kathryn_pints + ben_pints

    # FA
    answer = total_pints
    return answer