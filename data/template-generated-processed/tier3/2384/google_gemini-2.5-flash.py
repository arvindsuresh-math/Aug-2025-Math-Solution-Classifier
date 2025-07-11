def solve():
    """Index: 2384.
    Returns: the number of pfennigs Gerald will have left after buying the pie.
    """
    # L1
    total_farthings = 54 # Gerald has 54 farthings
    farthings_per_pfennig = 6 # there are 6 farthings to a pfennig
    farthings_in_pfennigs = total_farthings / farthings_per_pfennig

    # L2
    cost_of_pie = 2 # a meat pie that costs 2 pfennigs
    pfennigs_left = farthings_in_pfennigs - cost_of_pie

    # FA
    answer = pfennigs_left
    return answer