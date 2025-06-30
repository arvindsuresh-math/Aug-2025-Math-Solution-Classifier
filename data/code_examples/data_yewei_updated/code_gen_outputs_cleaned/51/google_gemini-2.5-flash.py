def solve(
        living_room_length: int = 4, # a 4 foot by 6 foot rectangle for the living room
        living_room_width: int = 6, # a 4 foot by 6 foot rectangle for the living room
        bedroom_length: int = 2, # a 2 foot by 4 foot rectangle for the bedroom
        bedroom_width: int = 4, # a 2 foot by 4 foot rectangle for the bedroom
        bolt_length: int = 16, # the bolt of fabric is 16 feet by 12 feet
        bolt_width: int = 12 # the bolt of fabric is 16 feet by 12 feet
    ):
    """Index: 51.
    Returns: the amount of fabric left in square feet.
    """
    #: L1
    original_bolt_area = bolt_length * bolt_width

    #: L2
    living_room_fabric_area = living_room_length * living_room_width

    #: L3
    bedroom_fabric_area = bedroom_length * bedroom_width

    #: L4
    fabric_left = original_bolt_area - living_room_fabric_area - bedroom_fabric_area

    answer = fabric_left # FINAL ANSWER
    return answer