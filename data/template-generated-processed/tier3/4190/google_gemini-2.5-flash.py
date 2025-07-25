def solve():
    """Index: 4190.
    Returns: the amount of money left on Marlon's gift card.
    """
    # L1
    initial_gift_card_amount = 200 # $200
    half_divisor = 2 # half of it
    remaining_after_monday = initial_gift_card_amount / half_divisor

    # L2
    quarter_divisor = 4 # one-fourth of the remainder
    spent_on_tuesday = remaining_after_monday / quarter_divisor

    # L3
    final_remaining_amount = remaining_after_monday - spent_on_tuesday

    # FA
    answer = final_remaining_amount
    return answer