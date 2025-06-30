def solve():
    # Dimensions of the aquarium
    length_ft = 4
    width_ft = 6
    height_ft = 3

    # L1: Calculate the total volume of the aquarium
    total_volume_cubic_ft = length_ft * width_ft * height_ft

    # Initial state: aquarium is filled halfway
    initial_fill_proportion = 0.5

    # Cat spills half the water that was in it
    # L2: Proportion after cat spills
    proportion_after_spill = initial_fill_proportion * 0.5

    # Nancy triples the amount of water in the aquarium
    # L3: Proportion after Nancy refills
    proportion_after_refill = proportion_after_spill * 3

    # L4: Calculate the final volume of water in the aquarium
    final_water_volume_cubic_ft = total_volume_cubic_ft * proportion_after_refill

    return final_water_volume_cubic_ft

# Execute the function to get the answer
# print(solve())