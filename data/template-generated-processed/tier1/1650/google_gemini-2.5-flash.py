def solve():
    """Index: 1650.
    Returns: the number of cookies Sarah took.
    """
    # L1
    total_neighbors = 15 # her 15 neighbors
    sarah_count = 1 # 1 Sarah
    final_neighbor_count = 1 # 1 final neighbor
    neighbors_took_correct_amount = total_neighbors - sarah_count - final_neighbor_count

    # L2
    correct_cookies_per_neighbor = 10 # 10 cookies each
    cookies_taken_by_correct_neighbors = neighbors_took_correct_amount * correct_cookies_per_neighbor

    # L3
    total_cookies_made = 150 # made 150 cookies
    cookies_left = 8 # only 8 cookies left
    cookies_taken_by_all_except_last = total_cookies_made - cookies_left

    # L4
    sarah_cookies_taken = cookies_taken_by_all_except_last - cookies_taken_by_correct_neighbors

    # FA
    answer = sarah_cookies_taken
    return answer