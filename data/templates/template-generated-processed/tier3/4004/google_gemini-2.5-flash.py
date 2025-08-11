def solve():
    """Index: 4004.
    Returns: the total number of necklaces John can make.
    """
    # L1
    num_spools = 3 # 3 spools of wire
    feet_per_spool = 20 # 20 feet each
    total_wire_feet = num_spools * feet_per_spool

    # L2
    feet_per_necklace = 4 # 4 feet to make a necklace
    num_necklaces = total_wire_feet / feet_per_necklace

    # FA
    answer = num_necklaces
    return answer