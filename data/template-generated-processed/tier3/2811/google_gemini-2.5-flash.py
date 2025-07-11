def solve():
    """Index: 2811.
    Returns: the number of baby mice Brenda had left.
    """
    # L1
    num_litters = 3 # three litters
    mice_per_litter = 8 # 8 each
    total_baby_mice = num_litters * mice_per_litter

    # L2
    robbie_fraction_denominator = 6 # a sixth of the baby mice
    mice_given_to_robbie = total_baby_mice / robbie_fraction_denominator

    # L3
    pet_store_multiplier = 3 # three times the number of babies she gave Robbie
    mice_sold_to_pet_store = pet_store_multiplier * mice_given_to_robbie

    # L4
    mice_remaining_after_sales = total_baby_mice - mice_sold_to_pet_store - mice_given_to_robbie

    # L5
    feeder_mice_divisor = 2 # Half of the remaining mice
    feeder_mice_sold = mice_remaining_after_sales / feeder_mice_divisor

    # L6
    final_mice_left = mice_remaining_after_sales - feeder_mice_sold

    # FA
    answer = final_mice_left
    return answer