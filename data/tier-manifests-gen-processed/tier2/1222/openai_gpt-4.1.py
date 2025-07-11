def solve():
    """Index: 1222.
    Returns: Wendy's total sales for the day.
    """
    # L1
    morning_apples = 40 # sell an average of 40 apples
    afternoon_apples = 50 # sell 50 apples
    total_apples = morning_apples + afternoon_apples

    # L2
    morning_oranges = 30 # 30 oranges
    afternoon_oranges = 40 # 40 oranges
    total_oranges = morning_oranges + afternoon_oranges

    # L3
    apple_price = 1.5 # apple at $1.50 each
    apple_sales = total_apples * apple_price

    # L4
    orange_price = 1 # orange at $1
    orange_sales = total_oranges * orange_price

    # L5
    total_sales = apple_sales + orange_sales

    # FA
    answer = total_sales
    return answer