def solve():
    """Index: 981.
    Returns: the combined number of stripes on all of their pairs of tennis shoes.
    """
    # L1
    olga_stripes = 3 # three stripes on the side of each of her tennis shoes
    rick_less_than_olga = 1 # one less stripe per shoe than does Olga
    rick_stripes = olga_stripes - rick_less_than_olga

    # L2
    hortense_double_olga = 2 # double the number of stripes on her tennis shoes as does Olga
    hortense_stripes = olga_stripes * hortense_double_olga

    # L3
    shoes_per_pair = 2 # two tennis shoes per pair
    total_stripes = shoes_per_pair * (olga_stripes + rick_stripes + hortense_stripes)

    # FA
    answer = total_stripes
    return answer