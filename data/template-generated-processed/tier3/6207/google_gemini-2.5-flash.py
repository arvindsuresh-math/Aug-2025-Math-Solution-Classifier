from fractions import Fraction

def solve():
    """Index: 6207.
    Returns: the total amount Andre paid for the treadmill and plates.
    """
    # L1
    treadmill_original_price = 1350 # a $1350 treadmill
    discount_percentage = Fraction(30, 100) # 30% discount
    treadmill_discount = treadmill_original_price * discount_percentage

    # L2
    treadmill_final_price = treadmill_original_price - treadmill_discount

    # L3
    plate_price_per_piece = 50 # $50 each
    number_of_plates = 2 # 2 pieces
    total_plate_cost = plate_price_per_piece * number_of_plates

    # L4
    total_paid = treadmill_final_price + total_plate_cost

    # FA
    answer = total_paid
    return answer