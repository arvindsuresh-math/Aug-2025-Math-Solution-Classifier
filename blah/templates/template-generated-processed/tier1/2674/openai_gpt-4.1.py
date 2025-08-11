def solve():
    """Index: 2674.
    Returns: the total number of dog toys Daisy would have if all lost and new toys are found.
    """
    # L1
    monday_toys = 5 # Daisy played with 5 dog toys
    tuesday_new_toys = 3 # her owner got her 3 more
    old_and_tuesday_toys = monday_toys + tuesday_new_toys

    # L2
    wednesday_new_toys = 5 # her owner bought her 5 more
    total_toys = wednesday_new_toys + old_and_tuesday_toys

    # FA
    answer = total_toys
    return answer