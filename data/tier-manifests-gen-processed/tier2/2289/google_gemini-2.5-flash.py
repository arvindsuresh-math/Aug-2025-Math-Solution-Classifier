def solve():
    """Index: 2289.
    Returns: how much more money Connor needed to spend to receive free shipping.
    """
    # L1
    book1_cost = 13.00 # Book 1 cost 13.00
    book2_cost = 15.00 # Book 2 cost 15.00
    cost_book1_book2_original = book1_cost + book2_cost

    # L2
    num_discounted_books_text = 2 # the first two were 25% off
    discount_percent_text_val = 25 # 25% off
    discount_percent_decimal = 0.25 # 25% off
    discount_amount = cost_book1_book2_original * discount_percent_decimal

    # L3
    cost_book1_book2_after_discount = cost_book1_book2_original - discount_amount

    # L4
    book3_book4_cost_each = 10.00 # Book 3 & 4 were both $10.00 each
    num_books_3_4 = 2 # Book 3 & 4
    cost_book3_book4 = num_books_3_4 * book3_book4_cost_each

    # L5
    total_num_books = 4 # when you buy 4 books
    total_cost_books = cost_book1_book2_after_discount + cost_book3_book4

    # L6
    free_shipping_threshold = 50.00 # free shipping over $50.00
    money_needed_for_free_shipping = free_shipping_threshold - total_cost_books

    # FA
    answer = money_needed_for_free_shipping
    return answer