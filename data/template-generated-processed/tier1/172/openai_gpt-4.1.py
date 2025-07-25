def solve():
    """Index: 172.
    Returns: the total number of origami stars Kyle must make to fill all the bottles he bought.
    """
    # L1
    bottles_first = 2 # bought 2 glass bottles
    bottles_second = 3 # bought another 3 identical glass bottles
    total_bottles = bottles_first + bottles_second

    # L2
    stars_per_bottle = 15 # can hold 15 origami stars each
    total_stars = stars_per_bottle * total_bottles

    # FA
    answer = total_stars
    return answer