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

    #: L2
    bill_dale_pieces_eaten = 2 * pieces_per_pizza * bill_dale_percent_eaten # eval: 4.0 = 2 * 4 * 0.5

    #: L3
    ann_cate_pieces_eaten = 2 * pieces_per_pizza * ann_cate_percent_eaten # eval: 6.0 = 2 * 4 * 0.75

    #: L4
    total_pieces_eaten = bill_dale_pieces_eaten + ann_cate_pieces_eaten # eval: 10.0 = 4.0 + 6.0

    #: L5
    pieces_left_uneaten = bill_dale_percent_eaten - total_pieces_eaten # eval: -9.5 = 0.5 - 10.0

    #: FA
    answer = pieces_left_uneaten
    return answer # eval: return -9.5
