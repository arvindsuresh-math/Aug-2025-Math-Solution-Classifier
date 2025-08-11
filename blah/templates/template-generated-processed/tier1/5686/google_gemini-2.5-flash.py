def solve():
    """Index: 5686.
    Returns: the total money Linda had at the end of the day.
    """
    # L1
    num_tees_sold = 7 # sold 7 tees
    price_per_tee = 8 # tees at 8 dollars each
    cost_of_tees = num_tees_sold * price_per_tee

    # L2
    num_jeans_sold = 4 # sold 4 jeans
    price_per_jean = 11 # jeans at 11 dollars each
    cost_of_jeans = num_jeans_sold * price_per_jean

    # L3
    total_money = cost_of_tees + cost_of_jeans

    # FA
    answer = total_money
    return answer