def solve():
    """Index: 5378.
    Returns: the total height of the building.
    """
    # L1
    num_first_stories = 10 # The first 10 stories
    height_first_story = 12 # 12 feet tall each
    height_first_section = num_first_stories * height_first_story

    # L2
    total_stories = 20 # a 20 story building
    remaining_stories = total_stories - num_first_stories

    # L3
    taller_by = 3 # 3 feet taller
    height_remaining_story = height_first_story + taller_by

    # L4
    height_remaining_section = height_remaining_story * remaining_stories

    # L5
    total_height = height_first_section + height_remaining_section

    # FA
    answer = total_height
    return answer