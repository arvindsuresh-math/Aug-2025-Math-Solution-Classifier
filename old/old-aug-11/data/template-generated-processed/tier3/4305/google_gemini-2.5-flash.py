from fractions import Fraction

def solve():
    """Index: 4305.
    Returns: the total number of crates of eggs sold over 4 days.
    """
    # L1
    monday_sales = 5 # On Monday she sells 5 crates of eggs
    tuesday_multiplier = 2 # 2 times as many crates of eggs as Monday
    tuesday_sales = monday_sales * tuesday_multiplier

    # L2
    wednesday_fewer = 2 # 2 fewer crates than Tuesday
    wednesday_sales = tuesday_sales - wednesday_fewer

    # L3
    thursday_fraction = Fraction(1, 2) # half as many crates of eggs as she sells on Tuesday
    thursday_sales = thursday_fraction * tuesday_sales

    # L4
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales

    # FA
    answer = total_sales
    return answer