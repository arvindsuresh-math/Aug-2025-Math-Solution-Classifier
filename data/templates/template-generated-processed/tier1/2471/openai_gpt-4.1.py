def solve():
    """Index: 2471.
    Returns: the total amount John pays for the hotel after the discount.
    """
    # L1
    nightly_rate = 250 # $250 a night
    num_nights = 3 # 3 nights
    total_cost = nightly_rate * num_nights

    # L2
    discount = 100 # $100 discount
    final_payment = total_cost - discount

    # FA
    answer = final_payment
    return answer