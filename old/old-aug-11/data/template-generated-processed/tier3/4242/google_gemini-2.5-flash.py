def solve():
    """Index: 4242.
    Returns: the total number of comics in the box.
    """
    # L1
    total_pages_found = 150 # 150 pages on the floor
    pages_per_comic = 25 # Each comic has 25 pages
    fixed_comics = total_pages_found / pages_per_comic

    # L2
    untorn_comics = 5 # 5 untorn comics in the box
    total_comics_in_box = fixed_comics + untorn_comics

    # FA
    answer = total_comics_in_box
    return answer