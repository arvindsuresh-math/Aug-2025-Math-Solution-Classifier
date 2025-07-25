def solve():
    """Index: 4115.
    Returns: the number of additional batches of cookies Linda needs to bake.
    """
    # L1
    num_classmates = 24 # 24 classmates
    cookies_per_student = 10 # give each student 10 cookies
    total_cookies_needed = num_classmates * cookies_per_student

    # L2
    dozens_per_batch = 4 # Each cookie recipe made exactly 4 dozen cookies
    cookies_per_dozen = 12 # WK
    cookies_per_batch = dozens_per_batch * cookies_per_dozen

    # L3
    chocolate_chip_batches = 2 # 2 batches of chocolate chip cookies
    oatmeal_raisin_batches = 1 # 1 batch of oatmeal raisin cookies
    total_batches_baked = chocolate_chip_batches + oatmeal_raisin_batches

    # L4
    total_cookies_baked = total_batches_baked * cookies_per_batch

    # L5
    remaining_cookies_needed = total_cookies_needed - total_cookies_baked

    # L6
    additional_batches_needed = remaining_cookies_needed / cookies_per_batch

    # FA
    answer = additional_batches_needed
    return answer