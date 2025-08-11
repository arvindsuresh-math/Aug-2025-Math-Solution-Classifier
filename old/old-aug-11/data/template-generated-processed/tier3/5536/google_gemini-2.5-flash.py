def solve():
    """Index: 5536.
    Returns: the amount of money made from cauliflower sales.
    """
    # L1
    broccoli_sales = 57 # made $57 from broccoli
    carrot_multiplier = 2 # twice as much as the sales of broccoli
    carrot_sales = broccoli_sales * carrot_multiplier

    # L2
    half_divisor = 2 # half of the sales of carrots
    half_carrot_sales = carrot_sales / half_divisor

    # L3
    spinach_additional_amount = 16 # $16 more than half of the sales of carrots
    spinach_sales = half_carrot_sales + spinach_additional_amount

    # L4
    total_sales_other_vegetables = broccoli_sales + carrot_sales + spinach_sales

    # L5
    total_earnings = 380 # made $380
    cauliflower_sales = total_earnings - total_sales_other_vegetables

    # FA
    answer = cauliflower_sales
    return answer