def solve():
    """Index: 1650.
    Returns: the number of cookies Sarah took.
    """
    # L2
    total_neighbors = 15 # her 15 neighbors
    sarah_count = 1 # Sarah
    final_neighbor_count = 1 # final neighbor
    correct_neighbors = total_neighbors - sarah_count - final_neighbor_count
    cookies_per_neighbor = 10 # 10 cookies each
    correct_neighbors_cookies = correct_neighbors * cookies_per_neighbor

    # L3
    total_cookies = 150 # made 150 cookies
    cookies_left = 8 # only 8 cookies left
    cookies_taken_by_14 = total_cookies - cookies_left

    # L4
    sarah_cookies = cookies_taken_by_14 - correct_neighbors_cookies

    # FA
    answer = sarah_cookies
    return answer