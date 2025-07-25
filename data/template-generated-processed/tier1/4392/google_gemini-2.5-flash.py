def solve():
    """Index: 4392.
    Returns: the total number of street lights in the town.
    """
    # L1
    lights_per_side = 250 # 250 street lights on each opposite side
    num_sides = 2 # WK
    lights_per_road = lights_per_side * num_sides

    # L2
    roads_per_neighborhood = 4 # four roads passing through them
    lights_per_neighborhood = lights_per_road * roads_per_neighborhood

    # L3
    num_neighborhoods = 10 # ten neighborhoods
    total_lights_town = lights_per_neighborhood * num_neighborhoods

    # FA
    answer = total_lights_town
    return answer