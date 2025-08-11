def solve():
    """Index: 3954.
    Returns: the total number of building blocks Jesse started with.
    """
    # L1
    building_blocks_building = 80 # builds a building with 80 building blocks
    building_blocks_farmhouse = 123 # builds a farmhouse with 123 building blocks
    building_blocks_fenced_area = 57 # made of 57 building blocks
    total_blocks_built = building_blocks_building + building_blocks_farmhouse + building_blocks_fenced_area

    # L2
    blocks_left = 84 # has 84 building blocks left
    total_blocks_started_with = total_blocks_built + blocks_left

    # FA
    answer = total_blocks_started_with
    return answer