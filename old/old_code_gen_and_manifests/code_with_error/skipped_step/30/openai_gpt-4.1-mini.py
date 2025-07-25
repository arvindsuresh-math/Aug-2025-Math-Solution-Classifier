def solve(
    num_people: int = 4,  # Ann, Bill, Cate, and Dale each buy personal pan pizzas
    pieces_per_pizza: int = 4,  # pizzas cut into 4 pieces
    percent_eaten_bill_dale: float = 0.5,  # Bill and Dale eat 50% of their pizzas
    percent_eaten_ann_cate: float = 0.75  # Ann and Cate eat 75% of their pizzas
):
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """

    #: L1
    total_pieces = num_people * pieces_per_pizza

    #: L2
    pieces_eaten_bill_dale = 2 * pieces_per_pizza * percent_eaten_bill_dale

    #: L3
    pieces_eaten_ann_cate = 2 * pieces_per_pizza * percent_eaten_ann_cate

    #: L4

    #: L5
    pieces_uneaten = total_pieces - percent_eaten_ann_cate

    #: FA
    answer = pieces_uneaten
    return answer