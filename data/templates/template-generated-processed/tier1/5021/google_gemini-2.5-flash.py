def solve():
    """Index: 5021.
    Returns: the amount of money Jesse had left after going to the mall.
    """
    # L1
    novel_cost = 7 # novel that costs her $7

    # L2
    lunch_multiplier = 2 # twice as much as the novel cost her
    lunch_cost = novel_cost * lunch_multiplier

    # L3
    total_spent = novel_cost + lunch_cost

    # L4
    initial_gift = 50 # $50 as a gift
    money_left = initial_gift - total_spent

    # FA
    answer = money_left
    return answer