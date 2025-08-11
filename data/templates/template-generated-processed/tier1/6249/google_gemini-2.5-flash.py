def solve():
    """Index: 6249.
    Returns: the money Raul has left.
    """
    # L1
    num_comics = 8 # 8 comics
    cost_per_comic = 4 # $4
    spent_on_comics = num_comics * cost_per_comic

    # L2
    initial_money = 87 # $87
    money_left = initial_money - spent_on_comics

    # FA
    answer = money_left
    return answer