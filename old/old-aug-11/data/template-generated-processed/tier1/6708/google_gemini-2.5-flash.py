def solve():
    """Index: 6708.
    Returns: the price Nelly paid for the painting.
    """
    # L1
    multiplier_thrice = 3 # WK
    joe_bid = 160000 # Joe’s bid was $160,000
    thrice_joe_bid = multiplier_thrice * joe_bid

    # L2
    additional_payment = 2000 # paying $2000 more
    nelly_payment = additional_payment + thrice_joe_bid

    # FA
    answer = nelly_payment
    return answer