def solve():
    """Index: 1568.
    Returns: the total money contributed to the fundraiser.
    """
    # L1
    sasha_muffins = 30 # Sasha made 30 chocolate muffins
    melissa_multiplier = 4 # Melissa made 4 times as many muffins as Sasha
    melissa_muffins = sasha_muffins * melissa_multiplier

    # L2
    sasha_melissa_total_muffins = sasha_muffins + melissa_muffins

    # L3
    tiffany_divisor = 2 # Tiffany made half of Sasha and Melissa's total number of muffins
    tiffany_muffins = sasha_melissa_total_muffins / tiffany_divisor

    # L4
    total_muffins = sasha_melissa_total_muffins + tiffany_muffins

    # L5
    muffin_price = 4 # If one muffin sold for $4
    total_contribution = total_muffins * muffin_price

    # FA
    answer = total_contribution
    return answer