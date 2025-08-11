def solve():
    """Index: 4421.
    Returns: the amount of additional money required to buy the card.
    """
    # L1
    patricia_money = 6 # Patricia has $6
    lisa_multiplier = 5 # five times Patricia’s money
    lisa_money = patricia_money * lisa_multiplier

    # L2
    charlotte_divisor = 2 # double Charlotte’s
    charlotte_money = lisa_money / charlotte_divisor

    # L3
    total_money_collected = patricia_money + lisa_money + charlotte_money

    # L4
    card_cost = 100 # rare baseball card for $100
    money_required = card_cost - total_money_collected

    # FA
    answer = money_required
    return answer