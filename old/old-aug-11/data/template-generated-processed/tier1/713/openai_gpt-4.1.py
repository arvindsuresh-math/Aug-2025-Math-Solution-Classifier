def solve():
    """Index: 713.
    Returns: how many fewer popsicle sticks the girls brought than the boys.
    """
    # L1
    num_boys = 10 # Ten boys
    sticks_per_boy = 15 # 15 popsicle sticks each
    boys_total = num_boys * sticks_per_boy

    # L2
    num_girls = 12 # Twelve girls
    sticks_per_girl = 12 # 12 popsicle sticks each
    girls_total = num_girls * sticks_per_girl

    # L3
    fewer_sticks = boys_total - girls_total

    # FA
    answer = fewer_sticks
    return answer