def solve():
    """Index: 3152.
    Returns: the total number of slices of bread eaten by the guests.
    """
    # L1
    triangles_eaten = 28 # guests ate 28 triangles
    triangles_per_cucumber_sandwich = 4 # Each cucumber sandwich was cut into 4 triangles
    cucumber_sandwiches_eaten = triangles_eaten / triangles_per_cucumber_sandwich

    # L2
    rectangles_eaten = 12 # guests ate 12 rectangles
    rectangles_per_egg_sandwich = 2 # Each egg sandwich was cut into 2 rectangles
    egg_sandwiches_eaten = rectangles_eaten / rectangles_per_egg_sandwich

    # L3
    total_sandwiches_eaten = cucumber_sandwiches_eaten + egg_sandwiches_eaten

    # L4
    slices_per_sandwich = 2 # WK
    total_slices_of_bread_eaten = total_sandwiches_eaten * slices_per_sandwich

    # FA
    answer = total_slices_of_bread_eaten
    return answer