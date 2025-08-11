def solve():
    """Index: 1306.
    Returns: the amount of money Anna had left.
    """
    # L1
    num_gum_packs = 3 # 3 packs of chewing gum
    cost_per_gum_pack = 1.00 # $1.00 each
    cost_gum = num_gum_packs * cost_per_gum_pack

    # L2
    num_chocolate_bars = 5 # 5 chocolate bars
    cost_per_chocolate_bar = 1.00 # $1 each
    cost_chocolate = num_chocolate_bars * cost_per_chocolate_bar

    # L3
    num_candy_canes = 2 # 2 large candy canes
    cost_per_candy_cane = 0.50 # $0.50 each
    cost_candy_canes = num_candy_canes * cost_per_candy_cane

    # L4
    total_spent = cost_gum + cost_chocolate + cost_candy_canes

    # L5
    initial_money = 10.00 # $10.00
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer