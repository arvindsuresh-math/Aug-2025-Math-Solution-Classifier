def solve():
    """Index: 1157.
    Returns: the number of additional pairs of underwear Tony can add.
    """
    # L1
    num_shirts = 2 # 2 shirts
    weight_per_shirt = 5 # a shirt weighs 5 ounces
    weight_shirts = num_shirts * weight_per_shirt

    # L2
    num_socks_pairs = 3 # 3 pairs of socks
    weight_per_sock_pair = 2 # a pair of socks weighs 2 ounces
    weight_socks = num_socks_pairs * weight_per_sock_pair

    # L3
    weight_pants = 10 # a pair of pants weighs 10 ounces
    weight_shorts = 8 # shorts weigh 8 ounces
    current_total_weight = weight_pants + weight_shirts + weight_shorts + weight_socks

    # L4
    max_weight_allowed = 50 # 50 total ounces of clothing
    remaining_capacity = max_weight_allowed - current_total_weight

    # L5
    weight_per_underwear = 4 # underwear weighs 4 ounces
    num_underwear_pairs = remaining_capacity / weight_per_underwear

    # FA
    answer = num_underwear_pairs
    return answer