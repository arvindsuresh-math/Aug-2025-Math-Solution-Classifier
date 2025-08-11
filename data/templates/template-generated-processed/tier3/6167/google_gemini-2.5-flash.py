def solve():
    """Index: 6167.
    Returns: the difference in the number of potato chips and wedges Cynthia made.
    """
    # L1
    total_potatoes = 67 # Cynthia harvested 67 potatoes
    potatoes_for_wedges = 13 # she cut 13 of them into wedges
    remaining_potatoes = total_potatoes - potatoes_for_wedges

    # L2
    halved_divisor = 2 # halved the remaining potatoes
    potatoes_for_chips = remaining_potatoes / halved_divisor

    # L3
    wedges_per_potato = 8 # one potato can be cut into 8 wedges
    total_wedges = potatoes_for_wedges * wedges_per_potato

    # L4
    chips_per_potato = 20 # make 20 potato chips
    total_chips = potatoes_for_chips * chips_per_potato

    # L5
    difference_chips_wedges = total_chips - total_wedges

    # FA
    answer = difference_chips_wedges
    return answer