def solve():
    """Index: 820.
    Returns: the total amount James paid including his half of the bill and the tip.
    """
    # L1
    steak_egg_price = 16 # steak and egg meal for $16
    chicken_fried_steak_price = 14 # chicken fried steak for $14
    total_meal_cost = steak_egg_price + chicken_fried_steak_price

    # L2
    num_people = 2 # WK (James and his friend)
    james_share = total_meal_cost / num_people

    # L3
    tip_percent = 0.2 # tip 20%
    tip_amount = total_meal_cost * tip_percent

    # L4
    james_total_paid = james_share + tip_amount

    # FA
    answer = james_total_paid
    return answer