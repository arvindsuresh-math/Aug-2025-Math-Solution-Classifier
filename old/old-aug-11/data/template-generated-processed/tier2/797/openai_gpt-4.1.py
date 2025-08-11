def solve():
    """Index: 797.
    Returns: the total number of cups of dog food Hannah should prepare in a day for her three dogs.
    """
    # L1
    first_dog_cups = 1.5 # first dog eats 1.5 cups of dog food a day
    twice = 2 # second dog eats twice as much
    second_dog_cups = first_dog_cups * twice

    # L2
    more_than_second = 2.5 # third dog eats 2.5 cups more than the second dog
    third_dog_cups = second_dog_cups + more_than_second

    # L3
    total_cups = first_dog_cups + second_dog_cups + third_dog_cups

    # FA
    answer = total_cups
    return answer