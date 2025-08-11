from fractions import Fraction

def solve():
    """Index: 5390.
    Returns: the number of cups of chocolate-flavored milk tea sold.
    """
    # L1
    total_sales = 50 # total of 50 cups of milk tea
    winter_melon_fraction = Fraction(2, 5) # Two-fifths of their sales are winter melon flavor
    winter_melon_sales = total_sales * winter_melon_fraction

    # L2
    okinawa_fraction = Fraction(3, 10) # three-tenths are Okinawa flavor
    okinawa_sales = total_sales * okinawa_fraction

    # L3
    total_winter_melon_okinawa_sales = winter_melon_sales + okinawa_sales

    # L4
    chocolate_sales = total_sales - total_winter_melon_okinawa_sales

    # FA
    answer = chocolate_sales
    return answer