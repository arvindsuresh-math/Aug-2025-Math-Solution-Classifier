def solve():
    """Index: 5124.
    Returns: the total time until all her fields are fertilized.
    """
    # L1
    gallons_per_horse_per_day = 5 # One horse produces 5 gallons of fertilizer per day
    num_horses = 80 # If Janet has 80 horses
    fertilizer_produced_per_day = gallons_per_horse_per_day * num_horses

    # L2
    gallons_per_acre = 400 # Each acre needs 400 gallons of fertilizer
    total_acres = 20 # spread it over 20 acres of farmland
    total_fertilizer_needed = gallons_per_acre * total_acres

    # L3
    days_to_collect_fertilizer = total_fertilizer_needed / fertilizer_produced_per_day

    # L4
    acres_per_day_spread = 4 # Janet can spread fertilizer over 4 acres per day
    days_to_spread_fertilizer = total_acres / acres_per_day_spread

    # L5
    total_time_days = days_to_spread_fertilizer + days_to_collect_fertilizer

    # FA
    answer = total_time_days
    return answer