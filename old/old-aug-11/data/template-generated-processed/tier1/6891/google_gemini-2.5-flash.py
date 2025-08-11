def solve():
    """Index: 6891.
    Returns: the total number of fish filets Ben and his family will have.
    """
    # L1
    ben_caught = 4 # Ben caught 4 fish
    judy_caught = 1 # his wife Judy caught 1 fish
    billy_caught = 3 # his oldest son Billy caught 3
    jim_caught = 2 # his younger son Jim caught 2
    susie_caught = 5 # his youngest child Susie surprised them all by catching 5!
    total_fish_caught = ben_caught + judy_caught + billy_caught + jim_caught + susie_caught

    # L2
    fish_too_small = 3 # 3 of the fish were too small
    fish_kept = total_fish_caught - fish_too_small

    # L3
    filets_per_fish = 2 # each fish will give them 2 filets
    total_filets = fish_kept * filets_per_fish

    # FA
    answer = total_filets
    return answer