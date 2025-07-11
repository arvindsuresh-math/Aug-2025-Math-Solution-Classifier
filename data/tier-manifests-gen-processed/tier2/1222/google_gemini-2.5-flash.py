def solve():
    """Index: 1222.
    Returns: Wendy's total sales for the day.
    """
    # L1
    morning_apples = 40 # average of 40 apples
    afternoon_apples = 50 # sell 50 apples
    total_apples = morning_apples + afternoon_apples

    # L2
    morning_oranges = 30 # 30 oranges
    afternoon_oranges = 40 # 40 oranges
    total_oranges = morning_oranges + afternoon_oranges

    # L3
    apple_price = 1.50 # an apple at $1.50 each
    sales_apples = total_apples * apple_price

    # L4
    orange_price = 1 # one orange at $1
    sales_oranges = total_oranges * orange_price

    # L5
    total_sales = sales_apples + sales_oranges

    # FA
    answer = total_sales
    return answer