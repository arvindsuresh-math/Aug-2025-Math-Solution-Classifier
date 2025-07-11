def solve():
    """Index: 2289.
    Returns: the additional amount Connor needs to spend to receive free shipping.
    """
    # L1
    book1_price = 13.00 # Book 1 cost 13.00
    book2_price = 15.00 # Book 2 cost 15.00
    first_two_total = book1_price + book2_price

    # L2
    discount_percent = 0.25 # first two were 25% off
    discount_amount = first_two_total * discount_percent

    # L3
    discounted_first_two_total = first_two_total - discount_amount

    # L4
    book3_price = 10.00 # Book 3 $10.00
    book4_price = 10.00 # Book 4 $10.00
    last_two_total = 2 * book3_price

    # L5
    total_books_cost = discounted_first_two_total + last_two_total

    # L6
    free_shipping_threshold = 50.00 # free shipping over $50.00
    additional_needed = free_shipping_threshold - total_books_cost

    # FA
    answer = additional_needed
    return answer