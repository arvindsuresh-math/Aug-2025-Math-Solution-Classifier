def solve():
    """Index: 387.
    Returns: the number of sourball candies each person will get.
    """
    # L1
    nellie_candies = 12 # Nellie can eat 12 sourball candies
    jacob_divisor = 2 # half of that number
    jacob_candies = nellie_candies / jacob_divisor

    # L2
    lana_deduction = 3 # three fewer than Jacob
    lana_candies = jacob_candies - lana_deduction

    # L3
    total_eaten_candies = nellie_candies + jacob_candies + lana_candies

    # L4
    initial_candies = 30 # a bucket of 30 candies
    remaining_candies = initial_candies - total_eaten_candies

    # L5
    number_of_people = 3 # they divide the remaining candies in the bucket equally
    candies_per_person = remaining_candies / number_of_people

    # FA
    answer = candies_per_person
    return answer