def solve():
    """Index: 4104.
    Returns: the total amount Annie spent on candies.
    """
    # L1
    total_people_in_class = 35 # 35 people in Annie's class
    annie_is_one_person = 1 # WK
    num_classmates = total_people_in_class - annie_is_one_person

    # L2
    candies_per_classmate = 2 # Every classmate got 2 candies
    candies_given_out = num_classmates * candies_per_classmate

    # L3
    candies_left = 12 # Annie got left with 12 candies
    total_candies_initial = candies_given_out + candies_left

    # L4
    cost_per_candy = 0.1 # one candy costs $0.1
    total_cost = total_candies_initial * cost_per_candy

    # FA
    answer = total_cost
    return answer