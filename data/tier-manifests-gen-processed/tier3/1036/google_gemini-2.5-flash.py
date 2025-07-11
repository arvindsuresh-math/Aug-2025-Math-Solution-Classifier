def solve():
    """Index: 1036.
    Returns: the number of markers Alia has.
    """
    # L1
    steve_markers = 60 # Steve has 60 markers
    austin_fraction_denominator = 3 # one-third as many markers
    austin_markers = steve_markers / austin_fraction_denominator

    # L2
    alia_multiplier = 2 # 2 times as many markers
    alia_markers = austin_markers * alia_multiplier

    # FA
    answer = alia_markers
    return answer