from fractions import Fraction

def solve():
    """Index: 4604.
    Returns: the total number of people on the bus.
    """
    # L1
    girls_more_fraction = Fraction(2, 5) # 2/5 times more girls
    boys_count = 50 # total number of boys on the trip is 50
    additional_girls = girls_more_fraction * boys_count

    # L2
    total_girls = boys_count + additional_girls

    # L3
    staff_count = 3 # a driver and an assistant, and the teacher also drives
    total_people = total_girls + boys_count + staff_count

    # FA
    answer = total_people
    return answer