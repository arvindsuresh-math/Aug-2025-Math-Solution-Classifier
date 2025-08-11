def solve():
    """Index: 292.
    Returns: the total number of scarves May can make.
    """
    # L1
    red_yarns = 2 # 2 red yarns
    scarves_per_yarn = 3 # 3 scarves using one yarn
    red_scarves = red_yarns * scarves_per_yarn

    # L2
    blue_yarns = 6 # 6 blue yarns
    blue_scarves = scarves_per_yarn * blue_yarns

    # L3
    yellow_yarns = 4 # 4 yellow yarns
    yellow_scarves = yellow_yarns * scarves_per_yarn

    # L4
    total_scarves = yellow_scarves + blue_scarves + red_scarves

    # FA
    answer = total_scarves
    return answer