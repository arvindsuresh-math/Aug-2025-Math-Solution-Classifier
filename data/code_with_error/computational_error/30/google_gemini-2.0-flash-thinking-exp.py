def solve(
    pieces_per_pizza: int = 4, # cut into 4 pieces
    percent_eaten_bill_dale: float = 0.50, # Bill and Dale eat 50%
    percent_eaten_ann_cate: float = 0.75, # Ann and Cate eat 75%
    num_people: int = 4, # Ann, Bill, Cate, and Dale each buy personal pan pizzas
    num_bill_dale: int = 2, # Bill and Dale
    num_ann_cate: int = 2 # Ann and Cate
):
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """

    #: L1
    total_pizza_pieces = num_people * pieces_per_pizza

    #: L2
    pieces_eaten_bill_dale = num_bill_dale * pieces_per_pizza * percent_eaten_bill_dale

    #: L3
    pieces_eaten_ann_cate = -4.0

    #: L4
    total_pieces_eaten = pieces_eaten_bill_dale + pieces_eaten_ann_cate

    #: L5
    pieces_left_uneaten = total_pizza_pieces - total_pieces_eaten

    #: FA
    answer = pieces_left_uneaten
    return answer