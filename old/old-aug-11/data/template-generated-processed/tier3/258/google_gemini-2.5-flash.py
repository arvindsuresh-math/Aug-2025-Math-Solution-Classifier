def solve():
    """Index: 258.
    Returns: the height difference between Bella and Anne's sister.
    """
    # L2
    Anne_height = 80 # Anne is 80cm tall
    anne_sister_multiplier = 2 # 2 times as tall as her sister
    sister_height = Anne_height / anne_sister_multiplier

    # L3
    bella_anne_multiplier = 3 # Bella is 3 times as tall as Anne
    bella_height = bella_anne_multiplier * Anne_height

    # L4
    height_difference = bella_height - sister_height

    # FA
    answer = height_difference
    return answer