def solve():
    """Index: 4260.
    Returns: the total number of asparagus spears the caterer will need.
    """
    # L1
    bridgette_guests = 84 # Bridgette is inviting 84 guests
    alex_multiplier_numerator = 2 # two thirds of that number
    alex_multiplier_denominator = 3 # two thirds of that number
    alex_guests = bridgette_guests * alex_multiplier_numerator / alex_multiplier_denominator

    # L2
    total_guests = bridgette_guests + alex_guests

    # L3
    extra_plates = 10 # ten extra plates
    total_plates_needed = total_guests + extra_plates

    # L4
    asparagus_per_plate = 8 # 8 asparagus spears on it
    total_asparagus_spears = total_plates_needed * asparagus_per_plate

    # FA
    answer = total_asparagus_spears
    return answer