from fractions import Fraction

def solve():
    """Index: 538.
    Returns: the price the reseller should sell the bag for to get a 15% profit.
    """
    # L1
    cost_price = 3000 # A luxury bag costs $3000
    profit_percentage = Fraction(15, 100) # 15% profit
    profit = cost_price * profit_percentage

    # L2
    selling_price = cost_price + profit

    # FA
    answer = selling_price
    return answer