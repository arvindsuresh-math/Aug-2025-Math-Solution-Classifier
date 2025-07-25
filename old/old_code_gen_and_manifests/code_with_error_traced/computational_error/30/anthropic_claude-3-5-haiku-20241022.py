def solve(
        num_people: int = 4,  # Ann, Bill, Cate, and Dale
        pieces_per_pizza: int = 4,  # personal pan pizzas cut into 4 pieces
        bill_dale_percent_eaten: float = 0.5,  # Bill and Dale eat 50% of their pizzas
        ann_cate_percent_eaten: float = 0.75  # Ann and Cate eat 75% of the pizzas
    ):
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """

    #: L1
    total_pizza_pieces = num_people * pieces_per_pizza # eval: 16 = 4 * 4

    #: L2
    bill_dale_pieces_eaten = -6.0 # eval: -6.0 = -6.0

    #: L3
    ann_cate_pieces_eaten = 2 * pieces_per_pizza * ann_cate_percent_eaten # eval: 6.0 = 2 * 4 * 0.75

    #: L4
    total_pieces_eaten = bill_dale_pieces_eaten + ann_cate_pieces_eaten # eval: 0.0 = -6.0 + 6.0

    #: L5
    pieces_left_uneaten = total_pizza_pieces - total_pieces_eaten # eval: 16.0 = 16 - 0.0

    #: FA
    answer = pieces_left_uneaten
    return answer # eval: return 16.0
