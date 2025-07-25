def solve():
    """Index: 192.
    Returns: the average cost across all products sold today.
    """
    # L1
    iphone_count = 100 # Apple sold 100 iPhones
    iphone_avg_cost = 1000 # average cost of $1000
    iphone_sales = iphone_count * iphone_avg_cost

    # L2
    ipad_count = 20 # sold 20 iPads
    ipad_avg_cost = 900 # average cost of $900
    ipad_sales = ipad_count * ipad_avg_cost

    # L3
    appletv_count = 80 # 80 Apple TVs
    appletv_avg_cost = 200 # average cost of $200
    appletv_sales = appletv_count * appletv_avg_cost

    # L4
    total_sales = iphone_sales + ipad_sales + appletv_sales

    # L5
    total_products = iphone_count + ipad_count + appletv_count

    # L6
    average_cost = total_sales / total_products

    # FA
    answer = average_cost
    return answer