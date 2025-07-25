from fractions import Fraction

def solve():
    """Index: 3446.
    Returns: the combined total number of wheels for bicycles and tricycles.
    """
    # L1
    bicycle_fraction = Fraction(3, 5) # 3/5 of them are riding on bicycles
    total_people = 40 # 40 people in the race
    num_bicyclists = bicycle_fraction * total_people

    # L2
    wheels_per_bicycle = 2 # a bicycle has 2 wheels
    total_bicycle_wheels = wheels_per_bicycle * num_bicyclists

    # L3
    num_tricyclists = total_people - num_bicyclists

    # L4
    wheels_per_tricycle = 3 # a tricycle has 3 wheels
    total_tricycle_wheels = wheels_per_tricycle * num_tricyclists

    # L5
    combined_total_wheels = total_bicycle_wheels + total_tricycle_wheels

    # FA
    answer = combined_total_wheels
    return answer