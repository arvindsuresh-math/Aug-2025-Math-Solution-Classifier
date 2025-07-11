def solve():
    """Index: 1658.
    Returns: the total number of blueberries James needs to pick to make 6 pies.
    """
    # L1
    blueberries_per_pint = 200 # James needs 200 blueberries to make a pint of blueberry jam
    pints_per_quart = 2 # there are two pints per quart
    blueberries_per_pie = blueberries_per_pint * pints_per_quart

    # L2
    number_of_pies = 6 # to make 6 pies
    total_blueberries = blueberries_per_pie * number_of_pies

    # FA
    answer = total_blueberries
    return answer