from fractions import Fraction

def solve():
    """Index: 3619.
    Returns: the final price of the coffee and cheesecake set.
    """
    # L1
    cheesecake_price = 10 # a piece of cheesecake $10
    coffee_price = 6 # one cup of coffee is $6
    total_initial_price = cheesecake_price + coffee_price

    # L2
    discount_percentage = Fraction(25, 100) # a 25% discount
    discount_amount = discount_percentage * total_initial_price

    # L3
    final_price = total_initial_price - discount_amount

    # FA
    answer = final_price
    return answer