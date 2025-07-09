def solve(
    num_people: int = 4, # Ann, Bill, Cate, and Dale
    pieces_per_pizza: int = 4, # pizzas cut into 4 pieces
    num_people_eating_50_percent: int = 2, # Bill and Dale eat 50% of their pizzas
    percent_eaten_by_bill_dale: float = 0.50, # Bill and Dale eat 50% of their pizzas
    num_people_eating_75_percent: int = 2, # Ann and Cate eat 75% of the pizzas
    percent_eaten_by_ann_cate: float = 0.75 # Ann and Cate eat 75% of the pizzas
):
    """Index: 30.
    Returns: the number of pizza pieces left uneaten.
    """

    #: L1
    total_pieces = num_people * pieces_per_pizza # eval: 16 = 4 * 4

    #: L2
    pieces_eaten_by_bill_dale = num_people_eating_50_percent * pieces_per_pizza * percent_eaten_by_bill_dale # eval: 4.0 = 2 * 4 * 0.5

    #: L3
    pieces_eaten_by_ann_cate = num_people_eating_75_percent + pieces_per_pizza * percent_eaten_by_ann_cate # eval: 5.0 = 2 + 4 * 0.75

    #: L4
    total_pieces_eaten = pieces_eaten_by_bill_dale + pieces_eaten_by_ann_cate # eval: 9.0 = 4.0 + 5.0

    #: L5
    uneaten_pieces = total_pieces - total_pieces_eaten # eval: 7.0 = 16 - 9.0

    #: FA
    answer = uneaten_pieces
    return answer # eval: return 7.0
