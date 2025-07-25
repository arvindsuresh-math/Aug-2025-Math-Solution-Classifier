def solve():
    """Index: 6563.
    Returns: the total number of plates Jack has left.
    """
    # L1
    num_multiplier_polka_dotted = 2 # twice as many
    checked_plates_initial = 8 # 8 plates with a checked pattern
    polka_dotted_plates = num_multiplier_polka_dotted * checked_plates_initial

    # L2
    flower_plates_initial = 4 # four plates with a flower pattern
    smashed_flower_plates = 1 # smashes one of the flowered plates
    flower_plates_left = flower_plates_initial - smashed_flower_plates

    # L3
    total_plates = flower_plates_left + polka_dotted_plates + checked_plates_initial

    # FA
    answer = total_plates
    return answer