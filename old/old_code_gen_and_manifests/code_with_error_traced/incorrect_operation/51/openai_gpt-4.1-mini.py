def solve(
    bolt_length: int = 16,  # bolt of fabric is 16 feet
    bolt_width: int = 12,   # bolt of fabric is 12 feet
    living_room_length: int = 4,  # living room curtain length 4 feet
    living_room_width: int = 6,   # living room curtain width 6 feet
    bedroom_length: int = 2,       # bedroom curtain length 2 feet
    bedroom_width: int = 4         # bedroom curtain width 4 feet
):
    """Index: 51.
    Returns: the amount of fabric left in square feet after cutting curtains.
    """

    #: L1
    total_fabric_area = bolt_length * bolt_width # eval: 192 = 16 * 12

    #: L2
    living_room_area = living_room_length * living_room_width # eval: 24 = 4 * 6

    #: L3
    bedroom_area = bedroom_length - bedroom_width # eval: -2 = 2 - 4

    #: L4
    fabric_left = total_fabric_area - living_room_area - bedroom_area # eval: 170 = 192 - 24 - -2

    #: FA
    answer = fabric_left
    return answer # eval: return 170
