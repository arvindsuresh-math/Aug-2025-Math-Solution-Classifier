def solve():
    """Index: 3316.
    Returns: the amount of candy the friend had after eating some.
    """
    # L1
    candies_left_after_eating = 50 # 50 candies left in a bowl
    candies_eaten_previous_week = 20 # Shelly ate 20 candies the previous week
    candies_before_eating = candies_left_after_eating + candies_eaten_previous_week

    # L2
    friend_multiplier = 2 # bringing twice as much candy
    friend_brought_candies = friend_multiplier * candies_before_eating

    # L3
    total_candies_in_bowl = friend_brought_candies + candies_left_after_eating

    # L4
    number_of_people = 2 # divide them equally
    candies_per_person = total_candies_in_bowl / number_of_people

    # L5
    friend_eats_candies = 10 # eating 10 of her candies
    friend_candies_remaining = candies_per_person - friend_eats_candies

    # FA
    answer = friend_candies_remaining
    return answer