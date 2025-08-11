def solve():
    """Index: 2183.
    Returns: the total number of wooden planks Andrew bought to start with.
    """
    # L1
    bedroom_planks = 8 # his bedroom took eight wooden planks
    guest_bedroom_fewer = 2 # guest bedroom took two fewer planks than Andrew’s bedroom
    guest_bedroom_planks = bedroom_planks - guest_bedroom_fewer

    # L2
    num_hallways = 2 # each of his two hallways
    hallway_planks_each = 4 # each of his two hallways took four planks
    hallway_planks = num_hallways * hallway_planks_each

    # L3
    ruined_per_bedroom = 3 # ruined three planks in each bedroom
    num_bedrooms_ruined = 2 # in two bedrooms
    extra_bedroom_planks = ruined_per_bedroom * num_bedrooms_ruined

    # L4
    living_room_planks = 20 # his living room took twenty planks
    kitchen_planks = 11 # his kitchen took eleven planks
    total_used = bedroom_planks + living_room_planks + kitchen_planks + guest_bedroom_planks + hallway_planks + extra_bedroom_planks

    # L5
    leftover_planks = 6 # he ended up with six leftover planks at the end
    total_bought = total_used + leftover_planks

    # FA
    answer = total_bought
    return answer