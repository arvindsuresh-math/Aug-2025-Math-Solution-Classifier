def solve():
    """Index: 51.
    Returns: the amount of fabric left in square feet.
    """
    # L1
    bolt_length = 16 # 16 feet by 12 feet
    bolt_width = 12 # 16 feet by 12 feet
    total_bolt_area = bolt_length * bolt_width

    # L2
    living_room_length = 4 # 4 foot by 6 foot rectangle for the living room
    living_room_width = 6 # 4 foot by 6 foot rectangle for the living room
    living_room_area = living_room_length * living_room_width

    # L3
    bedroom_length = 2 # 2 foot by 4 foot rectangle for the bedroom
    bedroom_width = 4 # 2 foot by 4 foot rectangle for the bedroom
    bedroom_area = bedroom_length * bedroom_width

    # L4
    fabric_left = total_bolt_area - living_room_area - bedroom_area

    # FA
    answer = fabric_left
    return answer