from fractions import Fraction

def solve():
    """Index: 3232.
    Returns: Mr. Brown's selling price of the house.
    """
    # L1
    initial_house_value = 100000 # $100,000
    profit_percentage = Fraction(10, 100) # profit of 10%
    grey_profit = initial_house_value * profit_percentage

    # L2
    brown_purchase_price = initial_house_value + grey_profit

    # L3
    loss_percentage = Fraction(10, 100) # a 10% loss
    brown_loss = brown_purchase_price * loss_percentage

    # L4
    brown_selling_price = brown_purchase_price - brown_loss

    # FA
    answer = brown_selling_price
    return answer