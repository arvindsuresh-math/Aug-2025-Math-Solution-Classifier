def solve():
    """Index: 1658.
    Returns: the total number of blueberries James needs to pick.
    """
    # L1
    blueberries_per_pint = 200 # 200 blueberries to make a pint
    pints_per_quart = 2 # two pints per quart
    blueberries_per_pie = blueberries_per_pint * pints_per_quart

    # L2
    num_pies = 6 # make 6 pies
    total_blueberries_needed = blueberries_per_pie * num_pies

    # FA
    answer = total_blueberries_needed
    return answer