def solve():
    """Index: 6280.
    Returns: the percentage chance of picking a pepperjack cheese stick.
    """
    # L1
    cheddar_sticks = 15 # 15 of the sticks are cheddar
    mozzarella_sticks = 30 # 30 are mozzarella
    pepperjack_sticks = 45 # and 45 are pepperjack
    total_cheese_sticks = cheddar_sticks + mozzarella_sticks + pepperjack_sticks

    # L2
    percentage_multiplier = 100 # multiply by 100%
    percentage_chance = (pepperjack_sticks / total_cheese_sticks) * percentage_multiplier

    # FA
    answer = percentage_chance
    return answer