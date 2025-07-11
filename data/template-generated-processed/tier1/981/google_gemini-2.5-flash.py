def solve():
    """Index: 981.
    Returns: the combined number of stripes on all of their pairs of tennis shoes.
    """
    # L1
    olga_stripes_per_shoe = 3 # three stripes on the side of each of her tennis shoes
    rick_less_stripes = 1 # one less stripe per shoe
    rick_stripes_per_shoe = olga_stripes_per_shoe - rick_less_stripes

    # L2
    double_factor = 2 # double the number of stripes
    hortense_stripes_per_shoe = olga_stripes_per_shoe * double_factor

    # L3
    shoes_per_pair = 2 # WK
    total_stripes_per_person_per_shoe = olga_stripes_per_shoe + rick_stripes_per_shoe + hortense_stripes_per_shoe
    total_stripes = shoes_per_pair * total_stripes_per_person_per_shoe

    # FA
    answer = total_stripes
    return answer