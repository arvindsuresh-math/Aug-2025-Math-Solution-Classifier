from fractions import Fraction

def solve():
    """Index: 7259.
    Returns: the total number of cups of lemonade sold for both weeks.
    """
    # L1
    initial_sales = 20 # 20 cups of lemonade last week
    increase_percentage = Fraction(30, 100) # 30% more lemonade this week
    additional_sales_this_week = initial_sales * increase_percentage

    # L2
    sales_this_week = initial_sales + additional_sales_this_week

    # L3
    total_sales = initial_sales + sales_this_week

    # FA
    answer = total_sales
    return answer