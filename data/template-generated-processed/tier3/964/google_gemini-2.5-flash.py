def solve():
    """Index: 964.
    Returns: the number of additional wings Alan must eat per minute to beat Kevin's record.
    """
    # L1
    kevin_total_wings = 64 # He can eat 64 wings
    kevin_time_minutes = 8 # in 8 minutes
    kevin_wings_per_minute = kevin_total_wings / kevin_time_minutes

    # L2
    alan_current_rate = 5 # He is currently able to eat 5 hot wings per minute
    wings_to_equal_record = kevin_wings_per_minute - alan_current_rate

    # L3
    beat_record_extra = 1 # WK
    wings_to_beat_record = wings_to_equal_record + beat_record_extra

    # FA
    answer = wings_to_beat_record
    return answer