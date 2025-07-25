from fractions import Fraction

def solve():
    """Index: 1413.
    Returns: the total amount Maria earned over three days.
    """
    # L1
    first_day_tulips = 30 # she sold 30 tulips
    doubling_factor = 2 # doubled the previous day's sales
    second_day_tulips = first_day_tulips * doubling_factor

    # L2
    first_day_roses = 20 # and 20 roses
    second_day_roses = first_day_roses * doubling_factor

    # L3
    third_day_tulip_percentage = Fraction(10, 100) # sold only 10% of the tulips sold on the second day
    third_day_tulips = third_day_tulip_percentage * second_day_tulips

    # L4
    total_tulips_sold = first_day_tulips + second_day_tulips + third_day_tulips

    # L5
    third_day_roses = 16 # and 16 roses
    total_roses_sold = first_day_roses + second_day_roses + third_day_roses

    # L6
    tulip_price = 2 # The price of one tulip is $2
    tulip_earnings = total_tulips_sold * tulip_price

    # L7
    rose_price = 3 # and one rose is $3
    rose_earnings = total_roses_sold * rose_price

    # L8
    total_earnings = tulip_earnings + rose_earnings

    # FA
    answer = total_earnings
    return answer