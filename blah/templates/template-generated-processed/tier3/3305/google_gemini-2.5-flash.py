from fractions import Fraction

def solve():
    """Index: 3305.
    Returns: the amount of money Du Chin remains with after setting aside money for buying ingredients.
    """
    # L1
    num_pies = 200 # 200 meat pies
    price_per_pie = 20 # $20 each
    total_sales = num_pies * price_per_pie

    # L2
    ingredient_fraction = Fraction(3, 5) # 3/5 of the sales
    money_for_ingredients = ingredient_fraction * total_sales

    # L3
    remaining_money = total_sales - money_for_ingredients

    # FA
    answer = remaining_money
    return answer