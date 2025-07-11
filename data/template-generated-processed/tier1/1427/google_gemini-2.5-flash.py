def solve():
    """Index: 1427.
    Returns: the total number of remaining animals in the adoption center.
    """
    # L1
    initial_dogs = 200 # The total number of dogs at an animal rescue center is 200
    dogs_moved_in = 100 # 100 dogs at another rescue center are to be moved
    dogs_after_intake = initial_dogs + dogs_moved_in

    # L2
    adopted_after_week = 40 # gives out 40 animals for adoption
    dogs_after_week_adoption = dogs_after_intake - adopted_after_week

    # L3
    adopted_after_month = 60 # 60 more dogs were adopted
    remaining_dogs = dogs_after_week_adoption - adopted_after_month

    # FA
    answer = remaining_dogs
    return answer