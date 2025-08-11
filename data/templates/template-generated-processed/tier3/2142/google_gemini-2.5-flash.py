def solve():
    """Index: 2142.
    Returns: the number of pounds of seaweed fed to livestock.
    """
    # L1
    total_seaweed_pounds = 400 # Carson harvests 400 pounds of seaweed
    fire_seaweed_divisor = 2 # 50% of the seaweed is only good for starting fires
    seaweed_not_for_fire = total_seaweed_pounds / fire_seaweed_divisor

    # L2
    human_food_divisor = 4 # 25% of what's left can be eaten by humans
    seaweed_for_humans = seaweed_not_for_fire / human_food_divisor

    # L3
    seaweed_for_livestock = seaweed_not_for_fire - seaweed_for_humans

    # FA
    answer = seaweed_for_livestock
    return answer