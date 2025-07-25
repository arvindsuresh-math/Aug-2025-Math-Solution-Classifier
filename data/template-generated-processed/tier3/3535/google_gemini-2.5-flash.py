def solve():
    """Index: 3535.
    Returns: the final length of Marcia's hair.
    """
    # L1
    initial_hair_length = 24 # Marcia's hair is 24" long
    cut_fraction_denominator = 2 # cuts half of her hair off
    cut_amount = initial_hair_length / cut_fraction_denominator

    # L2
    hair_after_first_cut = initial_hair_length - cut_amount

    # L3
    growth_amount = 4 # lets it grow out 4 more inches
    hair_after_growth = hair_after_first_cut + growth_amount

    # L4
    second_cut_amount = 2 # cuts off another 2" of hair
    final_hair_length = hair_after_growth - second_cut_amount

    # FA
    answer = final_hair_length
    return answer