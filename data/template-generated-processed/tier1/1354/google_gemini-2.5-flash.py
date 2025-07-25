def solve():
    """Index: 1354.
    Returns: the number of square yards of sod Archie will need for his backyard.
    """
    # L1
    backyard_length = 20 # 20 yards
    backyard_width = 13 # 13 yards
    backyard_area = backyard_length * backyard_width

    # L2
    shed_length = 3 # 3 yards
    shed_width = 5 # 5 yards
    shed_area = shed_length * shed_width

    # L3
    sod_needed = backyard_area - shed_area

    # FA
    answer = sod_needed
    return answer