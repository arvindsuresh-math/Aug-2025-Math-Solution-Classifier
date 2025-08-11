def solve():
    """Index: 387.
    Returns: the number of sourball candies each person gets after dividing the remaining candies equally.
    """
    # L1
    nellie_candies = 12 # Nellie can eat 12 sourball candies before crying
    jacob_divisor = 2 # Jacob can only manage half of that number
    jacob_candies = nellie_candies / jacob_divisor

    # L2
    lana_difference = 3 # Lana can only do three fewer than Jacob
    lana_candies = jacob_candies - lana_difference

    # L3
    total_eaten = nellie_candies + jacob_candies + lana_candies

    # L4
    initial_bucket = 30 # They had a bucket of 30 candies
    candies_left = initial_bucket - total_eaten

    # L5
    people = 3 # Nellie, Jacob, and Lana
    candies_per_person = candies_left / people

    # FA
    answer = candies_per_person
    return answer