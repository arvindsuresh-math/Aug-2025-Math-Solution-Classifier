def solve():
    """Index: 749.
    Returns: how many more erasers Anya has than Andrea.
    """
    # L1
    anya_multiplier = 4 # 4 times as many erasers
    andrea_erasers = 4 # Andrea has 4 erasers
    anya_erasers = anya_multiplier * andrea_erasers

    # L2
    difference_erasers = anya_erasers - andrea_erasers

    # FA
    answer = difference_erasers
    return answer