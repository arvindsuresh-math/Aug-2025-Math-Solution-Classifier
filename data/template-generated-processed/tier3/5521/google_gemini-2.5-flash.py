def solve():
    """Index: 5521.
    Returns: the latest time the head baker can arrive at the store.
    """
    # L1
    room_temp_time_hours = 1 # 1 hour for refrigerated dough to come to room temperature
    proof_time_hours = 2 # 2 hours to proof
    total_hours_temp_proof = room_temp_time_hours + proof_time_hours

    # L2
    shape_time_minutes = 15 # 15 minutes to shape the dough
    bake_time_minutes = 30 # 30 minutes to bake
    cool_time_minutes = 15 # 15 minutes to cool
    total_minutes_shape_bake_cool = shape_time_minutes + bake_time_minutes + cool_time_minutes

    # L3
    minutes_per_hour = 60 # WK
    minutes_to_hours_conversion = total_minutes_shape_bake_cool / minutes_per_hour

    # L4
    total_prep_time_hours = total_hours_temp_proof + minutes_to_hours_conversion

    # L5
    opening_hour = 6 # bakery opens at 6:00 am
    arrival_hour = opening_hour - total_prep_time_hours

    # FA
    answer = arrival_hour
    return answer