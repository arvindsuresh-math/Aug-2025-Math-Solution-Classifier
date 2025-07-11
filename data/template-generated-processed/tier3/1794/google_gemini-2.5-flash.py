def solve():
    """Index: 1794.
    Returns: Joshua's share of the money.
    """
    # L1
    total_money = 40 # shared $40
    justin_parts = 1 # 1 part for Justin
    joshua_parts = 3 # thrice as much as Justin's
    total_parts = justin_parts + joshua_parts

    # L2
    value_per_part = total_money / total_parts

    # L3
    joshua_share = value_per_part * joshua_parts

    # FA
    answer = joshua_share
    return answer