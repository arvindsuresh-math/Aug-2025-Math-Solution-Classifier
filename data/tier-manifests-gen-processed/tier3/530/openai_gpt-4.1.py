def solve():
    """Index: 530.
    Returns: the total number of desserts each person will get.
    """
    # L1
    total_cookies = 42 # She has 42 cookies
    total_people = 7 # There are 7 people in her family
    cookies_per_person = total_cookies / total_people

    # L2
    total_candy = 63 # She also has 63 pieces of candy
    candy_per_person = total_candy / total_people

    # L3
    total_brownies = 21 # and 21 brownies
    brownies_per_person = total_brownies / total_people

    # L4
    total_desserts_per_person = cookies_per_person + candy_per_person + brownies_per_person

    # FA
    answer = total_desserts_per_person
    return answer