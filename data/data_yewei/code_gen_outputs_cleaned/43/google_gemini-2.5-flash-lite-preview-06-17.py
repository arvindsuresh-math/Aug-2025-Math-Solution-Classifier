# Calculate the number of buildings that collapsed after each earthquake
buildings_first_earthquake = 4
buildings_second_earthquake = buildings_first_earthquake * 2
buildings_third_earthquake = buildings_second_earthquake * 2
buildings_fourth_earthquake = buildings_third_earthquake * 2

# Calculate the total number of collapsed buildings
total_collapsed_buildings = (
    buildings_first_earthquake
    + buildings_second_earthquake
    + buildings_third_earthquake
    + buildings_fourth_earthquake
)

# Print the result
print(total_collapsed_buildings)