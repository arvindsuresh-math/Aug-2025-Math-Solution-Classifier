def solve():
    """Index: 3955.
    Returns: how much more candy Roger had than Sandra.
    """
    # L1
    sandra_num_bags = 2 # 2 different bags of candy
    sandra_pieces_per_bag = 6 # 6 pieces of candy left
    sandra_total_candy = sandra_num_bags * sandra_pieces_per_bag

    # L2
    roger_bag1_pieces = 11 # 11 pieces left
    roger_bag2_pieces = 3 # 3 pieces left
    roger_total_candy = roger_bag1_pieces + roger_bag2_pieces

    # L3
    roger_more_candy = roger_total_candy - sandra_total_candy

    # FA
    answer = roger_more_candy
    return answer