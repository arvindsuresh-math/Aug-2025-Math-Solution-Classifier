def solve():
    """Index: 2730.
    Returns: the number of flowers James planted in a day.
    """
    # L1
    james_count = 1 # James and 4 of his friends
    friends_count = 4 # and 4 of his friends
    total_volunteers = james_count + friends_count

    # L2
    total_flowers_planted = 200 # a total of 200 flowers
    number_of_days = 2 # In 2 days
    flowers_per_day_total = total_flowers_planted / number_of_days

    # L3
    james_flowers_per_day = flowers_per_day_total / total_volunteers

    # FA
    answer = james_flowers_per_day
    return answer