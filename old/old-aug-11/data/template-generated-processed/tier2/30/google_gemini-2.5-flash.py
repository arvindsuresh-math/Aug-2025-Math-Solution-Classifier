def solve():
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """
    # L1
    num_people = 4 # Ann, Bill, Cate, and Dale each buy
    pieces_per_pizza = 4 # cut into 4 pieces
    total_pizza_pieces = num_people * pieces_per_pizza

    # L2
    num_people_group1 = 2 # Bill and Dale
    percent_eaten_group1_num = 50 # 50%
    percent_factor = 0.01 # WK
    pieces_eaten_group1 = num_people_group1 * pieces_per_pizza * percent_eaten_group1_num * percent_factor

    # L3
    num_people_group2 = 2 # Ann and Cate
    percent_eaten_group2_num = 75 # 75%
    pieces_eaten_group2 = num_people_group2 * pieces_per_pizza * percent_eaten_group2_num * percent_factor

    # L4
    total_pieces_eaten = pieces_eaten_group1 + pieces_eaten_group2

    # L5
    uneaten_pizza_pieces = total_pizza_pieces - total_pieces_eaten

    # FA
    answer = uneaten_pizza_pieces
    return answer