def solve():
    """Index: 956.
    Returns: the number of square feet of the garden used for strawberries.
    """
    # L1
    garden_size = 64 # Joel’s garden is 64 square feet large
    fruit_division_factor = 2 # half of the garden for fruits
    fruit_section_size = garden_size / fruit_division_factor

    # L2
    strawberry_division_factor = 4 # a quarter of the fruit section
    strawberry_area = fruit_section_size / strawberry_division_factor

    # FA
    answer = strawberry_area
    return answer