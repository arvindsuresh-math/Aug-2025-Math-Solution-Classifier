def solve():
    """Index: 4824.
    Returns: the number of dogs not doing anything.
    """
    # L1
    total_dogs = 88 # There are 88 dogs in a park
    half_divisor = 2 # Half of them are playing with toys
    dogs_playing_with_toys = total_dogs / half_divisor

    # L2
    fourth_divisor = 4 # A fourth of them are barking
    dogs_barking = total_dogs / fourth_divisor

    # L3
    dogs_running = 12 # 12 of the dogs are running
    dogs_not_doing_anything = total_dogs - dogs_running - dogs_playing_with_toys - dogs_barking

    # FA
    answer = dogs_not_doing_anything
    return answer