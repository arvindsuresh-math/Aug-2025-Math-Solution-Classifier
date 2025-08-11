def solve():
    """Index: 3876.
    Returns: the amount of meat sold beyond original plans.
    """
    # L1
    thursday_sales = 210 # On Thursday the Meat Market sold 210kg of ground beef
    friday_multiplier = 2 # On Friday they sold twice that amount
    friday_sales = thursday_sales * friday_multiplier

    # L2
    saturday_sales = 130 # On Saturday they only sold 130kg
    sunday_divisor = 2 # On Sunday they sold half of what they sold Saturday
    sunday_sales = saturday_sales / sunday_divisor

    # L3
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales

    # L4
    planned_sales = 500 # If they originally planned to sell only 500kg
    extra_sales = total_sales - planned_sales

    # FA
    answer = extra_sales
    return answer