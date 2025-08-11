def solve():
    """Index: 6491.
    Returns: the amount James paid for the cable program.
    """
    # L1
    first_100_channels_cost = 100 # The first 100 channels cost $100
    half_divisor = 2 # half that much
    next_100_channels_cost = first_100_channels_cost / half_divisor

    # L2
    total_cost = first_100_channels_cost + next_100_channels_cost

    # L3
    split_divisor = 2 # splits it evenly with his roommate
    james_payment = total_cost / split_divisor

    # FA
    answer = james_payment
    return answer