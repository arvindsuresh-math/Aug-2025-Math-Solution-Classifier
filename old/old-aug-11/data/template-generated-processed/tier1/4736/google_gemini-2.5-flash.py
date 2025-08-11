def solve():
    """Index: 4736.
    Returns: the total banana produce from the two islands that year.
    """
    # L1
    jakies_multiplier = 10 # ten times as many bananas
    nearby_island_produce = 9000 # produced 9000 bananas in a year
    jakies_island_produce = jakies_multiplier * nearby_island_produce

    # L2
    total_produce = jakies_island_produce + nearby_island_produce

    # FA
    answer = total_produce
    return answer