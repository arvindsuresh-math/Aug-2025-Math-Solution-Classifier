def solve():
    """Index: 443.
    Returns: the amount each of Sab and Dane will earn if they divide their total earnings equally.
    """
    # L1
    num_shoes = 6 # 6 pairs of shoes
    shoe_price = 3 # cost $3 each
    shoes_earning = num_shoes * shoe_price

    # L2
    num_shirts = 18 # 18 shirts
    shirt_price = 2 # cost $2
    shirts_earning = num_shirts * shirt_price

    # L3
    total_earning = shoes_earning + shirts_earning

    # L4
    num_people = 2 # divided their total earning
    earning_each = total_earning / num_people

    # FA
    answer = earning_each
    return answer