def solve():
    """Index: 5797.
    Returns: the total money the coffee shop made.
    """
    # L1
    num_coffee_customers = 7 # 7 customers order coffee
    price_per_coffee = 5 # $5 each
    coffee_sales = num_coffee_customers * price_per_coffee

    # L2
    num_tea_customers = 8 # 8 customers order tea
    price_per_tea = 4 # $4 each
    tea_sales = num_tea_customers * price_per_tea

    # L3
    total_sales = coffee_sales + tea_sales

    # FA
    answer = total_sales
    return answer