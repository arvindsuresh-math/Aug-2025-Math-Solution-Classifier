def solve():
    """Index: 5287.
    Returns: the floor number Dennis lives on.
    """
    # L1
    frank_floor_number = 16 # Frank lives on the 16th floor
    divisor_for_charlie = 4 # 1/4 Frank's floor number
    charlie_floor_number = frank_floor_number / divisor_for_charlie

    # L2
    floors_above_charlie = 2 # Dennis lives two floors above Charlie
    dennis_floor_number = charlie_floor_number + floors_above_charlie

    # FA
    answer = dennis_floor_number
    return answer