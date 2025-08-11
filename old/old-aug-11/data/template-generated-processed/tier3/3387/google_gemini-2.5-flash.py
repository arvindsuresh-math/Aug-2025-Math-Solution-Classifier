def solve():
    """Index: 3387.
    Returns: the total volume of milk Bryan bought in liters.
    """
    # L1
    volume_bottle_2_ml = 750 # 750 milliliters
    volume_bottle_3_ml = 250 # 250 milliliters
    total_smaller_bottles_ml = volume_bottle_2_ml + volume_bottle_3_ml

    # L2
    ml_per_liter = 1000 # 1 liter is equal to 1000 milliliters
    total_smaller_bottles_liters = total_smaller_bottles_ml / ml_per_liter

    # L3
    volume_bottle_1_liters = 2 # 2 liters
    total_milk_liters = volume_bottle_1_liters + total_smaller_bottles_liters

    # FA
    answer = total_milk_liters
    return answer