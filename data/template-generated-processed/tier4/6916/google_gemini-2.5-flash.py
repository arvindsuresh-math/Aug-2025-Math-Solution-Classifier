def solve():
    """Index: 6916.
    Returns: the percent profit after the discount.
    """
    # L1
    book_cost = 50 # If the book costs $50
    markup_percent_num = 30 # 30% above the cost
    percent_divisor = 100 # WK
    markup_profit = book_cost * markup_percent_num / percent_divisor

    # L2
    initial_selling_price = book_cost + markup_profit

    # L3
    discount_percent_num = 10 # a 10% discount
    discount_amount = initial_selling_price * discount_percent_num / percent_divisor

    # L4
    final_selling_price = initial_selling_price - discount_amount

    # L5
    actual_profit = final_selling_price - book_cost

    # L6
    percent_multiplier = 100 # WK
    percent_profit = actual_profit / book_cost * percent_multiplier

    # FA
    answer = percent_profit
    return answer