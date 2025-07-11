def solve():
    """Index: 1488.
    Returns: the total number of earrings all friends have.
    """
    # L1
    total_percentage = 100 # 100%
    bella_percentage_of_monica = 25 # 25% of Monica's earrings
    ratio_monica_to_bella = total_percentage / bella_percentage_of_monica

    # L2
    bella_earrings = 10 # Bella has 10 earrings
    monica_earrings = bella_earrings * ratio_monica_to_bella

    # L3
    rachel_divisor = 2 # twice as many earrings as Rachel
    rachel_earrings = monica_earrings / rachel_divisor

    # L4
    total_earrings = bella_earrings + monica_earrings + rachel_earrings

    # FA
    answer = total_earrings
    return answer