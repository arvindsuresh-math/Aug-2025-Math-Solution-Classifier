from fractions import Fraction

def solve():
    """Index: 3669.
    Returns: the total number of ice creams that were not sold.
    """
    # L1
    chocolate_initial = 50 # 50 chocolate-flavored ice creams
    mango_initial = 54 # 54 mango-flavored ice creams
    total_initial_ice_creams = chocolate_initial + mango_initial

    # L2
    chocolate_sold_fraction = Fraction(3, 5) # sold 3/5 of the chocolate-flavored ice creams
    chocolate_sold = chocolate_initial * chocolate_sold_fraction

    # L3
    mango_sold_fraction = Fraction(2, 3) # and 2/3 of the mango-flavored ice creams
    mango_sold = mango_initial * mango_sold_fraction

    # L4
    total_sold_ice_creams = chocolate_sold + mango_sold

    # L5
    total_not_sold_ice_creams = total_initial_ice_creams - total_sold_ice_creams

    # FA
    answer = total_not_sold_ice_creams
    return answer