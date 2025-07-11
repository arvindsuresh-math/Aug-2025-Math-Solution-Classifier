def solve():
    """Index: 713.
    Returns: the number of fewer popsicle sticks the girls brought than the boys.
    """
    # L1
    num_boys = 10 # Ten boys
    sticks_per_boy = 15 # 15 popsicle sticks each
    total_boys_sticks = num_boys * sticks_per_boy

    # L2
    num_girls = 12 # Twelve girls
    sticks_per_girl = 12 # 12 popsicle sticks each
    total_girls_sticks = num_girls * sticks_per_girl

    # L3
    difference_sticks = total_boys_sticks - total_girls_sticks

    # FA
    answer = difference_sticks
    return answer