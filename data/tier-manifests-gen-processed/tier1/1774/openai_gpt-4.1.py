def solve():
    """Index: 1774.
    Returns: the number of people who can taste Sedrach's apple pies if all are divided into bite-size samples.
    """
    # L1
    bite_sizes_per_half = 5 # every half an apple pie can be split into 5 bite-size samples
    halves_per_pie = 2 # every apple pie can be quickly divided into halves
    bite_sizes_per_pie = bite_sizes_per_half * halves_per_pie

    # L2
    num_pies = 13 # Sedrach has 13 apple pies
    total_bite_sizes = num_pies * bite_sizes_per_pie

    # FA
    answer = total_bite_sizes
    return answer