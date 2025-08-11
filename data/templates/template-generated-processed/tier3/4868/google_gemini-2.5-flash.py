def solve():
    """Index: 4868.
    Returns: the total number of whales Ishmael saw across all trips.
    """
    # L1
    male_whales_trip1 = 28 # 28 male whales
    female_multiplier_trip1 = 2 # twice as many female whales
    female_whales_trip1 = male_whales_trip1 * female_multiplier_trip1

    # L2
    total_whales_trip1 = male_whales_trip1 + female_whales_trip1

    # L3
    baby_whale_count_per_group = 1 # WK
    parent_count_per_group = 2 # WK
    whales_per_baby_group = baby_whale_count_per_group + parent_count_per_group

    # L4
    baby_whales_trip2 = 8 # 8 baby whales
    total_whales_trip2 = baby_whales_trip2 * whales_per_baby_group

    # L5
    male_whales_divisor_trip3 = 2 # half as many male whales
    male_whales_trip3 = male_whales_trip1 / male_whales_divisor_trip3

    # L6
    total_whales_trip3 = male_whales_trip3 + female_whales_trip1

    # L7
    total_whales_all_trips = total_whales_trip1 + total_whales_trip2 + total_whales_trip3

    # FA
    answer = total_whales_all_trips
    return answer