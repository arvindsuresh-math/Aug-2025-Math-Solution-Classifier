def solve():
    """Index: 3196.
    Returns: the number of candies each person will have.
    """
    # L1
    mark_candies = 30 # Mark has 30 candies
    peter_candies = 25 # Peter has 25 candies
    john_candies = 35 # John has 35 candies
    total_candies = mark_candies + peter_candies + john_candies

    # L2
    number_of_people = 3 # They decided to combine their candies together and share them equally.
    candies_per_person = total_candies / number_of_people

    # FA
    answer = candies_per_person
    return answer