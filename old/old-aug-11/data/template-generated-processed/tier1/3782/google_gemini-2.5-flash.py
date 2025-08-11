def solve():
    """Index: 3782.
    Returns: the total number of treasures Simon found on the beach.
    """
    # L1
    sand_dollars_in_bag = 10 # a bag of ten sand dollars
    multiplier_for_glass = 3 # three times as many pieces of glass as the bag does sand dollars
    pieces_of_glass_in_jar = multiplier_for_glass * sand_dollars_in_bag

    # L2
    multiplier_for_seashells = 5 # five times as many seashells as the jar holds pieces of glass
    seashells_in_bucket = multiplier_for_seashells * pieces_of_glass_in_jar

    # L3
    total_treasures = sand_dollars_in_bag + pieces_of_glass_in_jar + seashells_in_bucket

    # FA
    answer = total_treasures
    return answer