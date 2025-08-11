def solve():
    """Index: 4427.
    Returns: the total number of wheels Naomi saw at the park.
    """
    # L1
    num_regular_bikes = 7 # 7 regular bikes
    wheels_per_regular_bike = 2 # Regular bikes have 2 wheels
    wheels_regular_bikes = num_regular_bikes * wheels_per_regular_bike

    # L2
    num_childrens_bikes = 11 # 11 children’s bikes
    wheels_per_childrens_bike = 4 # kid’s bikes have 4 wheels
    wheels_childrens_bikes = num_childrens_bikes * wheels_per_childrens_bike

    # L3
    total_wheels = wheels_regular_bikes + wheels_childrens_bikes

    # FA
    answer = total_wheels
    return answer