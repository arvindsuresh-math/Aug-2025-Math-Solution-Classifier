def solve():
    """Index: 192.
    Returns: the average cost across all products sold today.
    """
    # L1
    num_iphones = 100 # 100 iPhones
    cost_per_iphone = 1000 # average cost of $1000
    iphone_sales = num_iphones * cost_per_iphone

    # L2
    num_ipads = 20 # 20 iPads
    cost_per_ipad = 900 # average cost of $900
    ipad_sales = num_ipads * cost_per_ipad

    # L3
    num_apple_tvs = 80 # 80 Apple TVs
    cost_per_apple_tv = 200 # average cost of $200
    apple_tv_sales = num_apple_tvs * cost_per_apple_tv

    # L4
    total_sales = iphone_sales + ipad_sales + apple_tv_sales

    # L5
    total_products_sold = num_iphones + num_ipads + num_apple_tvs

    # L6
    average_cost_per_product = total_sales / total_products_sold

    # FA
    answer = average_cost_per_product
    return answer