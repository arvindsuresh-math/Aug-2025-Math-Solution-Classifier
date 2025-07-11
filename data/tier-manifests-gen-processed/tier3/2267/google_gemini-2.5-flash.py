def solve():
    """Index: 2267.
    Returns: the number of houses on the street.
    """
    # L1
    num_children = 11 # 11 children
    items_per_child = 4 # 4 items of clothing
    child_clothing_items = num_children * items_per_child

    # L2
    num_adults = 20 # 20 adults
    items_per_adult = 3 # 3 items of clothing
    adult_clothing_items = num_adults * items_per_adult

    # L3
    total_clothing_items = child_clothing_items + adult_clothing_items

    # L4
    items_per_clothesline = 2 # Each clothesline can hold 2 items of clothing
    total_clotheslines = total_clothing_items / items_per_clothesline

    # L5
    clotheslines_per_house = 2 # 2 clotheslines for every house
    num_houses = total_clotheslines / clotheslines_per_house

    # FA
    answer = num_houses
    return answer