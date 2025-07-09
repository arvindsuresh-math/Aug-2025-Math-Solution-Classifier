def solve():
    # Initial number of balls in the first batch
    first_batch_balls = 100
    # Fraction of balls hit in the first batch
    fraction_hit_first_batch = 2/5
    # Fraction of balls NOT hit in the first batch
    fraction_not_hit_first_batch = 1 - fraction_hit_first_batch
    # Number of balls not hit in the first batch
    balls_not_hit_first_batch = int(first_batch_balls * fraction_not_hit_first_batch)

    # Number of balls in the second batch
    second_batch_balls = 75
    # Fraction of balls hit in the second batch
    fraction_hit_second_batch = 1/3
    # Fraction of balls NOT hit in the second batch
    fraction_not_hit_second_batch = 1 - fraction_hit_second_batch
    # Number of balls not hit in the second batch
    balls_not_hit_second_batch = int(second_batch_balls * fraction_not_hit_second_batch)

    # Total number of balls not hit
    total_balls_not_hit = balls_not_hit_first_batch + balls_not_hit_second_batch

    return total_balls_not_hit

# Execute the function to get the answer
answer = solve()