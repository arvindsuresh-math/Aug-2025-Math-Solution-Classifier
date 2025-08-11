def solve():
    """Index: 1562.
    Returns: the number of friends who receive a candy necklace.
    """
    # L1
    num_blocks_candy = 3 # 3 blocks of candy
    pieces_per_block = 30 # each produce 30 pieces of candy
    total_pieces_candy = num_blocks_candy * pieces_per_block

    # L2
    pieces_per_necklace = 10 # 10 pieces of candies
    total_necklaces = total_pieces_candy / pieces_per_necklace

    # L3
    jan_necklace = 1 # Jan is keeping a candy necklace too
    friends_receive_necklace = total_necklaces - jan_necklace

    # FA
    answer = friends_receive_necklace
    return answer