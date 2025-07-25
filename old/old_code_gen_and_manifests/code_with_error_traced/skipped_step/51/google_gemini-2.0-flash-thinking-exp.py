def solve(
    living_room_length: int = 4, # cuts a 4 foot
    living_room_width: int = 6, # by 6 foot rectangle for the living room
    bedroom_length: int = 2, # and a 2 foot
    bedroom_width: int = 4, # by 4 foot rectangle for the bedroom
    bolt_length: int = 16, # the bolt of fabric is 16 feet
    bolt_width: int = 12 # by 12 feet
):
    """Index: 51.
    Returns: the amount of fabric left in square feet.
    """

    #: L1
    original_bolt_area = bolt_length * bolt_width # eval: 192 = 16 * 12

    #: L2

    #: L3
    bedroom_area = bedroom_length * bedroom_width # eval: 8 = 2 * 4

    #: L4
    fabric_left = original_bolt_area - bedroom_width - bedroom_area # eval: 180 = 192 - 4 - 8

    #: FA
    answer = fabric_left
    return answer # eval: return 180
