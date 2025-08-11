def solve():
    """Index: 5133.
    Returns: the amount of money each class received.
    """
    # L1
    entrance_tickets_money = 368 # paid a total of $368 for entrance tickets
    raffle_money = 343 # raffle which brought in $343
    cakes_drinks_money = 279 # sale of cakes and drinks brought $279
    total_money_collected = entrance_tickets_money + raffle_money + cakes_drinks_money

    # L2
    number_of_classes = 5 # 5 classes
    money_per_class = total_money_collected / number_of_classes

    # FA
    answer = money_per_class
    return answer