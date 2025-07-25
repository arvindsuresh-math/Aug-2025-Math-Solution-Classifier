def solve():
    """Index: 2588.
    Returns: the total cost John pays.
    """
    # L1
    num_outside_doors = 2 # two outside doors
    cost_per_outside_door = 20 # $20 each to replace
    total_cost_outside_doors = num_outside_doors * cost_per_outside_door

    # L2
    cost_reference_for_indoor = 20 # The outside doors cost $20 each
    indoor_cost_divisor = 2 # the bedroom doors are half that cost
    cost_per_indoor_door = cost_reference_for_indoor / indoor_cost_divisor

    # L3
    num_bedroom_doors = 3 # 3 bedroom doors
    total_cost_indoor_doors = cost_per_indoor_door * num_bedroom_doors

    # L4
    total_cost = total_cost_outside_doors + total_cost_indoor_doors

    # FA
    answer = total_cost
    return answer