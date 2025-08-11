def solve():
    """Index: 6326.
    Returns: the amount of money Ali had left.
    """
    # L1
    initial_money = 480 # Ali has $480
    food_divisor = 2 # half of it on food
    spent_on_food = initial_money / food_divisor

    # L2
    money_left_after_food = initial_money - spent_on_food

    # L3
    glasses_divisor = 3 # a third of what was left on a pair of glasses
    spent_on_glasses = money_left_after_food / glasses_divisor

    # L4
    final_money_left = money_left_after_food - spent_on_glasses

    # FA
    answer = final_money_left
    return answer