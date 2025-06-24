def solve_32():
    # Given distances
    distance_after_1st_turn = 5  # meters
    distance_after_2nd_turn = 8  # meters
    distance_after_4th_turn = 0  # meters, as it immediately exits
    total_distance_around_ring = 23  # meters

    # Calculate the sum of known distances traveled around the ring
    known_distances_sum = distance_after_1st_turn + distance_after_2nd_turn + distance_after_4th_turn

    # Calculate the distance traveled after the 3rd turn
    distance_after_3rd_turn = total_distance_around_ring - known_distances_sum

    return distance_after_3rd_turn

# Execute the function to get the answer
# print(solve_32())