def solve():
    """Index: 1306.
    Returns: the amount of money Anna had left after shopping at the candy store.
    """
    # L1
    num_gum_packs = 3 # 3 packs of chewing gum
    gum_price = 1 # $1.00 each
    gum_total = num_gum_packs * gum_price

    # L2
    num_chocolate_bars = 5 # 5 chocolate bars
    chocolate_price = 1 # $1 each
    chocolate_total = num_chocolate_bars * chocolate_price

    # L3
    num_candy_canes = 2 # 2 large candy canes
    candy_cane_price = 0.50 # $0.50 each
    candy_cane_total = num_candy_canes * candy_cane_price

    # L4
    total_spent = gum_total + chocolate_total + candy_cane_total

    # L5
    starting_money = 10 # Anna had $10 to start
    money_left = starting_money - total_spent

    # FA
    answer = money_left
    return answer