def solve():
    """Index: 5975.
    Returns: the number of 20-pound dog food bags Mike needs to buy a month.
    """
    # L1
    cups_per_feeding = 6 # 6 cups of dog food
    feedings_per_day = 2 # twice a day
    cups_per_dog_per_day = cups_per_feeding * feedings_per_day

    # L2
    number_of_dogs = 2 # 2 dogs
    total_cups_per_day = cups_per_dog_per_day * number_of_dogs

    # L3
    pounds_per_cup_denominator = 4 # 1/4 of a pound
    total_pounds_per_day = total_cups_per_day / pounds_per_cup_denominator

    # L4
    days_per_month = 30 # WK
    total_pounds_per_month = total_pounds_per_day * days_per_month

    # L5
    pounds_per_bag = 20 # 20 pound bags
    num_bags_needed = total_pounds_per_month / pounds_per_bag

    # FA
    answer = num_bags_needed
    return answer