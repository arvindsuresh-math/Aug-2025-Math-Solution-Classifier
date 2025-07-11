from fractions import Fraction

def solve():
    """Index: 2742.
    Returns: the number of candies each person received.
    """
    # L1
    total_candies = 300 # Henley bought 300 candies
    sour_percentage = Fraction(40, 100) # 40% of them were sour
    sour_candies = sour_percentage * total_candies

    # L2
    good_candies = total_candies - sour_candies

    # L3
    henley = 1 # Henley
    brothers = 2 # her two brothers
    num_people = henley + brothers

    # L4
    candies_per_person = good_candies / num_people

    # FA
    answer = candies_per_person
    return answer