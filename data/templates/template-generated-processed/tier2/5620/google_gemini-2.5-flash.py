def solve():
    """Index: 5620.
    Returns: the total amount Gordon will spend on books.
    """
    # L1
    book_price_1_over_22 = 25.00 # books with the following prices; $25.00
    book_price_2_over_22 = 35.00 # $35.00
    total_cost_over_22 = book_price_1_over_22 + book_price_2_over_22

    # L2
    discount_rate_over_22 = 0.30 # 30% off
    discount_amount_over_22 = total_cost_over_22 * discount_rate_over_22

    # L3
    final_cost_over_22 = total_cost_over_22 - discount_amount_over_22

    # L4
    book_price_1_under_20 = 18.00 # books with the following prices; $18.00
    book_price_2_under_20 = 12.00 # $12.00
    book_price_3_under_20 = 10.00 # $10.00
    total_cost_under_20 = book_price_1_under_20 + book_price_2_under_20 + book_price_3_under_20

    # L5
    discount_rate_under_20 = 0.20 # 20% off
    discount_amount_under_20 = total_cost_under_20 * discount_rate_under_20

    # L6
    final_cost_under_20 = total_cost_under_20 - discount_amount_under_20

    # L7
    book_price_no_discount = 21.00 # $21.00
    total_spent = final_cost_over_22 + final_cost_under_20 + book_price_no_discount

    # FA
    answer = total_spent
    return answer