def solve():
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """
    # L1
    num_people = 4 # Ann, Bill, Cate, and Dale each buy
    pieces_per_pizza = 4 # pizzas cut into 4 pieces
    total_pieces = num_people * pieces_per_pizza

    # L2
    bill_dale_count = 2 # Bill and Dale
    bill_dale_percent_num = 50 # 50% of their pizzas
    percent_factor = 0.01 # WK
    bill_dale_eaten = bill_dale_count * pieces_per_pizza * bill_dale_percent_num * percent_factor

    # L3
    ann_cate_count = 2 # Ann and Cate
    ann_cate_percent_num = 75 # 75% of the pizzas
    ann_cate_eaten = ann_cate_count * pieces_per_pizza * ann_cate_percent_num * percent_factor

    # L4
    total_eaten = bill_dale_eaten + ann_cate_eaten

    # L5
    uneaten_pieces = total_pieces - total_eaten

    # FA
    answer = uneaten_pieces
    return answer