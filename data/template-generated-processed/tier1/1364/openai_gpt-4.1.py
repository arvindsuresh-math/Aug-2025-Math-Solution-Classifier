def solve():
    """Index: 1364.
    Returns: the total amount Gina will spend on college this year.
    """
    # L1
    num_credits = 14 # taking 14 credits
    cost_per_credit = 450 # cost $450 each
    tuition = num_credits * cost_per_credit

    # L2
    num_books = 5 # 5 textbooks
    cost_per_book = 120 # $120 for each
    textbooks = num_books * cost_per_book

    # L3
    facilities_fee = 200 # $200 facilities fee
    total_cost = tuition + textbooks + facilities_fee

    # FA
    answer = total_cost
    return answer