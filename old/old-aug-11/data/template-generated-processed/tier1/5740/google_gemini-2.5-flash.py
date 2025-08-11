def solve():
    """Index: 5740.
    Returns: the total number of eBook readers John and Anna have altogether.
    """
    # L1
    anna_readers = 50 # Anna bought 50 eBook readers
    john_less_than_anna = 15 # John bought 15 eBook readers less than Anna did
    john_bought = anna_readers - john_less_than_anna

    # L2
    john_lost = 3 # John lost 3 eBook readers
    john_remaining = john_bought - john_lost

    # L3
    total_readers = anna_readers + john_remaining

    # FA
    answer = total_readers
    return answer