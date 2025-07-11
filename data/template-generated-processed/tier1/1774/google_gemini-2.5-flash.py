def solve():
    """Index: 1774.
    Returns: the number of people who can taste Sedrach's apple pie.
    """
    # L1
    samples_per_half = 5 # every half an apple pie can be split into 5 bite-size samples
    halves_per_pie = 2 # WK
    bite_sizes_per_pie = samples_per_half * halves_per_pie

    # L2
    num_apple_pies = 13 # 13 apple pies
    total_people_can_taste = num_apple_pies * bite_sizes_per_pie

    # FA
    answer = total_people_can_taste
    return answer