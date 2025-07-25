def solve():
    """Index: 4393.
    Returns: the total money Hallie makes from her art.
    """
    # L1
    paintings_sold = 3 # sells 3 of her paintings
    price_per_painting = 50 # for $50 each
    money_from_paintings = paintings_sold * price_per_painting

    # L2
    contest_prize = 150 # receives a $150 prize
    total_money = contest_prize + money_from_paintings

    # FA
    answer = total_money
    return answer