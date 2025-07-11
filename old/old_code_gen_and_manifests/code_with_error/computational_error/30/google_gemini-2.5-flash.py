def solve(
        num_people: int = 4, # Ann, Bill, Cate, and Dale each buy personal pan pizzas
        pieces_per_pizza: int = 4, # cut into 4 pieces
        bill_dale_eat_percent: float = 0.50, # Bill and Dale eat 50% of their pizzas
        ann_cate_eat_percent: float = 0.75 # Ann and Cate eat 75% of the pizzas
    ):
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """

    #: L1
    total_pizza_pieces = 15

    #: L2
    pieces_eaten_bill_dale = 2 * pieces_per_pizza * bill_dale_eat_percent

    #: L3
    pieces_eaten_ann_cate = 2 * pieces_per_pizza * ann_cate_eat_percent

    #: L4
    total_pieces_eaten = pieces_eaten_bill_dale + pieces_eaten_ann_cate

    #: L5
    uneaten_pizza_pieces = total_pizza_pieces - total_pieces_eaten

    #: FA
    answer = uneaten_pizza_pieces
    return answer