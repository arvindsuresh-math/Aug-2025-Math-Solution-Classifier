def solve():
    """Index: 5361.
    Returns: the number of dishes left for Oliver on the buffet.
    """
    # L1
    total_dishes = 36 # 36 different dishes
    fresh_mango_divisor = 6 # a sixth of its dishes
    dishes_with_fresh_mango = total_dishes / fresh_mango_divisor

    # L2
    mango_salsa_dishes = 3 # mango salsa on three of its dishes
    mango_jelly_dish = 1 # mango jelly in one dish
    total_mango_dishes = mango_salsa_dishes + dishes_with_fresh_mango + mango_jelly_dish

    # L3
    dishes_oliver_can_pick_out = 2 # pick them out of two of the dishes
    dishes_oliver_wont_eat = total_mango_dishes - dishes_oliver_can_pick_out

    # L4
    dishes_left_for_oliver = total_dishes - dishes_oliver_wont_eat

    # FA
    answer = dishes_left_for_oliver
    return answer