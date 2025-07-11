def solve():
    """Index: 313.
    Returns: the total number of toys the boys have together.
    """
    # L1
    bill_toys = 60 # Bill has 60 toys
    half_divisor = 2 # half as many toys
    half_bill_toys = bill_toys / half_divisor

    # L2
    hash_extra_toys = 9 # Hash has nine more than half as many toys
    hash_toys = hash_extra_toys + half_bill_toys

    # L3
    total_toys = bill_toys + hash_toys

    # FA
    answer = total_toys
    return answer