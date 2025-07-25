def solve():
    """Index: 4437.
    Returns: the distance between table 1 and table 3 in meters.
    """
    # L1
    last_year_race_length = 300 # Last year, the race was 300 meters
    length_multiplier = 4 # it will be 4 times as long
    current_race_length = last_year_race_length * length_multiplier

    # L2
    num_tables = 6 # Giselle needs to set up 6 tables
    distance_between_adjacent_tables = current_race_length / num_tables

    # L3
    segments_between_table1_and_table3 = 2 # distance between table 1 and table 3
    distance_table1_to_table3 = distance_between_adjacent_tables * segments_between_table1_and_table3

    # FA
    answer = distance_table1_to_table3
    return answer