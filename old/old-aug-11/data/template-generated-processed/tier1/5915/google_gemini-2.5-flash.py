def solve():
    """Index: 5915.
    Returns: the total number of eggs Michael has now.
    """
    # L1
    initial_crates = 6 # bought 6 crates of egg on Tuesday
    crates_given_out = 2 # gave out 2 crates to Susan
    crates_after_giving_out = initial_crates - crates_given_out

    # L2
    crates_bought_thursday = 5 # bought another 5 crates on Thursday
    total_crates = crates_after_giving_out + crates_bought_thursday

    # L3
    eggs_per_crate = 30 # one crate holds 30 eggs
    total_eggs = eggs_per_crate * total_crates

    # FA
    answer = total_eggs
    return answer