def solve():
    """Index: 4371.
    Returns: the number of pieces of candy that were not chocolate.
    """
    # L1
    total_candy_pieces = 63 # Jerry had 63 pieces of candy
    total_bags = 9 # divided them up equally into 9 bags
    candy_per_bag = total_candy_pieces / total_bags

    # L2
    chocolate_heart_bags = 2 # 2 of the bags had chocolate hearts
    chocolate_hearts_candy = chocolate_heart_bags * candy_per_bag

    # L3
    chocolate_kisses_bags = 3 # 3 of the bags were chocolate kisses
    chocolate_kisses_candy = chocolate_kisses_bags * candy_per_bag

    # L4
    total_chocolate_candy = chocolate_kisses_candy + chocolate_hearts_candy

    # L5
    non_chocolate_candy = total_candy_pieces - total_chocolate_candy

    # FA
    answer = non_chocolate_candy
    return answer