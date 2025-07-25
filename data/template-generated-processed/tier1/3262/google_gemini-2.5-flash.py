def solve():
    """Index: 3262.
    Returns: the required length of the curtains in inches.
    """
    # L1
    inches_per_foot = 12 # WK
    room_height_feet = 8 # room is 8 feet tall
    room_height_inches = inches_per_foot * room_height_feet

    # L2
    additional_material_inches = 5 # additional 5" of material
    total_curtain_length_inches = additional_material_inches + room_height_inches

    # FA
    answer = total_curtain_length_inches
    return answer