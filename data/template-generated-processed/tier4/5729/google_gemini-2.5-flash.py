def solve():
    """Index: 5729.
    Returns: the number of flamingoes Milly needs to harvest.
    """
    # L1
    flamingo_tail_feathers = 20 # 20 tail feathers
    safe_pluck_percent_num = 25 # 25% of their tail feathers
    percent_factor = 0.01 # WK
    feathers_per_flamingo = flamingo_tail_feathers * safe_pluck_percent_num * percent_factor

    # L2
    num_boas = 12 # 12 boas
    feathers_per_boa = 200 # each boa has 200 feathers
    total_feathers_needed = num_boas * feathers_per_boa

    # L3
    num_flamingoes_needed = total_feathers_needed / feathers_per_flamingo

    # FA
    answer = num_flamingoes_needed
    return answer