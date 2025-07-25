def solve():
    """Index: 2100.
    Returns: the amount of money Victoria should return to her mother.
    """
    # L1
    pizza_price = 12 # costs $12 each
    pizza_qty = 2 # 2 boxes of pizza
    pizza_total = pizza_price * pizza_qty

    # L2
    juice_price = 2 # cost $2 each
    juice_qty = 2 # 2 packs of juice drinks
    juice_total = juice_price * juice_qty

    # L3
    total_paid = pizza_total + juice_total

    # L4
    given_money = 50 # given a $50 bill
    money_to_return = given_money - total_paid

    # FA
    answer = money_to_return
    return answer