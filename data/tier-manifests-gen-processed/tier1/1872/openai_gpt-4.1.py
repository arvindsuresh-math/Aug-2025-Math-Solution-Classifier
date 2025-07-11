def solve():
    """Index: 1872.
    Returns: the combined distance all birds have traveled in the two seasons.
    """
    # L1
    distance_jim_disney = 50 # 50 miles apart
    distance_disney_london = 60 # 60 miles apart
    total_distance_per_bird = distance_jim_disney + distance_disney_london

    # L2
    num_birds = 20 # 20 birds migrate
    combined_distance = total_distance_per_bird * num_birds

    # FA
    answer = combined_distance
    return answer