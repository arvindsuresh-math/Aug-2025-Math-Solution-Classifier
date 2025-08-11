def solve():
    """Index: 4010.
    Returns: the number of cookies each person consumes.
    """
    # L1
    num_batches = 4 # 4, 2 dozen batches
    dozen_per_batch = 2 # 2 dozen batches
    total_dozen_batches = num_batches * dozen_per_batch

    # L2
    cookies_per_dozen = 12 # WK
    total_cookies = cookies_per_dozen * total_dozen_batches

    # L3
    num_people = 16 # amongst 16 people equally
    cookies_per_person = total_cookies / num_people

    # FA
    answer = cookies_per_person
    return answer