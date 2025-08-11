def solve():
    """Index: 4080.
    Returns: the number of cookies each person in Karen's class will receive.
    """
    # L1
    initial_cookies = 50 # Karen bakes 50 chocolate chip cookies
    cookies_kept = 10 # She keeps 10 for herself
    cookies_after_keeping = initial_cookies - cookies_kept

    # L2
    cookies_given_to_grandparents = 8 # she gives 8 to her grandparents
    cookies_after_grandparents = cookies_after_keeping - cookies_given_to_grandparents

    # L3
    num_people_in_class = 16 # there are 16 people in her class
    cookies_per_person = cookies_after_grandparents / num_people_in_class

    # FA
    answer = cookies_per_person
    return answer