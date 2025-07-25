def solve():
    """Index: 6300.
    Returns: the total number of screens Bennett sold from January to March.
    """
    # L1
    march_sales = 8800 # Bennet sold 8800 window screens in March
    february_fraction_denominator = 4 # a fourth of what he sold in March
    february_sales = march_sales / february_fraction_denominator

    # L2
    january_divisor = 2 # twice as many window screens in February as he sold last month
    january_sales = february_sales / january_divisor

    # L3
    total_sales_jan_to_march = march_sales + february_sales + january_sales

    # FA
    answer = total_sales_jan_to_march
    return answer