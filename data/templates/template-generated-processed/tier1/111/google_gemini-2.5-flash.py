def solve():
    """Index: 111.
    Returns: the amount of money Paul had left after shopping.
    """
    # L1
    bread_price = 2 # bread for $2
    juice_multiplier = 2 # two times the price of the bread
    juice_price = juice_multiplier * bread_price

    # L2
    butter_price = 3 # butter for $3
    total_paid = bread_price + butter_price + juice_price

    # L3
    initial_money = 15 # He had $15 for his shopping
    money_left = initial_money - total_paid

    # FA
    answer = money_left
    return answer