def solve():
    """Index: 417.
    Returns: the total amount Jim paid for the package of car washes.
    """
    # L1
    num_carwashes = 20 # package of 20 car washes
    package_percent = 0.6 # only has to pay 60%
    paid_carwashes = num_carwashes * package_percent

    # L2
    carwash_price = 15 # carwash normally costs 15 dollars
    total_paid = paid_carwashes * carwash_price

    # FA
    answer = total_paid
    return answer