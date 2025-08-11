def solve():
    """Index: 1406.
    Returns: the actual number of toddlers at the daycare.
    """
    # L1
    bill_counted = 26 # Bill thinks he counted 26 toddlers
    double_counted = 8 # He double-counts 8 toddlers
    after_double_count = bill_counted - double_counted

    # L2
    missed = 3 # misses 3 who are hiding
    real_count = after_double_count + missed

    # FA
    answer = real_count
    return answer