def solve():
    """Index: 1733.
    Returns: the total number of articles of clothing being donated.
    """
    # L1
    pajama_sets = 4 # 4 pajama sets
    pieces_per_set = 2 # made up of a top and a bottom
    pajama_pieces = pajama_sets * pieces_per_set

    # L2
    pants = 4 # 4 pairs of pants
    jumpers = 4 # 4 jumpers
    t_shirts = 20 # 20 t-shirts
    adam_initial_donation = pants + jumpers + pajama_pieces + t_shirts

    # L3
    num_friends = 3 # 3 of his friends
    friends_total_donation = adam_initial_donation * num_friends

    # L4
    half_divisor = 2 # keep half of his clothes
    adam_final_donation = adam_initial_donation / half_divisor

    # L5
    total_donated_clothing = friends_total_donation + adam_final_donation

    # FA
    answer = total_donated_clothing
    return answer