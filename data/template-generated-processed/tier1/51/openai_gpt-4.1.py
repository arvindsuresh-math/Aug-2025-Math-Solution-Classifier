def solve():
    """Index: 51.
    Returns: the amount of fabric left in square feet after making the curtains.
    """
    # L1
    bolt_length = 16 # bolt of fabric is 16 feet
    bolt_width = 12 # bolt of fabric is 12 feet
    bolt_area = bolt_length * bolt_width

    # L2
    living_length = 4 # 4 foot by 6 foot rectangle for the living room
    living_width = 6 # 4 foot by 6 foot rectangle for the living room
    living_area = living_length * living_width

    # L3
    bedroom_length = 2 # 2 foot by 4 foot rectangle for the bedroom
    bedroom_width = 4 # 2 foot by 4 foot rectangle for the bedroom
    bedroom_area = bedroom_length * bedroom_width

    # L4
    fabric_left = bolt_area - living_area - bedroom_area

    # FA
    answer = fabric_left
    return answer