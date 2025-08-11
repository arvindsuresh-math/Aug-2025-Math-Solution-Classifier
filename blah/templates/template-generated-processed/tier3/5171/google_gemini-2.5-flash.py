def solve():
    """Index: 5171.
    Returns: the total number of bags of soil needed.
    """
    # L1
    bed_length = 8 # 8 feet long
    bed_width = 4 # 4 feet wide
    bed_height = 1 # 1 foot high
    cubic_feet_per_bed = bed_length * bed_width * bed_height

    # L2
    num_beds = 2 # 2 raised beds
    total_cubic_feet_needed = num_beds * cubic_feet_per_bed

    # L3
    cubic_feet_per_bag = 4 # Each bag of soil has 4 cubic feet
    total_bags_needed = total_cubic_feet_needed / cubic_feet_per_bag

    # FA
    answer = total_bags_needed
    return answer