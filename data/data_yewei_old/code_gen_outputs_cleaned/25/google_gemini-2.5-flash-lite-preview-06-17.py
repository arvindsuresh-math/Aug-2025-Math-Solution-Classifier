# Calculate the number of balls Ralph did not hit from the first 100 balls.
balls_not_hit_first_100 = (1 - 2/5) * 100

# Calculate the number of balls Ralph did not hit from the next 75 balls.
balls_not_hit_next_75 = (1 - 1/3) * 75

# Calculate the total number of balls Ralph did not hit.
total_balls_not_hit = balls_not_hit_first_100 + balls_not_hit_next_75

# Print the result
print(f"Ralph did not hit {total_balls_not_hit} tennis balls.")