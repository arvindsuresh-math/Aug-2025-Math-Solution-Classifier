def solve():
    """Index: 258.
    Returns: the height difference between Bella and Anne's sister in cm.
    """
    # L2
    anne_height = 80 # Anne is 80cm tall
    anne_to_sister_ratio = 2 # Anne is 2 times as tall as her sister
    sister_height = anne_height / anne_to_sister_ratio

    # L3
    bella_to_anne_ratio = 3 # Bella is 3 times as tall as Anne
    bella_height = bella_to_anne_ratio * anne_height

    # L4
    height_difference = bella_height - sister_height

    # FA
    answer = height_difference
    return answer