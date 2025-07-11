from fractions import Fraction

def solve():
    """Index: 973.
    Returns: the amount Mr. Brandon got from cash sales.
    """
    # L1
    credit_sales_fraction = Fraction(2, 5) # 2/5 of the total amount of sales
    total_sales = 80 # goods worth $80
    credit_sales_amount = credit_sales_fraction * total_sales

    # L2
    cash_sales_amount = total_sales - credit_sales_amount

    # FA
    answer = cash_sales_amount
    return answer