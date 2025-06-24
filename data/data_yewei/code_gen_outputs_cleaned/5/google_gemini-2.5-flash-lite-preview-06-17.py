# Calculate the number of purple flowers
yellow_flowers = 10
purple_flowers_increase = 0.80
num_purple_flowers = yellow_flowers + (yellow_flowers * purple_flowers_increase)

# Calculate the number of green flowers
green_flowers_percentage = 0.25
total_yellow_purple = yellow_flowers + num_purple_flowers
num_green_flowers = total_yellow_purple * green_flowers_percentage

# Calculate the total number of flowers
total_flowers = yellow_flowers + num_purple_flowers + num_green_flowers

# Print the results for each step
print(f"Number of yellow flowers: {yellow_flowers}")
print(f"Number of purple flowers: {int(num_purple_flowers)}")
print(f"Total yellow and purple flowers: {int(total_yellow_purple)}")
print(f"Number of green flowers: {int(num_green_flowers)}")
print(f"Total flowers in the garden: {int(total_flowers)}")

def solve_5():
    yellow_flowers = 10
    purple_flowers_increase = 0.80
    num_purple_flowers = yellow_flowers + (yellow_flowers * purple_flowers_increase)
    
    green_flowers_percentage = 0.25
    total_yellow_purple = yellow_flowers + num_purple_flowers
    num_green_flowers = total_yellow_purple * green_flowers_percentage
    
    total_flowers = yellow_flowers + num_purple_flowers + num_green_flowers
    
    return int(total_flowers)