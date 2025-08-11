def solve():
    """Index: 4323.
    Returns: the number of times a day Sandra should feed the puppies.
    """
    # L1
    total_portions = 105 # 105 portions of formula
    number_of_days = 5 # for 5 days
    daily_portions = total_portions / number_of_days

    # L2
    number_of_puppies = 7 # 7 puppies
    feedings_per_puppy_per_day = daily_portions / number_of_puppies

    # FA
    answer = feedings_per_puppy_per_day
    return answer