from fractions import Fraction

def solve():
    """Index: 5241.
    Returns: Chloe's total profit.
    """
    # L1
    cost_per_dozen = 50 # $50 a dozen
    half_dozen_divisor = 2 # half a dozen
    cost_per_half_dozen = cost_per_dozen / half_dozen_divisor

    # L2
    selling_price_half_dozen = 30 # $30 for half a dozen
    profit_per_half_dozen = selling_price_half_dozen - cost_per_half_dozen

    # L3
    total_dozens_sold = 50 # sold 50 dozens
    fraction_half = Fraction(1, 2) # 1/2
    total_half_dozens_sold = total_dozens_sold / fraction_half

    # L4
    total_profit = profit_per_half_dozen * total_half_dozens_sold

    # FA
    answer = total_profit
    return answer