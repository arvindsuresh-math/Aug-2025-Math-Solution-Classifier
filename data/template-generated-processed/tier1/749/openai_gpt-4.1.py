def solve():
    """Index: 749.
    Returns: how many more erasers Anya has than Andrea.
    """
    # L1
    anya_multiplier = 4 # 4 times as many erasers as Andrea
    andrea_erasers = 4 # Andrea has 4 erasers
    anya_erasers = anya_multiplier * andrea_erasers

    # L2
    anya_more_than_andrea = anya_erasers - andrea_erasers

    # FA
    answer = anya_more_than_andrea
    return answer