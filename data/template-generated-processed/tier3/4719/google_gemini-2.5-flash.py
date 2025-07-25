def solve():
    """Index: 4719.
    Returns: the amount of money Sid spent on computer accessories.
    """
    # L1
    original_money = 48 # Sid takes $48 with him
    half_divisor = 2 # half of his original money
    half_original_money = original_money / half_divisor

    # L2
    additional_money_left = 4 # only has $4 more than half of his original money left
    money_left_after_purchases = half_original_money + additional_money_left

    # L3
    spent_on_snacks = 8 # another $8 on snacks
    money_before_snacks = money_left_after_purchases + spent_on_snacks

    # L4
    spent_on_accessories = original_money - money_before_snacks

    # FA
    answer = spent_on_accessories
    return answer