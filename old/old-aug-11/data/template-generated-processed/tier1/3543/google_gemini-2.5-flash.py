def solve():
    """Index: 3543.
    Returns: the total square feet of hardwood flooring installed.
    """
    # L1
    central_area_length = 10 # 10 foot by 10 foot central area
    central_area_width = 10 # 10 foot by 10 foot central area
    central_area_sq_ft = central_area_length * central_area_width

    # L2
    hallway_length = 6 # 6 foot by 4 foot hallway
    hallway_width = 4 # 6 foot by 4 foot hallway
    hallway_sq_ft = hallway_width * hallway_length

    # L3
    total_sq_ft = central_area_sq_ft + hallway_sq_ft

    # FA
    answer = total_sq_ft
    return answer