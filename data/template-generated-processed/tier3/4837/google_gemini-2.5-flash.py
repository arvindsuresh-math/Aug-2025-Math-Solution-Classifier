from fractions import Fraction

def solve():
    """Index: 4837.
    Returns: the total amount Fern pays.
    """
    # L1
    high_heels_price = 60 # one pair of high heels for $60
    ballet_slippers_fraction = Fraction(2, 3) # 2/3rds of the price of the high heels
    cost_one_ballet_slipper = high_heels_price * ballet_slippers_fraction

    # L2
    num_ballet_slippers = 5 # five pairs of ballet slippers
    total_cost_ballet_slippers = cost_one_ballet_slipper * num_ballet_slippers

    # L3
    total_cost = total_cost_ballet_slippers + high_heels_price

    # FA
    answer = total_cost
    return answer