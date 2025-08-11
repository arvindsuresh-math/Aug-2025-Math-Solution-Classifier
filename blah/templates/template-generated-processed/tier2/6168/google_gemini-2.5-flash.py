def solve():
    """Index: 6168.
    Returns: the total earnings for apples and oranges.
    """
    # L1
    initial_apples = 50 # 50 apples
    remaining_apples = 10 # only 10 apples
    apples_sold = initial_apples - remaining_apples

    # L2
    initial_oranges = 40 # 40 oranges
    remaining_oranges = 6 # 6 oranges left
    oranges_sold = initial_oranges - remaining_oranges

    # L3
    cost_per_apple = 0.80 # an apple costs $0.80
    apple_sales = cost_per_apple * apples_sold

    # L4
    cost_per_orange = 0.50 # an orange costs $0.50
    orange_sales = cost_per_orange * oranges_sold

    # L5
    total_earnings = apple_sales + orange_sales

    # FA
    answer = total_earnings
    return answer