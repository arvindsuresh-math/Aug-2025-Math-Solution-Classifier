def solve():
    """Index: 5014.
    Returns: the total time it will take Ellen to paint all the flowers and vines.
    """
    # L1
    time_per_lily = 5 # 5 minutes to paint a lily
    num_lilies = 17 # 17 lilies
    total_time_lilies = time_per_lily * num_lilies

    # L2
    time_per_rose = 7 # 7 minutes to paint a rose
    num_roses = 10 # 10 roses
    total_time_roses = time_per_rose * num_roses

    # L3
    time_per_orchid = 3 # 3 minutes to paint an orchid
    num_orchids = 6 # 6 orchids
    total_time_orchids = time_per_orchid * num_orchids

    # L4
    time_per_vine = 2 # 2 minutes to paint a vine
    num_vines = 20 # 20 vines
    total_time_vines = time_per_vine * num_vines

    # L5
    total_time = total_time_lilies + total_time_roses + total_time_orchids + total_time_vines

    # FA
    answer = total_time
    return answer