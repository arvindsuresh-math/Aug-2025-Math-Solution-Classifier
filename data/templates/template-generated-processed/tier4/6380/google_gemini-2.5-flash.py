def solve():
    """Index: 6380.
    Returns: the difference between the number of black female pigeons and black male pigeons.
    """
    # L1
    total_pigeons = 70 # 70 pigeons that call the park home
    half_fraction_divisor = 2 # Half of the pigeons are black
    black_pigeons = total_pigeons / half_fraction_divisor

    # L2
    black_male_percent = 0.20 # 20 percent of the black pigeons are male
    black_male_pigeons = black_pigeons * black_male_percent

    # L3
    black_female_pigeons = black_pigeons - black_male_pigeons

    # L4
    difference_female_male = black_female_pigeons - black_male_pigeons

    # FA
    answer = difference_female_male
    return answer