def solve():
    """Index: 5416.
    Returns: the new area of the bathroom.
    """
    # L1
    original_area = 96 # The size of a bathroom is 96 sq ft
    original_width = 8 # the width of the bathroom is 8 feet
    original_length = original_area / original_width

    # L2
    extension_length = 2 # extend it by 2 feet on each side
    new_length = original_length + extension_length

    # L3
    extension_width = 2 # extend it by 2 feet on each side
    new_width = original_width + extension_width

    # L4
    new_area = new_length * new_width

    # FA
    answer = new_area
    return answer