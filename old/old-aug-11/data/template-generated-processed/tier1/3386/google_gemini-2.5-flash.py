def solve():
    """Index: 3386.
    Returns: the number of times the poodle barked.
    """
    # L1
    hush_times = 6 # She has to say “hush” six times
    terrier_bark_multiplier = 2 # every second time it barks
    terrier_barks = hush_times * terrier_bark_multiplier

    # L2
    poodle_bark_ratio = 2 # The poodle barks twice for every one time the terrier barks
    poodle_barks = terrier_barks * poodle_bark_ratio

    # FA
    answer = poodle_barks
    return answer