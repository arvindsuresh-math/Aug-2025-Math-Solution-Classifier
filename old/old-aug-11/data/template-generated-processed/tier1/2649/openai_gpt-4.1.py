def solve():
    """Index: 2649.
    Returns: the total amount Ivan paid for ten Uno Giant Family Cards after discount.
    """
    # L1
    original_price = 12 # an Uno Giant Family Card costs $12
    discount_per_card = 2 # discount of $2 each
    discounted_price = original_price - discount_per_card

    # L2
    num_cards = 10 # Ivan bought ten pieces
    total_paid = discounted_price * num_cards

    # FA
    answer = total_paid
    return answer