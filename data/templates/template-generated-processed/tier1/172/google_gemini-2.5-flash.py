def solve():
    """Index: 172.
    Returns: the total number of stars Kyle must make to fill all the glass bottles.
    """
    # L1
    initial_bottles = 2 # 2 glass bottles
    additional_bottles = 3 # another 3 identical glass bottles
    total_bottles = initial_bottles + additional_bottles

    # L2
    stars_per_bottle = 15 # can hold 15 origami stars each
    total_stars = stars_per_bottle * total_bottles

    # FA
    answer = total_stars
    return answer