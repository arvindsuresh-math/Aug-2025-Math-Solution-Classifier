def solve_43():
    # Initial number of buildings collapsed in the first earthquake
    initial_collapsed_buildings = 4

    # Number of additional earthquakes after the first one
    num_additional_earthquakes = 3

    # List to store the number of collapsed buildings for each earthquake
    collapsed_buildings_per_earthquake = [initial_collapsed_buildings]

    # Calculate collapsed buildings for subsequent earthquakes
    current_collapsed = initial_collapsed_buildings
    for _ in range(num_additional_earthquakes):
        current_collapsed *= 2
        collapsed_buildings_per_earthquake.append(current_collapsed)

    # Calculate the total number of buildings collapsed
    total_collapsed_buildings = sum(collapsed_buildings_per_earthquake)

    return total_collapsed_buildings

# Execute the function to get the answer
# print(solve_43())