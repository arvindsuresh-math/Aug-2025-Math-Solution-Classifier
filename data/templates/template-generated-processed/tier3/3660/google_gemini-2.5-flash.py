from fractions import Fraction

def solve():
    """Index: 3660.
    Returns: the number of ice cream cones Marco needs to sell to make a profit.
    """
    # L1
    expense_percentage_numerator = 80 # His expenses are 80% of total sales
    expense_percentage_denominator = 100 # His expenses are 80% of total sales
    expense_fraction = Fraction(expense_percentage_numerator, expense_percentage_denominator)

    # L2
    profit_percentage_numerator = 20 # His profit would be 20/100
    profit_percentage_denominator = 100 # His profit would be 20/100
    profit_fraction = Fraction(profit_percentage_numerator, profit_percentage_denominator)

    # L3
    desired_profit = 200 # make a $200 profit
    profit_fraction_denominator = profit_fraction.denominator
    total_sales = desired_profit * profit_fraction_denominator

    # L4
    cone_price = 5 # ice cream cones are $5 each
    total_cones_sold = total_sales / cone_price

    # FA
    answer = total_cones_sold
    return answer