def solve():
    """Index: 1785.
    Returns: the total number of boys and girls.
    """
    # L1
    total_candies = 90 # 90 assorted candies
    lollipop_fraction_denominator = 3 # One-third of the candies
    num_lollipops = total_candies / lollipop_fraction_denominator

    # L2
    num_candy_canes = total_candies - num_lollipops

    # L3
    lollipops_per_boy = 3 # each boy received 3
    num_boys = num_lollipops / lollipops_per_boy

    # L4
    candy_canes_per_girl = 2 # each received 2
    num_girls = num_candy_canes / candy_canes_per_girl

    # L5
    total_boys_and_girls = num_boys + num_girls

    # FA
    answer = total_boys_and_girls
    return answer