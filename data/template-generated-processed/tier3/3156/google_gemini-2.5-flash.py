def solve():
    """Index: 3156.
    Returns: the number of chocolate chips each family member eats.
    """
    # L1
    cookies_per_batch = 12 # Each batch contains 12 cookies
    num_batches = 3 # She made three batches
    total_cookies = cookies_per_batch * num_batches

    # L2
    chocolate_chips_per_cookie = 2 # Each cookie contains 2 chocolate chips
    total_chocolate_chips = total_cookies * chocolate_chips_per_cookie

    # L3
    num_family_members = 4 # His family has 4 total people
    chips_per_family_member = total_chocolate_chips / num_family_members

    # FA
    answer = chips_per_family_member
    return answer