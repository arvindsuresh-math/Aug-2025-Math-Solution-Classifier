from fractions import Fraction

def solve():
    """Index: 2660.
    Returns: the number of oranges left to be sold today.
    """
    # L1
    seven_dozen = 7 # seven dozen oranges
    dozen = 12 # WK
    total_oranges = seven_dozen * dozen

    # L2
    reserved_fraction = Fraction(1, 4) # 1/4 of it
    reserved_oranges = total_oranges * reserved_fraction

    # L3
    oranges_after_reservation = total_oranges - reserved_oranges

    # L4
    sold_yesterday_fraction = Fraction(3, 7) # 3/7 of the remaining
    oranges_sold_yesterday = oranges_after_reservation * sold_yesterday_fraction

    # L5
    oranges_left_after_sale = oranges_after_reservation - oranges_sold_yesterday

    # L6
    rotten_oranges = 4 # four rotten oranges
    oranges_left_to_sell_today = oranges_left_after_sale - rotten_oranges

    # FA
    answer = oranges_left_to_sell_today
    return answer