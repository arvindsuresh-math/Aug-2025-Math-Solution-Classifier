def solve():
    """Index: 4706.
    Returns: the number of cookies in a batch.
    """
    # L1
    total_chips_in_bag = 81 # A bag of chocolate chips has 81 chips in it
    num_batches = 3 # The dough makes three batches of cookies
    chips_per_batch = total_chips_in_bag / num_batches

    # L2
    chips_per_cookie = 9 # each cookie has nine chocolate chips in it
    cookies_per_batch = chips_per_batch / chips_per_cookie

    # FA
    answer = cookies_per_batch
    return answer