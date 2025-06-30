def solve(
    bolt_length: int = 16,  # bolt of fabric is 16 feet long
    bolt_width: int = 12,   # bolt of fabric is 12 feet wide
    living_room_length: int = 4,  # living room curtain is 4 feet long
    living_room_width: int = 6,   # living room curtain is 6 feet wide
    bedroom_length: int = 2,  # bedroom curtain is 2 feet long
    bedroom_width: int = 4    # bedroom curtain is 4 feet wide
):
    """Index: 51.
    Returns: the amount of fabric left in square feet after cutting curtains."""
    #: L1
    total_fabric_area = bolt_length * bolt_width # eval: 192 = 16 * 12
    #: L2
    living_room_curtain_area = living_room_length * living_room_width # eval: 24 = 4 * 6
    #: L3
    bedroom_curtain_area = bedroom_length * bedroom_width # eval: 8 = 2 * 4
    #: L4
    fabric_left = total_fabric_area - living_room_curtain_area - bedroom_curtain_area # eval: 160 = 192 - 24 - 8
    answer = fabric_left  # FINAL ANSWER # eval: 160 = 160  # FINAL ANSWER
    return answer # eval: return 160