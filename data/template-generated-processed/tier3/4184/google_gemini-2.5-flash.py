def solve():
    """Index: 4184.
    Returns: the number of gnomes with red hats that have small noses.
    """
    # L1
    total_gnomes = 28 # There are 28 garden gnomes in a yard
    half_divisor = 2 # Half the garden gnomes
    gnomes_with_big_noses = total_gnomes / half_divisor

    # L2
    red_hat_numerator = 3 # Three-fourths of them have red hats
    red_hat_denominator = 4 # Three-fourths of them have red hats
    gnomes_with_red_hats = total_gnomes * red_hat_numerator / red_hat_denominator

    # L3
    blue_hat_big_nose_gnomes = 6 # If six gnomes with blue hats have big noses
    red_hat_big_nose_gnomes = gnomes_with_big_noses - blue_hat_big_nose_gnomes

    # L4
    red_hat_small_nose_gnomes = gnomes_with_red_hats - red_hat_big_nose_gnomes

    # FA
    answer = red_hat_small_nose_gnomes
    return answer