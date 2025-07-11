def solve():
    """Index: 313.
    Returns: the total number of toys the boys have.
    """
    # L1
    bill_toys = 60 # Bill has 60 toys
    half_divisor = 2 # half as many toys
    half_bill_toys = bill_toys / half_divisor

    # L2
    hash_additional_toys = 9 # nine more
    hash_toys = hash_additional_toys + half_bill_toys

    # L3
    total_toys = bill_toys + hash_toys

    # FA
    answer = total_toys
    return answer