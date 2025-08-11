def solve():
    """Index: 3673.
    Returns: how much shorter Lucille's house is than the average height.
    """
    # L1
    neighbor_house_1_height = 70 # One neighbor's house is 70 feet tall
    lucille_house_height = 80 # His family's house is 80 feet tall
    neighbor_house_2_height = 99 # Another neighbor's house is 99 feet tall
    total_height = neighbor_house_1_height + lucille_house_height + neighbor_house_2_height

    # L2
    number_of_houses = 3 # WK
    average_height = total_height / number_of_houses

    # L3
    height_difference = average_height - lucille_house_height

    # FA
    answer = height_difference
    return answer