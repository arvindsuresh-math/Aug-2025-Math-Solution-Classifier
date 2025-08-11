def solve():
    """Index: 4651.
    Returns: the number of aprons Heather should sew tomorrow.
    """
    # L1
    already_sewn_aprongs = 13 # she already was able to sew 13 aprons
    multiplier_today = 3 # three times as many aprons
    aprongs_sewn_today = already_sewn_aprongs * multiplier_today

    # L2
    total_aprongs_sewn = already_sewn_aprongs + aprongs_sewn_today

    # L3
    total_needed_aprongs = 150 # sew 150 aprons
    remaining_aprongs_needed = total_needed_aprongs - total_aprongs_sewn

    # L4
    tomorrow_divisor = 2 # half of the remaining number of aprons
    aprongs_for_tomorrow = remaining_aprongs_needed / tomorrow_divisor

    # FA
    answer = aprongs_for_tomorrow
    return answer